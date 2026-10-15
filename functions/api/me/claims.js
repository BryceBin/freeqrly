// POST /api/me/claims — claim an anonymous code into the signed-in account.
// Body: { code, editKey }. Requires session. Verifies the editKey hash (same
// check as the PATCH handler), then enforces the per-plan quota.
// 404 unknown code · 409 { error: "already_claimed" } · 403 { error: "invalid_key" }
// 403 { error: "quota_exceeded", hint: "upgrade" } · 200 { ok: true, code }
import { sha256Hex, json } from '../../_lib/dynamic.js';
import { getSessionUser, getCodeCount } from '../../_lib/auth.js';

export async function onRequestPost({ request, env }) {
  if (!env.DB) return json({ error: 'Auth not configured yet' }, 503);
  const sess = await getSessionUser(env, request);
  if (!sess) return json({ error: 'unauthorized' }, 401);
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const code = String(body.code || '').trim();
  const editKey = body.editKey || '';
  if (!code || !editKey) return json({ error: 'code and editKey are required' }, 400);

  const row = await env.DB.prepare('SELECT user_id, edit_key_hash FROM codes WHERE code = ?').bind(code).first();
  if (!row) return json({ error: 'Code not found' }, 404);
  if (row.user_id && row.user_id === sess.user.id) return json({ ok: true, code }); // already mine
  if (row.user_id) return json({ error: 'already_claimed' }, 409);
  const hash = await sha256Hex(editKey);
  if (hash !== row.edit_key_hash) return json({ error: 'invalid_key' }, 403);

  const used = await getCodeCount(env, sess.user.id);
  if (used >= sess.user.code_limit) return json({ error: 'quota_exceeded', hint: 'upgrade' }, 403);
  await env.DB.prepare('UPDATE codes SET user_id = ? WHERE code = ?').bind(sess.user.id, code).run();
  return json({ ok: true, code });
}
