// DELETE /api/tokens/:id — revoke a token (soft revoke, keeps audit trail).
// SESSION-ONLY: the signed-in owner of the token.
import { json } from '../../_lib/dynamic.js';
import { getSessionUser } from '../../_lib/auth.js';

export async function onRequestDelete({ request, env, params }) {
  if (!env.DB) return json({ error: 'Not configured' }, 503);
  const id = (params.id || '').trim();
  if (!id) return json({ error: 'Invalid id' }, 400);

  let sess = null;
  try { sess = await getSessionUser(env, request); } catch { sess = null; }
  if (!sess) return json({ error: 'unauthorized' }, 401);

  const row = await env.DB.prepare('SELECT user_id, revoked_at FROM api_tokens WHERE id = ?').bind(id).first();
  if (!row) return json({ error: 'Token not found' }, 404);
  if (row.user_id !== sess.user.id) return json({ error: 'forbidden' }, 403);
  if (row.revoked_at) return json({ ok: true, id, already_revoked: true });

  await env.DB.prepare('UPDATE api_tokens SET revoked_at = ? WHERE id = ?').bind(Date.now(), id).run();
  return json({ ok: true, id });
}
