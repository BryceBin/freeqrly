// PATCH /api/codes/:code — edit type + payload (requires editKey in body)
// Body: { editKey, type, payload }
import { sha256Hex, json } from '../../_lib/dynamic.js';

const VALID_TYPES = new Set(['url','text','wifi','vcard','email','sms','phone','geo','event','bitcoin','coupon','appstore']);

export async function onRequestPatch(context) {
  const { request, env, params } = context;
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);
  const code = (params.code || '').trim();
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const { editKey, type, payload } = body;
  if (!editKey) return json({ error: 'editKey is required' }, 401);
  if (!type || !VALID_TYPES.has(type)) return json({ error: 'Invalid type' }, 400);
  if (!payload || payload.length > 8000) return json({ error: 'Invalid payload' }, 400);
  if (type === 'url') {
    try {
      const u = new URL(payload);
      if (u.protocol !== 'http:' && u.protocol !== 'https:') return json({ error: 'Invalid URL' }, 400);
    } catch { return json({ error: 'Invalid URL' }, 400); }
  }

  const row = await env.DB.prepare('SELECT edit_key_hash FROM codes WHERE code = ?').bind(code).first();
  if (!row) return json({ error: 'Code not found' }, 404);
  const hash = await sha256Hex(editKey);
  if (hash !== row.edit_key_hash) return json({ error: 'Invalid edit key' }, 403);

  await env.DB.prepare(
    'UPDATE codes SET type = ?, payload = ?, destination = ? WHERE code = ?'
  ).bind(type, payload, type === 'url' ? payload : '', code).run();
  return json({ ok: true, code, type, payload });
}
