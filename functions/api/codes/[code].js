// PATCH /api/codes/:code — edit destination (requires editKey in body)
// GET  /api/codes/:code/stats — scan stats (requires editKey as ?key= query param)
import { sha256Hex, isValidDestination, json } from '../../_lib/dynamic.js';

export async function onRequestPatch(context) {
  const { request, env, params } = context;
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);
  const code = (params.code || '').trim();
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const { editKey, destination } = body;
  if (!editKey) return json({ error: 'editKey is required' }, 401);
  if (!destination || !isValidDestination(destination)) return json({ error: 'Invalid destination URL' }, 400);

  const row = await env.DB.prepare('SELECT edit_key_hash FROM codes WHERE code = ?').bind(code).first();
  if (!row) return json({ error: 'Code not found' }, 404);
  const hash = await sha256Hex(editKey);
  if (hash !== row.edit_key_hash) return json({ error: 'Invalid edit key' }, 403);

  await env.DB.prepare('UPDATE codes SET destination = ? WHERE code = ?').bind(destination, code).run();
  return json({ ok: true, code, destination });
}

export async function onRequestGet(context) {
  const { request, env, params } = context;
  const code = (params.code || '').trim();
  const url = new URL(request.url);
  const editKey = url.searchParams.get('key') || '';
  if (!editKey) return json({ error: 'editKey is required (as ?key=)' }, 401);

  const row = await env.DB.prepare('SELECT edit_key_hash, destination, total_scans, created_at FROM codes WHERE code = ?').bind(code).first();
  if (!row) return json({ error: 'Code not found' }, 404);
  const hash = await sha256Hex(editKey);
  if (hash !== row.edit_key_hash) return json({ error: 'Invalid edit key' }, 403);

  // By-date (last 30 days), by-country, by-device
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
    destination: row.destination,
    totalScans: row.total_scans,
    createdAt: row.created_at,
    byDate: byDate.results || [],
    byCountry: byCountry.results || [],
    byDevice: byDevice.results || [],
  });
}
