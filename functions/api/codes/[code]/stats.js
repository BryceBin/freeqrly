// GET /api/codes/:code/stats — scan stats + current type/payload (requires editKey as ?key=)
import { sha256Hex, json } from '../../../_lib/dynamic.js';

export async function onRequestGet(context) {
  const { request, env, params } = context;
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);
  const code = (params.code || '').trim();
  const url = new URL(request.url);
  const editKey = url.searchParams.get('key') || '';
  if (!editKey) return json({ error: 'editKey is required (as ?key=)' }, 401);

  const row = await env.DB.prepare('SELECT edit_key_hash, type, payload, destination, total_scans, created_at FROM codes WHERE code = ?').bind(code).first();
  if (!row) return json({ error: 'Code not found' }, 404);
  const hash = await sha256Hex(editKey);
  if (hash !== row.edit_key_hash) return json({ error: 'Invalid edit key' }, 403);

  const byDate = await env.DB.prepare(
    `SELECT date, SUM(count) AS scans FROM daily_stats WHERE code = ? GROUP BY date ORDER BY date DESC LIMIT 30`
  ).bind(code).all();
  const byCountry = await env.DB.prepare(
    `SELECT country, SUM(count) AS scans FROM daily_stats WHERE code = ? GROUP BY country ORDER BY scans DESC LIMIT 10`
  ).bind(code).all();
  const byDevice = await env.DB.prepare(
    `SELECT device, SUM(count) AS scans FROM daily_stats WHERE code = ? GROUP BY device ORDER BY scans DESC`
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
  });
}
