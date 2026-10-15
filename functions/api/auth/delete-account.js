// POST /api/auth/delete-account — delete the account.
// Requires a session AND a fresh session (created within the last 15 min),
// else 403 { error: "reauth_required", hint: "request a fresh magic link" }.
// Deletes the user row + their session rows; their codes are RELEASED
// (codes.user_id = NULL), NOT deleted — EditKey still works. Clears the cookie.
import { json } from '../../_lib/dynamic.js';
import { getSessionUser, clearSessionCookie, REAUTH_WINDOW_MS, SESSION_COOKIE, getCookie, deleteSessionByToken } from '../../_lib/auth.js';

export async function onRequestPost({ request, env }) {
  if (!env.DB) return json({ error: 'Auth not configured yet' }, 503);
  const sess = await getSessionUser(env, request);
  if (!sess) return json({ error: 'unauthorized' }, 401);
  if (Date.now() - sess.session.created_at > REAUTH_WINDOW_MS) {
    return json({ error: 'reauth_required', hint: 'request a fresh magic link' }, 403);
  }
  const userId = sess.user.id;
  await env.DB.prepare('DELETE FROM sessions WHERE user_id = ?').bind(userId).run();
  await env.DB.prepare('UPDATE codes SET user_id = NULL WHERE user_id = ?').bind(userId).run();
  await env.DB.prepare('DELETE FROM email_tokens WHERE user_id = ?').bind(userId).run();
  await env.DB.prepare('DELETE FROM users WHERE id = ?').bind(userId).run();
  // Defensive: also drop this exact session token row if it somehow remains
  try { await deleteSessionByToken(env, getCookie(request, SESSION_COOKIE)); } catch { /* ignore */ }
  return new Response(JSON.stringify({ ok: true }), {
    status: 200,
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', 'Set-Cookie': clearSessionCookie() },
  });
}
