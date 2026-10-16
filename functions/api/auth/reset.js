// POST /api/auth/reset — consume a password-reset token and set a new password.
// Body: { token, newPassword }
// - Token: SHA-256 hash lookup, purpose=reset, not used, not expired — else
//   invalid_link. Single-use: marked used before the password is changed.
// - newPassword must be ≥ 8 chars (else weak_password).
// - On success: new password_hash stored, token marked used, ALL existing
//   sessions for the user are DELETED (force re-login everywhere).
// Returns { ok: true }.
import { json, sha256Hex } from '../../_lib/dynamic.js';
import { hashPassword, MIN_PASSWORD_LEN } from '../../_lib/auth.js';

export async function onRequestPost({ request, env }) {
  if (!env.DB) return json({ error: 'Auth not configured yet' }, 503);
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const token = String(body.token || '');
  const newPassword = String(body.newPassword || '');
  if (!token) return json({ error: 'invalid_link' }, 400);

  const hash = await sha256Hex(token);
  const row = await env.DB.prepare(
    'SELECT user_id, expires_at, used FROM email_tokens WHERE token_hash = ? AND purpose = ?'
  ).bind(hash, 'reset').first();
  if (!row || row.used || row.expires_at <= Date.now()) return json({ error: 'invalid_link' }, 400);

  if (!newPassword || newPassword.length < MIN_PASSWORD_LEN) return json({ error: 'weak_password' }, 400);

  const passwordHash = await hashPassword(newPassword);
  // Single-use first, then rotate the credential and kill every session.
  await env.DB.prepare('UPDATE email_tokens SET used = 1 WHERE token_hash = ?').bind(hash).run();
  await env.DB.prepare('UPDATE users SET password_hash = ? WHERE id = ?').bind(passwordHash, row.user_id).run();
  await env.DB.prepare('DELETE FROM sessions WHERE user_id = ?').bind(row.user_id).run();
  return json({ ok: true });
}
