// POST /api/codes — create a dynamic QR code
// Body: { destination: string }
// Returns: { code, shortUrl, editKey }
import { genCode, genEditKey, sha256Hex, isValidDestination, json } from '../_lib/dynamic.js';

export async function onRequestPost(context) {
  const { request, env } = context;

  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const destination = (body.destination || '').trim();
  if (!destination) return json({ error: 'destination is required' }, 400);
  if (!isValidDestination(destination)) return json({ error: 'Invalid destination URL' }, 400);

  // Per-IP creation rate limit: ~10 codes/hour (best-effort, D1-backed)
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
  } catch { /* rate limit failure is non-fatal — continue */ }

  // Generate unique code (retry on collision)
  let code = null;
  for (let attempt = 0; attempt < 5; attempt++) {
    const candidate = genCode(7);
    try {
      const editKey = genEditKey();
      const editKeyHash = await sha256Hex(editKey);
      await env.DB.prepare(
        'INSERT INTO codes (code, destination, edit_key_hash, created_at, total_scans) VALUES (?, ?, ?, ?, 0)'
      ).bind(candidate, destination, editKeyHash, Date.now()).run();
      code = candidate;
      return json({ code, shortUrl: `${new URL(request.url).origin}/q/${code}`, editKey });
    } catch (e) {
      // UNIQUE constraint violation → collision, retry with a new code
      if (String(e.message || e).includes('UNIQUE')) continue;
      return json({ error: 'Failed to create code' }, 500);
    }
  }
  return json({ error: 'Failed to generate unique code' }, 500);
}
