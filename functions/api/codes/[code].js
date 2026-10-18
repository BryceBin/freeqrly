// PATCH /api/codes/:code — edit type + payload + style.
// DELETE /api/codes/:code — delete the code (frees one quota slot).
// Auth: login session cookie OR `Authorization: Bearer <api_token>`.
// Only the owning user; anonymous (user_id NULL) codes cannot be edited.
// Delete also removes the code's stats rows and its orphaned R2 logo.
import { json } from '../../_lib/dynamic.js';
import { getAuthUser } from '../../_lib/auth.js';
import { updateDynamicCode, deleteDynamicCode, ApiError } from '../../_lib/codes_api.js';

export async function onRequestPatch(context) {
  const { request, env, params } = context;
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);

  const sess = await getAuthUser(env, request);
  if (!sess) return json({ error: 'unauthorized' }, 401);

  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }

  try {
    const r = await updateDynamicCode(env, sess.user, params.code, {
      type: body.type,
      payload: body.payload,
      style: body.style,
    });
    return json({ ok: true, code: r.code, type: r.type, payload: r.payload });
  } catch (e) {
    if (e instanceof ApiError) return json(e.body, e.status);
    return json({ error: 'Failed to update code' }, 500);
  }
}

export async function onRequestDelete(context) {
  const { request, env, params } = context;
  if (!env.DB) return json({ error: 'Dynamic QR not configured yet' }, 503);

  const sess = await getAuthUser(env, request);
  if (!sess) return json({ error: 'unauthorized' }, 401);

  try {
    const r = await deleteDynamicCode(env, sess.user, params.code);
    return json({ ok: true, code: r.code });
  } catch (e) {
    if (e instanceof ApiError) return json(e.body, e.status);
    return json({ error: 'Failed to delete code' }, 500);
  }
}
