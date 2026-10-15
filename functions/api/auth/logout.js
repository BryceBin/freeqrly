// POST /api/auth/logout — delete the session row, clear the cookie. 200 { ok: true }.
import { getCookie, deleteSessionByToken, clearSessionCookie, SESSION_COOKIE } from '../../_lib/auth.js';

export async function onRequestPost({ request, env }) {
  if (env.DB) {
    try { await deleteSessionByToken(env, getCookie(request, SESSION_COOKIE)); } catch { /* ignore */ }
  }
  return new Response(JSON.stringify({ ok: true }), {
    status: 200,
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', 'Set-Cookie': clearSessionCookie() },
  });
}
