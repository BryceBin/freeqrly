// PATCH /api/codes/:code — edit type + payload + style.
// DELETE /api/codes/:code — delete the code (frees one quota slot).
// SESSION-ONLY: the signed-in owner of the code. No EditKey channel —
// anonymous codes cannot be edited (there is no claim flow anymore).
// Delete also removes the code's stats rows. A custom uploaded logo in R2
// is deleted too, but only when no other code of this user references it.
import { json } from '../../_lib/dynamic.js';
import { getSessionUser } from '../../_lib/auth.js';
import { sanitizeStyle, parseStyle } from '../../_lib/style.js';

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

  // Optional style update (same validation as create). Absent = keep current.
  let styleSql = '', styleVal = null;
  if (body.style !== undefined) {
    let style = null;
    try {
      style = sanitizeStyle(body.style, sess.user.id);
    } catch { return json({ error: 'Invalid style' }, 400); }
    styleSql = ', style = ?';
    styleVal = style ? JSON.stringify(style) : null;
  }

  await env.DB.prepare(
    `UPDATE codes SET type = ?, payload = ?, destination = ?${styleSql} WHERE code = ?`
  ).bind(type, payload, type === 'url' ? payload : '', ...(styleSql ? [styleVal] : []), code).run();
  return json({ ok: true, code, type, payload });
}

export async function onRequestDelete(context) {
  const { request, env, params } = context;
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);
  const code = (params.code || '').trim();

  let sess = null;
  try { sess = await getSessionUser(env, request); } catch { sess = null; }
  if (!sess) return json({ error: 'unauthorized' }, 401);
  const row = await env.DB.prepare('SELECT user_id, style FROM codes WHERE code = ?').bind(code).first();
  if (!row) return json({ error: 'Code not found' }, 404);
  if (row.user_id !== sess.user.id) return json({ error: 'forbidden' }, 403);

  const style = parseStyle(row.style);
  const logoKey = style && style.logoKey ? style.logoKey : null;

  await env.DB.batch([
    env.DB.prepare('DELETE FROM codes WHERE code = ?').bind(code),
    env.DB.prepare('DELETE FROM daily_stats WHERE code = ?').bind(code),
    env.DB.prepare('DELETE FROM scan_fingerprints WHERE code = ?').bind(code),
  ]);

  // Best-effort R2 cleanup: only delete the uploaded logo when no other
  // code of this user still references it.
  if (logoKey && env.LOGOS) {
    try {
      const others = await env.DB.prepare(
        'SELECT COUNT(*) AS n FROM codes WHERE user_id = ? AND style LIKE ?'
      ).bind(sess.user.id, `%${logoKey}%`).first();
      if (!others || others.n === 0) await env.LOGOS.delete(logoKey);
    } catch { /* orphaned logo is harmless */ }
  }
  return json({ ok: true, code });
}
