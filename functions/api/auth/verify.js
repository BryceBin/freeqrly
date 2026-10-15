// GET /api/auth/verify?token=... — consume a magic-link token.
// Valid → mark used, create session, set fq_session cookie, redirect /dashboard/.
// Invalid/expired/used → redirect /login/?error=invalid_link.
import { sha256Hex } from '../../_lib/dynamic.js';
import { createSession, sessionCookie, redirectTo } from '../../_lib/auth.js';

export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  const token = url.searchParams.get('token') || '';
  const loginErr = new URL('/login/?error=invalid_link', url.origin).toString();
  if (!token || !env.DB) return redirectTo(loginErr);
  const hash = await sha256Hex(token);
  const row = await env.DB.prepare(
    'SELECT user_id, expires_at, used FROM email_tokens WHERE token_hash = ? AND purpose = ?'
  ).bind(hash, 'magic_login').first();
  if (!row || row.used || row.expires_at <= Date.now()) return redirectTo(loginErr);

  await env.DB.prepare('UPDATE email_tokens SET used = 1 WHERE token_hash = ?').bind(hash).run();
  await env.DB.prepare('UPDATE users SET last_login_at = ? WHERE id = ?').bind(Date.now(), row.user_id).run();
  const sessionToken = await createSession(env, row.user_id, request);
  return redirectTo(new URL('/dashboard/', url.origin).toString(), {
    'Set-Cookie': sessionCookie(sessionToken),
  });
}
