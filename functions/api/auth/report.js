// POST /api/auth/report — report an abusive dynamic QR code.
// Body: { code, reason, reporter_email? }. No auth. Inserts into abuse_reports.
// No admin UI (Phase 2). Rate limited: 10/hr per IP.
import { json } from '../../_lib/dynamic.js';
import { getClientIp, checkRateLimit } from '../../_lib/auth.js';

export async function onRequestPost({ request, env }) {
  if (!env.DB) return json({ error: 'Auth not configured yet' }, 503);
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const code = String(body.code || '').trim();
  if (!code || code.length > 16) return json({ error: 'code is required' }, 400);
  if (!(await checkRateLimit(env, 'report:ip:' + getClientIp(request), 10))) {
    return json({ error: 'rate_limited' }, 429);
  }
  const reason = String(body.reason || '').trim().slice(0, 500);
  const reporterEmail = String(body.reporter_email || '').trim().slice(0, 254);
  await env.DB.prepare(
    'INSERT INTO abuse_reports (code, reason, reporter_email, created_at) VALUES (?, ?, ?, ?)'
  ).bind(code, reason || null, reporterEmail || null, Date.now()).run();
  return json({ ok: true });
}
