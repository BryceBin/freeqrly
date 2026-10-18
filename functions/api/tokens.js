// API token management. SESSION-ONLY (a Bearer token can never manage tokens).
// POST /api/tokens — create a token. Body: { name: string }.
//   Returns { id, name, prefix, created_at, token } — `token` is shown ONCE.
//   Max 20 active tokens per user.
// GET /api/tokens — list tokens (metadata only, never the raw value).
import { json } from '../_lib/dynamic.js';
import { getSessionUser, createApiToken } from '../_lib/auth.js';

const MAX_TOKENS = 20;

export async function onRequestGet({ request, env }) {
  if (!env.DB) return json({ error: 'Not configured' }, 503);
  let sess = null;
  try { sess = await getSessionUser(env, request); } catch { sess = null; }
  if (!sess) return json({ error: 'unauthorized' }, 401);
  const rows = await env.DB.prepare(
    'SELECT id, name, prefix, created_at, last_used_at, revoked_at FROM api_tokens WHERE user_id = ? ORDER BY created_at DESC LIMIT 50'
  ).bind(sess.user.id).all();
  return json({ tokens: rows.results || [] });
}

export async function onRequestPost({ request, env }) {
  if (!env.DB) return json({ error: 'Not configured' }, 503);
  let sess = null;
  try { sess = await getSessionUser(env, request); } catch { sess = null; }
  if (!sess) return json({ error: 'unauthorized' }, 401);

  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const name = String(body.name || '').trim().slice(0, 60);
  if (!name) return json({ error: 'name is required' }, 400);

  const cnt = await env.DB.prepare(
    'SELECT COUNT(*) AS n FROM api_tokens WHERE user_id = ? AND revoked_at IS NULL'
  ).bind(sess.user.id).first();
  if (cnt && cnt.n >= MAX_TOKENS) return json({ error: 'token_limit_reached', max: MAX_TOKENS }, 403);

  const t = await createApiToken(env, sess.user.id, name);
  return json({ id: t.id, name, prefix: t.prefix, created_at: t.created_at, token: t.token });
}
