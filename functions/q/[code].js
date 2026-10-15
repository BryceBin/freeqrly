// GET /q/:code — dynamic QR redirect / hosted page
// URL type → 302 redirect. Other types → hosted page rendering the content.
import { deviceFromUA } from '../_lib/dynamic.js';
import { renderHostedPage } from '../_lib/hosted.js';

export async function onRequest(context) {
  const { request, env, params } = context;
  if (!env.DB) return new Response('Dynamic QR not configured yet', { status: 503 });
  const code = (params.code || '').trim();
  if (!code || code.length > 16) {
    return new Response('Not found', { status: 404 });
  }
  let row;
  try {
    row = await env.DB.prepare('SELECT type, payload, destination FROM codes WHERE code = ?').bind(code).first();
  } catch (e) {
    return new Response('Service temporarily unavailable', { status: 503 });
  }
  if (!row) {
    return new Response('Not found', { status: 404 });
  }
  // Fire-and-forget analytics (fail-open, never blocks response)
  try {
    const ua = request.headers.get('User-Agent') || '';
    const isBot = request.cf && request.cf.client_bot;
    if (!isBot && context.waitUntil) {
      const country = (request.cf && request.cf.country) || 'XX';
      const device = deviceFromUA(ua);
      const date = new Date().toISOString().slice(0, 10);
      const p = (async () => {
        try {
          await env.DB.prepare(
            `INSERT INTO daily_stats (code, date, country, device, count) VALUES (?, ?, ?, ?, 1)
             ON CONFLICT(code, date, country, device) DO UPDATE SET count = count + 1`
          ).bind(code, date, country, device).run();
          await env.DB.prepare('UPDATE codes SET total_scans = total_scans + 1 WHERE code = ?').bind(code).run();
        } catch (err) { /* ignore */ }
      })();
      context.waitUntil(p);
    }
  } catch (err) { /* ignore */ }

  const type = row.type || 'url';
  const payload = row.payload || row.destination || '';
  if (type === 'url' && payload) {
    return Response.redirect(payload, 302);
  }
  // Non-URL types: serve hosted page
  return new Response(renderHostedPage(type, payload), {
    headers: { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex, nofollow' },
  });
}
