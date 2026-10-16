// GET /api/codes/:code/stats — scan stats + current type/payload.
// SESSION-ONLY: the signed-in owner of the code. No EditKey channel.
import { json } from '../../../_lib/dynamic.js';
import { getSessionUser } from '../../../_lib/auth.js';

export async function onRequestGet(context) {
  const { request, env, params } = context;
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);
  const code = (params.code || '').trim();

  let sess = null;
  try { sess = await getSessionUser(env, request); } catch { sess = null; }
  if (!sess) return json({ error: 'unauthorized' }, 401);
  const row = await env.DB.prepare('SELECT user_id, type, payload, destination, total_scans, created_at FROM codes WHERE code = ?').bind(code).first();
  if (!row) return json({ error: 'Code not found' }, 404);
  if (row.user_id !== sess.user.id) return json({ error: 'forbidden' }, 403);

  const byDate = await env.DB.prepare(
    `SELECT date, SUM(count) AS scans FROM daily_stats WHERE code = ? GROUP BY date ORDER BY date DESC LIMIT 30`
  ).bind(code).all();
  const byCountry = await env.DB.prepare(
    `SELECT country, SUM(count) AS scans FROM daily_stats WHERE code = ? GROUP BY country ORDER BY scans DESC LIMIT 10`
  ).bind(code).all();
  const byDevice = await env.DB.prepare(
    `SELECT device, SUM(count) AS scans FROM daily_stats WHERE code = ? GROUP BY device ORDER BY scans DESC`
  ).bind(code).all();
  const byCity = await env.DB.prepare(
    `SELECT city, SUM(count) AS scans FROM daily_stats WHERE code = ? AND city != '' GROUP BY city ORDER BY scans DESC LIMIT 10`
  ).bind(code).all();
  const byOS = await env.DB.prepare(
    `SELECT os, SUM(count) AS scans FROM daily_stats WHERE code = ? GROUP BY os ORDER BY scans DESC`
  ).bind(code).all();
  const uniqueRow = await env.DB.prepare(
    `SELECT COUNT(DISTINCT fingerprint) AS n FROM scan_fingerprints WHERE code = ?`
  ).bind(code).first();
  const uniqueByDate = await env.DB.prepare(
    `SELECT date, COUNT(*) AS uniques FROM scan_fingerprints WHERE code = ? GROUP BY date ORDER BY date DESC LIMIT 30`
  ).bind(code).all();

  return json({
    code,
    type: row.type || 'url',
    payload: row.payload || row.destination || '',
    destination: row.destination || '',
    totalScans: row.total_scans,
    createdAt: row.created_at,
    byDate: byDate.results || [],
    byCountry: byCountry.results || [],
    byDevice: byDevice.results || [],
    byCity: byCity.results || [],
    byOS: byOS.results || [],
    uniqueScans: (uniqueRow && uniqueRow.n) || 0,
    uniqueByDate: uniqueByDate.results || [],
  });
}
