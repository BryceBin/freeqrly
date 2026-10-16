// GET /api/auth/verify?token=...&next=... — consume a one-time email token.
// Only purpose: 'verify' (email-verification link from registration, 24 h).
// Sets email_verified=1, marks the token used, creates a session.
// Success → redirect /login/?verified=1&next=<validated next or /dashboard/>
// (the frontend shows the verified state, then continues to `next`).
// Invalid/expired/used → redirect /login/?error=invalid_link.
import { sha256Hex } from '../../_lib/dynamic.js';
import { createSession, sessionCookie, redirectTo, validateNext, loginVerifiedUrl } from '../../_lib/auth.js';

export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  const token = url.searchParams.get('token') || '';
  const next = validateNext(url.searchParams.get('next') || '');
  const loginErr = new URL('/login/?error=invalid_link', url.origin).toString();
  if (!token || !env.DB) return redirectTo(loginErr);
  const hash = await sha256Hex(token);
  const row = await env.DB.prepare(
    'SELECT user_id, purpose, expires_at, used FROM email_tokens WHERE token_hash = ?'
  ).bind(hash).first();
  if (!row || row.used || row.expires_at <= Date.now()) return redirectTo(loginErr);
  if (row.purpose !== 'verify') return redirectTo(loginErr);

  await env.DB.prepare('UPDATE email_tokens SET used = 1 WHERE token_hash = ?').bind(hash).run();
  await env.DB.prepare('UPDATE users SET email_verified = 1, last_login_at = ? WHERE id = ?').bind(Date.now(), row.user_id).run();
  const sessionToken = await createSession(env, row.user_id, request);
  return redirectTo(loginVerifiedUrl(url.origin, next), {
    'Set-Cookie': sessionCookie(sessionToken),
  });
}
