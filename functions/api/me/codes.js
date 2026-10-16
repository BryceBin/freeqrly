// GET /api/me/codes — the signed-in user's codes (newest first, max 100).
// 401 without a session. { codes: [{ code, type, destination, payload, style, totalScans, created_at }], quota: { used, limit } }
// destination: stored destination (URL codes); for other types the payload, truncated to 120 chars.
// style: the saved QR style (colors/dots/frame/logo) or null when the code predates style saving.
import { json } from '../../_lib/dynamic.js';
import { getSessionUser, getCodeCount } from '../../_lib/auth.js';
import { parseStyle } from '../../_lib/style.js';

export async function onRequestGet({ request, env }) {
  const sess = await getSessionUser(env, request);
  if (!sess) return json({ error: 'unauthorized' }, 401);
  const rows = await env.DB.prepare(
    'SELECT code, type, destination, payload, style, total_scans, created_at FROM codes WHERE user_id = ? ORDER BY created_at DESC LIMIT 100'
  ).bind(sess.user.id).all();
  const used = await getCodeCount(env, sess.user.id);
  return json({
    codes: (rows.results || []).map((r) => ({
      code: r.code,
      type: r.type || 'url',
      destination: String(r.destination || r.payload || '').slice(0, 120),
      payload: r.payload || '',
      style: parseStyle(r.style),
      totalScans: r.total_scans || 0,
      created_at: r.created_at,
    })),
    quota: { used, limit: sess.user.code_limit },
  });
}
