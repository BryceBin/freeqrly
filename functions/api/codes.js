// POST /api/codes — create a dynamic QR code.
// Auth: login session cookie OR `Authorization: Bearer <api_token>`.
// Body: { type: string, payload: string, style?: {...} }
// Returns: { code, shortUrl, type }. Quota: per-user code_limit (free: 8),
// else 403 { error: "quota_exceeded", hint: "upgrade" }.
import { json } from '../_lib/dynamic.js';
import { getAuthUser } from '../_lib/auth.js';
import { createDynamicCode, ApiError } from '../_lib/codes_api.js';

export async function onRequestPost(context) {
  const { request, env } = context;
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);

  const sess = await getAuthUser(env, request);
  if (!sess) return json({ error: 'unauthorized' }, 401);

  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }

  try {
    const r = await createDynamicCode(env, sess.user, {
      type: body.type,
      payload: body.payload,
      style: body.style,
    }, {
      origin: new URL(request.url).origin,
      ip: request.headers.get('CF-Connecting-IP') || 'unknown',
    });
    return json({ code: r.code, shortUrl: r.shortUrl });
  } catch (e) {
    if (e instanceof ApiError) return json(e.body, e.status);
    return json({ error: 'Failed to create code' }, 500);
  }
}
