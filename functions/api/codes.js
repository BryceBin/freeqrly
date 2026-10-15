// POST /api/codes — create a dynamic QR code
// Body: { type: string, payload: string }
// Returns: { code, shortUrl, editKey }
import { genCode, genEditKey, sha256Hex, json } from '../_lib/dynamic.js';

const VALID_TYPES = new Set(['url','text','wifi','vcard','email','sms','phone','geo','event','bitcoin','coupon','appstore']);

export async function onRequestPost(context) {
  const { request, env } = context;
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);

  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const type = (body.type || 'url').trim();
  const payload = (body.payload || '').trim();
  if (!payload) return json({ error: 'payload is required' }, 400);
  if (!VALID_TYPES.has(type)) return json({ error: 'Invalid type' }, 400);
  if (payload.length > 8000) return json({ error: 'Payload too large' }, 400);
  // URL type must be a valid http(s) URL
  if (type === 'url') {
    try {
      const u = new URL(payload);
      if (u.protocol !== 'http:' && u.protocol !== 'https:') return json({ error: 'Invalid URL' }, 400);
    } catch { return json({ error: 'Invalid URL' }, 400); }
  }

  // Per-IP creation rate limit: ~10 codes/hour
  const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
  const hour = new Date().toISOString().slice(0, 13);
  try {
    const cnt = await env.DB.prepare(
      'SELECT count FROM create_limits WHERE ip = ? AND hour = ?'
    ).bind(ip, hour).first();
    if (cnt && cnt.count >= 10) return json({ error: 'Rate limit: too many codes created' }, 429);
    await env.DB.prepare(
      `INSERT INTO create_limits (ip, hour, count) VALUES (?, ?, 1)
       ON CONFLICT(ip, hour) DO UPDATE SET count = count + 1`
    ).bind(ip, hour).run();
  } catch { /* rate limit failure is non-fatal */ }

  // Generate unique code (retry on collision)
  for (let attempt = 0; attempt < 5; attempt++) {
    const candidate = genCode(7);
    try {
      const editKey = genEditKey();
      const editKeyHash = await sha256Hex(editKey);
      await env.DB.prepare(
        'INSERT INTO codes (code, destination, type, payload, edit_key_hash, created_at, total_scans) VALUES (?, ?, ?, ?, ?, ?, 0)'
      ).bind(candidate, type === 'url' ? payload : '', type, payload, editKeyHash, Date.now()).run();
      return json({ code: candidate, shortUrl: `${new URL(request.url).origin}/q/${candidate}`, editKey });
    } catch (e) {
      if (String(e.message || e).includes('UNIQUE')) continue;
      return json({ error: 'Failed to create code' }, 500);
    }
  }
  return json({ error: 'Failed to generate unique code' }, 500);
}
