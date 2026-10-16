// POST /api/codes — create a dynamic QR code. LOGIN REQUIRED.
// Body: { type: string, payload: string }
// Returns: { code, shortUrl } — NEVER an editKey (new codes are session-owned;
// edit_key_hash is NULL). Quota: COUNT codes WHERE user_id=? < code_limit,
// else 403 { error: "quota_exceeded", hint: "upgrade" }.
// Grandfathered anonymous codes (edit_key_hash NOT NULL) keep working via
// the dual-channel PATCH/stats handlers; they are unaffected by this endpoint.
import { genCode, json } from '../_lib/dynamic.js';
import { getSessionUser, getCodeCount } from '../_lib/auth.js';

const VALID_TYPES = new Set(['url','text','wifi','vcard','email','sms','phone','geo','event','bitcoin','coupon','appstore']);

export async function onRequestPost(context) {
  const { request, env } = context;
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);

  // Login required: anonymous creation is rejected.
  let sess;
  try {
    sess = await getSessionUser(env, request);
  } catch { sess = null; }
  if (!sess) return json({ error: 'unauthorized' }, 401);

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

  // Per-plan quota for the signed-in owner.
  const used = await getCodeCount(env, sess.user.id);
  if (used >= sess.user.code_limit) return json({ error: 'quota_exceeded', hint: 'upgrade' }, 403);

  // Per-IP creation rate limit: ~10 codes/hour (unchanged abuse guard)
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

  // Generate unique code (retry on collision). Session-owned: user_id set,
  // edit_key_hash NULL — no EditKey is ever generated or returned.
  for (let attempt = 0; attempt < 5; attempt++) {
    const candidate = genCode(7);
    try {
      await env.DB.prepare(
        'INSERT INTO codes (code, destination, type, payload, edit_key_hash, created_at, total_scans, user_id) VALUES (?, ?, ?, ?, NULL, ?, 0, ?)'
      ).bind(candidate, type === 'url' ? payload : '', type, payload, Date.now(), sess.user.id).run();
      return json({ code: candidate, shortUrl: `${new URL(request.url).origin}/q/${candidate}` });
    } catch (e) {
      if (String(e.message || e).includes('UNIQUE')) continue;
      return json({ error: 'Failed to create code' }, 500);
    }
  }
  return json({ error: 'Failed to generate unique code' }, 500);
}
