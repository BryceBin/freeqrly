// GET /q/:code — dynamic QR redirect
// Looks up destination in D1, 302-redirects, logs scan stats async (fail-open)
import { deviceFromUA } from '../_lib/dynamic.js';

export async function onRequest(context) {
  const { request, env, params, ctx } = context;
  if (!env.DB) return new Response('Dynamic QR not configured yet', { status: 503 });
  const code = (params.code || '').trim();

  if (!code || code.length > 16) {
    return new Response('Not found', { status: 404 });
  }

  let row;
  try {
    row = await env.DB.prepare('SELECT destination FROM codes WHERE code = ?').bind(code).first();
  } catch (e) {
    return new Response('Service temporarily unavailable', { status: 503 });
  }

  if (!row) {
    return new Response('Not found', { status: 404 });
  }

  // Fire-and-forget analytics: never block the redirect on stats
  ctx.waitUntil((async () => {
    try {
      // Skip bots — they don't count as real scans
      const ua = request.headers.get('User-Agent') || '';
      if (request.cf && request.cf.client_bot) return;
      const country = (request.cf && request.cf.country) || 'XX';
      const device = deviceFromUA(ua);
      const date = new Date().toISOString().slice(0, 10);
      await env.DB.prepare(
        `INSERT INTO daily_stats (code, date, country, device, count) VALUES (?, ?, ?, ?, 1)
         ON CONFLICT(code, date, country, device) DO UPDATE SET count = count + 1`
      ).bind(code, date, country, device).run();
      await env.DB.prepare('UPDATE codes SET total_scans = total_scans + 1 WHERE code = ?').bind(code).run();
    } catch { /* analytics failure must never break the redirect */ }
  })());

  return Response.redirect(row.destination, 302);
}
