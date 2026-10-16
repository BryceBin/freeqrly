// PATCH /api/codes/:code — edit type + payload.
// SESSION-ONLY: the signed-in owner of the code. No EditKey channel —
// anonymous codes cannot be edited (there is no claim flow anymore).
import { json } from '../../_lib/dynamic.js';
import { getSessionUser } from '../../_lib/auth.js';

const VALID_TYPES = new Set(['url','text','wifi','vcard','email','sms','phone','geo','event','bitcoin','coupon','appstore']);

export async function onRequestPatch(context) {
  const { request, env, params } = context;
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);
  const code = (params.code || '').trim();
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const { type, payload } = body;
  if (!type || !VALID_TYPES.has(type)) return json({ error: 'Invalid type' }, 400);
  if (!payload || payload.length > 8000) return json({ error: 'Invalid payload' }, 400);
  if (type === 'url') {
    try {
      const u = new URL(payload);
      if (u.protocol !== 'http:' && u.protocol !== 'https:') return json({ error: 'Invalid URL' }, 400);
    } catch { return json({ error: 'Invalid URL' }, 400); }
  }

  let sess = null;
  try { sess = await getSessionUser(env, request); } catch { sess = null; }
  if (!sess) return json({ error: 'unauthorized' }, 401);
  const row = await env.DB.prepare('SELECT user_id FROM codes WHERE code = ?').bind(code).first();
  if (!row) return json({ error: 'Code not found' }, 404);
  if (row.user_id !== sess.user.id) return json({ error: 'forbidden' }, 403);

  await env.DB.prepare(
    'UPDATE codes SET type = ?, payload = ?, destination = ? WHERE code = ?'
  ).bind(type, payload, type === 'url' ? payload : '', code).run();
  return json({ ok: true, code, type, payload });
}
