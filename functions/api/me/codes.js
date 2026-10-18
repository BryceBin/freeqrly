// GET /api/me/codes — the user's codes (newest first, max 100).
// Auth: login session cookie OR `Authorization: Bearer <api_token>`.
// { codes: [{ code, type, destination, payload, style, totalScans, created_at }], quota: { used, limit } }
import { json } from '../../_lib/dynamic.js';
import { getAuthUser } from '../../_lib/auth.js';
import { listDynamicCodes, ApiError } from '../../_lib/codes_api.js';

export async function onRequestGet({ request, env }) {
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);
  const sess = await getAuthUser(env, request);
  if (!sess) return json({ error: 'unauthorized' }, 401);
  try {
    return json(await listDynamicCodes(env, sess.user));
  } catch (e) {
    if (e instanceof ApiError) return json(e.body, e.status);
    return json({ error: 'Failed to load codes' }, 500);
  }
}
