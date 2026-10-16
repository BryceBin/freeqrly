// Shared helpers for FreeQrly Tier 2 account system (auth + sessions + rate limits).
// Secrets come from env only (GOOGLE_*/GITHUB_*_CLIENT_*, RESEND_API_KEY,
// TURNSTILE_SECRET_KEY, APP_URL). Never hardcode, never log raw tokens — only SHA-256 hashes.
import { sha256Hex } from './dynamic.js';

export const SESSION_COOKIE = 'fq_session';
export const PKCE_COOKIE = 'fq_pkce';
export const OAUTH_STATE_COOKIE = 'fq_oauth_state';
export const SESSION_MAX_AGE = 30 * 24 * 3600; // 30 days
export const REAUTH_WINDOW_MS = 15 * 60 * 1000; // delete-account requires session < 15 min old
export const MAGIC_LINK_TTL_MS = 15 * 60 * 1000; // 15 min

export function appUrl(env) {
  return (env.APP_URL || 'https://freeqrly.com').replace(/\/+$/, '');
}

export function getClientIp(request) {
  return request.headers.get('CF-Connecting-IP') || 'unknown';
}

// ---- Random tokens (opaque, base64url) ----
export function genToken(bytes = 32) {
  const arr = new Uint8Array(bytes);
  crypto.getRandomValues(arr);
  let s = '';
  for (const b of arr) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

export async function sha256Base64Url(str) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(str));
  let s = '';
  for (const b of new Uint8Array(buf)) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

// ---- Cookies ----
export function getCookie(request, name) {
  const header = request.headers.get('Cookie') || '';
  for (const part of header.split(';')) {
    const [k, ...rest] = part.trim().split('=');
    if (k === name) return decodeURIComponent(rest.join('='));
  }
  return '';
}

function cookieStr(name, value, maxAge) {
  return `${name}=${encodeURIComponent(value)}; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=${maxAge}`;
}

export function sessionCookie(token, maxAge = SESSION_MAX_AGE) {
  return cookieStr(SESSION_COOKIE, token, maxAge);
}

export function clearSessionCookie() {
  return cookieStr(SESSION_COOKIE, '', 0);
}

export function tempCookie(name, value, maxAge = 600) {
  return cookieStr(name, value, maxAge);
}

export function clearTempCookie(name) {
  return cookieStr(name, '', 0);
}

// ---- Sessions ----
export async function createSession(env, userId, request) {
  const token = genToken(32);
  const hash = await sha256Hex(token);
  const now = Date.now();
  await env.DB.prepare(
    'INSERT INTO sessions (token_hash, user_id, created_at, expires_at, user_agent, ip) VALUES (?, ?, ?, ?, ?, ?)'
  ).bind(hash, userId, now, now + SESSION_MAX_AGE * 1000,
    request ? (request.headers.get('User-Agent') || '') : '', request ? getClientIp(request) : '').run();
  return token;
}

export async function deleteSessionByToken(env, token) {
  if (!token) return;
  const hash = await sha256Hex(token);
  await env.DB.prepare('DELETE FROM sessions WHERE token_hash = ?').bind(hash).run();
}

// Returns { session, user } or null. session.user_id / session.created_at used by callers.
export async function getSessionUser(env, request) {
  const token = getCookie(request, SESSION_COOKIE);
  if (!token) return null;
  const hash = await sha256Hex(token);
  const row = await env.DB.prepare(
    `SELECT s.token_hash AS token_hash, s.user_id AS user_id, s.created_at AS created_at,
            s.expires_at AS expires_at,
            u.id AS id, u.email AS email, u.name AS name, u.avatar_url AS avatar_url,
            u.plan AS plan, u.code_limit AS code_limit
     FROM sessions s JOIN users u ON u.id = s.user_id WHERE s.token_hash = ?`
  ).bind(hash).first();
  if (!row) return null;
  if (row.expires_at <= Date.now()) {
    try { await env.DB.prepare('DELETE FROM sessions WHERE token_hash = ?').bind(hash).run(); } catch { /* ignore */ }
    return null;
  }
  return {
    session: { token_hash: row.token_hash, user_id: row.user_id, created_at: row.created_at, expires_at: row.expires_at },
    user: { id: row.id, email: row.email, name: row.name, avatar_url: row.avatar_url, plan: row.plan, code_limit: row.code_limit },
  };
}

// ---- Users ----
export async function upsertUser(env, { email, name, avatar_url, auth_provider }) {
  const now = Date.now();
  const id = genToken(16);
  await env.DB.prepare(
    `INSERT INTO users (id, email, email_verified, name, avatar_url, auth_provider, plan, code_limit, created_at, last_login_at)
     VALUES (?, ?, 1, ?, ?, ?, 'free', 3, ?, ?)
     ON CONFLICT(email) DO UPDATE SET
       name = COALESCE(excluded.name, users.name),
       avatar_url = COALESCE(excluded.avatar_url, users.avatar_url),
       auth_provider = excluded.auth_provider,
       last_login_at = excluded.last_login_at`
  ).bind(id, email, name || null, avatar_url || null, auth_provider, now, now).run();
  return env.DB.prepare('SELECT * FROM users WHERE email = ?').bind(email).first();
}

export async function getCodeCount(env, userId) {
  const row = await env.DB.prepare('SELECT COUNT(*) AS n FROM codes WHERE user_id = ?').bind(userId).first();
  return (row && row.n) || 0;
}

// ---- Rate limits (D1 counting, same pattern as create_limits) ----
// Returns true if allowed (and increments), false if over limit. Fail-open on DB errors.
export async function checkRateLimit(env, key, limit) {
  const hour = new Date().toISOString().slice(0, 13);
  try {
    const row = await env.DB.prepare('SELECT count FROM rate_limits WHERE key = ? AND hour = ?').bind(key, hour).first();
    if (row && row.count >= limit) return false;
    await env.DB.prepare(
      `INSERT INTO rate_limits (key, hour, count) VALUES (?, ?, 1)
       ON CONFLICT(key, hour) DO UPDATE SET count = count + 1`
    ).bind(key, hour).run();
    return true;
  } catch { return true; }
}

// ---- Turnstile (Cloudflare siteverify) ----
// No TURNSTILE_SECRET_KEY in env → warn + proceed (per spec: do NOT hard-fail).
// Token present but verification fails → { ok: false }.
export async function verifyTurnstile(env, token, ip) {
  const secret = env.TURNSTILE_SECRET_KEY;
  if (!secret) {
    console.warn('Turnstile secret (TURNSTILE_SECRET_KEY) not set; skipping verification');
    return { ok: true, skipped: true };
  }
  if (!token) return { ok: false, reason: 'missing_token' };
  try {
    const res = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ secret, response: token, ...(ip && ip !== 'unknown' ? { remoteip: ip } : {}) }),
    });
    const data = await res.json();
    return { ok: !!data.success };
  } catch {
    return { ok: false, reason: 'verify_error' };
  }
}

// ---- OAuth provider config (env-driven) ----
export function oauthProviderConfig(env, provider) {
  const map = {
    google: {
      clientId: env.GOOGLE_CLIENT_ID, clientSecret: env.GOOGLE_CLIENT_SECRET,
      authorize: 'https://accounts.google.com/o/oauth2/v2/auth',
      token: 'https://oauth2.googleapis.com/token',
      scope: 'openid email profile', pkce: true,
    },
    github: {
      clientId: env.GITHUB_CLIENT_ID, clientSecret: env.GITHUB_CLIENT_SECRET,
      authorize: 'https://github.com/login/oauth/authorize',
      token: 'https://github.com/login/oauth/access_token',
      scope: 'read:user user:email', pkce: false,
    },
  };
  return map[provider] || null;
}

export function redirectTo(url, extraHeaders = {}) {
  return new Response(null, { status: 302, headers: { Location: url, ...extraHeaders } });
}
