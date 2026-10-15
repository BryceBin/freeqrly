// GET /api/auth/export — download the user's own data as JSON.
// Requires session. Content-Disposition: attachment; filename="freeqrly-export.json".
import { getSessionUser } from '../../_lib/auth.js';
import { json } from '../../_lib/dynamic.js';

export async function onRequestGet({ request, env }) {
  const sess = await getSessionUser(env, request);
  if (!sess) return json({ error: 'unauthorized' }, 401);
  const rows = await env.DB.prepare(
    'SELECT code, type, destination, payload, total_scans, created_at FROM codes WHERE user_id = ? ORDER BY created_at DESC'
  ).bind(sess.user.id).all();
  const userRow = await env.DB.prepare('SELECT email, created_at, plan FROM users WHERE id = ?').bind(sess.user.id).first();
  const data = {
    user: { email: userRow.email, created_at: userRow.created_at, plan: userRow.plan },
    codes: (rows.results || []).map((r) => ({
      code: r.code, type: r.type, destination: r.destination,
      totalScans: r.total_scans, created_at: r.created_at,
    })),
    exported_at: Date.now(),
  };
  return new Response(JSON.stringify(data, null, 2), {
    status: 200,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'no-store',
      'Content-Disposition': 'attachment; filename="freeqrly-export.json"',
    },
  });
}
