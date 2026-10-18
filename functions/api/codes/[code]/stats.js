// GET /api/codes/:code/stats — scan stats + current type/payload.
// Auth: login session cookie OR `Authorization: Bearer <api_token>`.
// Only the owning user.
import { json } from '../../../_lib/dynamic.js';
import { getAuthUser } from '../../../_lib/auth.js';
import { getCodeStats, ApiError } from '../../../_lib/codes_api.js';

export async function onRequestGet(context) {
  const { request, env, params } = context;
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);

  const sess = await getAuthUser(env, request);
  if (!sess) return json({ error: 'unauthorized' }, 401);

  try {
    return json(await getCodeStats(env, sess.user, params.code));
  } catch (e) {
    if (e instanceof ApiError) return json(e.body, e.status);
    return json({ error: 'Failed to load stats' }, 500);
  }
}
