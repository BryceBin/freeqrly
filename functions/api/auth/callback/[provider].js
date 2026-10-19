// GET /api/auth/callback/:provider — OAuth callback.
// Verifies state cookie, exchanges code server-side (PKCE for Google;
// GitHub's OAuth web flow does NOT support PKCE), fetches the user email,
// upserts the user, creates a session, redirects to the validated `next`
// carried in the state cookie (default /dashboard/).
// Failures redirect to /login/?error=<reason>.
import { oauthProviderConfig, appUrl, getCookie, getClientIp,
  PKCE_COOKIE, OAUTH_STATE_COOKIE, createSession, sessionCookie,
  clearTempCookie, checkRateLimit, upsertUser, redirectTo, validateNext } from '../../../_lib/auth.js';

async function fetchJson(url, init = {}) {
  const res = await fetch(url, init);
  if (!res.ok) throw new Error(`fetch ${url} -> ${res.status}`);
  return res.json();
}

export async function onRequestGet({ request, env, params }) {
  const url = new URL(request.url);
  const provider = (params.provider || '').toLowerCase();
  const login = (err) => redirectTo(new URL(`/login/?error=${err}`, url.origin).toString());
  const cfg = oauthProviderConfig(env, provider);
  if (!cfg || !cfg.clientId || !cfg.clientSecret) return login('provider_unavailable');
  if (url.searchParams.get('error')) return login('provider_denied');

  // CSRF: state cookie must match query state. The cookie holds
  // JSON { s: state, n: next } (new) or a bare state string (pre-change flows
  // still in flight during deploy — accept both).
  const stateCookieRaw = getCookie(request, OAUTH_STATE_COOKIE);
  let stateCookie = stateCookieRaw;
  let next = '/dashboard/';
  try {
    const parsed = JSON.parse(stateCookieRaw);
    if (parsed && typeof parsed.s === 'string') {
      stateCookie = parsed.s;
      next = validateNext(parsed.n || '');
    }
  } catch { /* not JSON → bare state string, next stays default */ }
  const stateQuery = url.searchParams.get('state') || '';
  // Missing cookie/query (expired tab, cookies blocked, or >30 min on the
  // provider page) is a different failure from a genuine state mismatch —
  // keep them distinguishable for diagnostics.
  if (!stateCookie || !stateQuery) return login('oauth_expired');
  if (stateCookie !== stateQuery) return login('csrf');

  // Per-IP callback attempt limit (D1 counting)
  if (!(await checkRateLimit(env, 'oauth:ip:' + getClientIp(request), 20))) return login('rate_limited');

  const code = url.searchParams.get('code') || '';
  if (!code) return login('missing_code');
  const redirectUri = `${appUrl(env)}/api/auth/callback/${provider}`;

  // Exchange code for tokens
  let tokens;
  try {
    const form = new URLSearchParams({
      client_id: cfg.clientId, client_secret: cfg.clientSecret,
      code, grant_type: 'authorization_code', redirect_uri: redirectUri,
    });
    if (cfg.pkce) {
      const verifier = getCookie(request, PKCE_COOKIE);
      if (!verifier) return login('oauth_expired');
      form.set('code_verifier', verifier);
    }
    const res = await fetch(cfg.token, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded', Accept: 'application/json' },
      body: form,
    });
    if (!res.ok) return login('token_exchange_failed');
    tokens = await res.json();
    if (tokens.error) return login('token_exchange_failed');
  } catch { return login('token_exchange_failed'); }
  const accessToken = tokens.access_token;
  if (!accessToken) return login('token_exchange_failed');

  // Fetch user email (+ name/avatar)
  let email = '', name = null, avatarUrl = null;
  try {
    if (provider === 'google') {
      const me = await fetchJson('https://www.googleapis.com/oauth2/v3/userinfo', {
        headers: { Authorization: `Bearer ${accessToken}` },
      });
      if (me.email_verified !== undefined && me.email_verified !== true && me.email_verified !== 'true') {
        return login('no_verified_email');
      }
      email = me.email || ''; name = me.name || null; avatarUrl = me.picture || null;
    } else if (provider === 'github') {
      const me = await fetchJson('https://api.github.com/user', {
        headers: { Authorization: `Bearer ${accessToken}`, Accept: 'application/vnd.github+json', 'User-Agent': 'FreeQrly' },
      });
      name = me.name || me.login || null; avatarUrl = me.avatar_url || null;
      email = me.email || '';
      if (!email) {
        const emails = await fetchJson('https://api.github.com/user/emails', {
          headers: { Authorization: `Bearer ${accessToken}`, Accept: 'application/vnd.github+json', 'User-Agent': 'FreeQrly' },
        });
        const primary = (Array.isArray(emails) ? emails : []).find((e) => e.primary && e.verified)
          || (Array.isArray(emails) ? emails : []).find((e) => e.verified);
        email = primary ? primary.email : '';
      }
      if (!email) return login('no_verified_email');
    }
  } catch { return login('profile_fetch_failed'); }

  const user = await upsertUser(env, { email, name, avatar_url: avatarUrl, auth_provider: provider });
  const sessionToken = await createSession(env, user.id, request, provider);
  const headers = new Headers();
  headers.append('Set-Cookie', sessionCookie(sessionToken));
  headers.append('Set-Cookie', clearTempCookie(PKCE_COOKIE));
  headers.append('Set-Cookie', clearTempCookie(OAUTH_STATE_COOKIE));
  headers.set('Location', new URL(next, url.origin).toString());
  return new Response(null, { status: 302, headers });
}
