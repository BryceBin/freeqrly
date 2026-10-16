// Shared helpers for FreeQrly Tier 2 account system (auth + sessions + rate limits).
// Secrets come from env only (GOOGLE_*/GITHUB_*_CLIENT_*, RESEND_API_KEY,
// TURNSTILE_SECRET_KEY, APP_URL). Never hardcode, never log raw tokens — only SHA-256 hashes.
// Passwords are NEVER logged and NEVER returned in any API response.
import { sha256Hex } from './dynamic.js';

export const SESSION_COOKIE = 'fq_session';
export const PKCE_COOKIE = 'fq_pkce';
export const OAUTH_STATE_COOKIE = 'fq_oauth_state';
export const SESSION_MAX_AGE = 30 * 24 * 3600; // 30 days
export const REAUTH_WINDOW_MS = 15 * 60 * 1000; // delete-account requires session < 15 min old
export const VERIFY_TOKEN_TTL_MS = 24 * 3600 * 1000; // email-verification tokens: 24 h
export const RESET_TOKEN_TTL_MS = 3600 * 1000; // password-reset tokens: 1 h
export const MIN_PASSWORD_LEN = 8;
export const LOGIN_MAX_FAILURES = 5; // failures per IP+email before lockout
export const LOGIN_LOCKOUT_MS = 15 * 60 * 1000; // 15 min lockout

export const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

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
     VALUES (?, ?, 1, ?, ?, ?, 'free', 8, ?, ?)
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

// ---- Post-auth redirect target (`next`) ----
// Only a same-origin path is allowed: must start with a SINGLE '/'; rejects
// '//', backslashes, and scheme-like prefixes ('/http:', '/javascript:', ...).
// Anything invalid → fallback. Used for email-link ?next= and OAuth state.
export function validateNext(next, fallback = '/dashboard/') {
  if (typeof next !== 'string' || !next) return fallback;
  if (next.includes('\\') || next.includes('\n') || next.includes('\r') || next.includes('\0')) return fallback;
  if (!next.startsWith('/') || next.startsWith('//')) return fallback;
  if (/^\/[a-z][a-z0-9+.-]*:/i.test(next)) return fallback; // '/http:', '/javascript:', ...
  return next;
}

// URL of the verified landing page: /login/?verified=1&next=<validated next>.
// The email-verification click lands here (frontend shows the "verified"
// state, then continues to `next`).
export function loginVerifiedUrl(origin, next) {
  const u = new URL('/login/', origin);
  u.searchParams.set('verified', '1');
  u.searchParams.set('next', validateNext(next));
  return u.toString();
}

// ---- Passwords (PBKDF2-SHA256, 100k iterations, random 16-byte salt) ----
// Stored format: pbkdf2$100000$<salt_b64>$<hash_b64>. Plaintext is never stored.
// Standard base64 (with +/=) is fine — the value lives in a TEXT column only.
function b64encode(bytes) {
  let s = '';
  for (const b of bytes) s += String.fromCharCode(b);
  return btoa(s);
}
function b64decode(str) {
  const bin = atob(str);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

export async function hashPassword(password) {
  const salt = new Uint8Array(16);
  crypto.getRandomValues(salt);
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(password), 'PBKDF2', false, ['deriveBits']);
  const bits = await crypto.subtle.deriveBits(
    { name: 'PBKDF2', salt, iterations: 100000, hash: 'SHA-256' }, key, 256);
  return `pbkdf2$100000$${b64encode(salt)}$${b64encode(new Uint8Array(bits))}`;
}

export async function verifyPassword(password, stored) {
  try {
    if (typeof stored !== 'string') return false;
    const parts = stored.split('$');
    if (parts.length !== 4 || parts[0] !== 'pbkdf2' || parts[1] !== '100000') return false;
    const salt = b64decode(parts[2]);
    const expected = b64decode(parts[3]);
    const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(password), 'PBKDF2', false, ['deriveBits']);
    const bits = await crypto.subtle.deriveBits(
      { name: 'PBKDF2', salt, iterations: 100000, hash: 'SHA-256' }, key, 256);
    const actual = new Uint8Array(bits);
    if (actual.length !== expected.length) return false;
    let diff = 0;
    for (let i = 0; i < actual.length; i++) diff |= actual[i] ^ expected[i];
    return diff === 0;
  } catch { return false; }
}

// ---- Password-account users ----
export async function getUserByEmail(env, email) {
  return env.DB.prepare('SELECT * FROM users WHERE email = ?').bind(email).first();
}

// Creates a password-account user (email_verified=0 until they click the
// verification link). Callers must check for an existing email FIRST and
// return 409 already_registered — never reveal which method an email used.
export async function createPasswordUser(env, email, passwordHash) {
  const now = Date.now();
  const id = genToken(16);
  await env.DB.prepare(
    `INSERT INTO users (id, email, email_verified, name, avatar_url, auth_provider, plan, code_limit, created_at, last_login_at, password_hash)
     VALUES (?, ?, 0, NULL, NULL, 'password', 'free', 8, ?, NULL, ?)`
  ).bind(id, email, now, passwordHash).run();
  return env.DB.prepare('SELECT * FROM users WHERE email = ?').bind(email).first();
}

// ---- One-time email tokens (verification / reset) ----
// Only the SHA-256 hash is stored; tokens are single-use (used=1 after consume).
export async function createEmailToken(env, userId, purpose, ttlMs) {
  const token = genToken(32);
  const tokenHash = await sha256Hex(token);
  await env.DB.prepare(
    'INSERT INTO email_tokens (token_hash, user_id, purpose, expires_at, used) VALUES (?, ?, ?, ?, 0)'
  ).bind(tokenHash, userId, purpose, Date.now() + ttlMs).run();
  return token;
}

// ---- Resend email (shared by register / forgot / unverified-login resend) ----
export async function sendResendEmail(env, { to, subject, html, text }) {
  if (!env.RESEND_API_KEY) return false;
  try {
    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: 'FreeQrly <login@freeqrly.com>',
        to, subject, html, text,
      }),
    });
    if (!res.ok) console.error('Resend send failed:', res.status, await res.text().catch(() => ''));
    return res.ok;
  } catch (e) {
    console.error('Resend send error:', e);
    return false;
  }
}

// ---- Login lockout: 5 failures per IP+email → 15 min lockout ----
// Dedicated login_lockouts table (exact 15-min window; the hourly rate_limits
// buckets can't express a rolling 15-min lockout). Fail-open on DB errors,
// matching the existing checkRateLimit behaviour.
export function loginLockoutKey(ip, email) {
  return sha256Hex(`${ip}|${email.toLowerCase()}`);
}

export async function checkLoginLockout(env, key) {
  try {
    const row = await env.DB.prepare(
      'SELECT failures, locked_until FROM login_lockouts WHERE key = ?'
    ).bind(key).first();
    if (row && row.locked_until > Date.now()) {
      return { locked: true, retryAfterSeconds: Math.ceil((row.locked_until - Date.now()) / 1000) };
    }
    return { locked: false };
  } catch { return { locked: false }; }
}

export async function recordLoginFailure(env, key) {
  try {
    const now = Date.now();
    const row = await env.DB.prepare(
      'SELECT failures, locked_until FROM login_lockouts WHERE key = ?'
    ).bind(key).first();
    // Expired lockout → fresh count starting at 1. Active lockout → leave alone.
    let failures = 1;
    let lockedUntil = 0;
    if (row) {
      if (row.locked_until > now) return;
      failures = (row.locked_until && row.failures >= LOGIN_MAX_FAILURES) ? 1 : (row.failures || 0) + 1;
    }
    if (failures >= LOGIN_MAX_FAILURES) lockedUntil = now + LOGIN_LOCKOUT_MS;
    await env.DB.prepare(
      `INSERT INTO login_lockouts (key, failures, locked_until, updated_at) VALUES (?, ?, ?, ?)
       ON CONFLICT(key) DO UPDATE SET failures = excluded.failures, locked_until = excluded.locked_until, updated_at = excluded.updated_at`
    ).bind(key, failures, lockedUntil, now).run();
  } catch { /* fail-open */ }
}

export async function clearLoginFailures(env, key) {
  try {
    await env.DB.prepare('DELETE FROM login_lockouts WHERE key = ?').bind(key).run();
  } catch { /* ignore */ }
}
