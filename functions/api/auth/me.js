// GET /api/auth/me — current session user + quota.
// 200 { user: { id, email, name, avatar_url, plan, codeLimit, codeCount, authMethod } }
// authMethod: how THIS session signed in ('password' | 'email' | 'google' |
// 'github'); falls back to the account's auth_provider for sessions created
// before auth_method existed.
// 401 { error: "unauthorized" }
import { json } from '../../_lib/dynamic.js';
import { getSessionUser, getCodeCount } from '../../_lib/auth.js';

export async function onRequestGet({ request, env }) {
  const sess = await getSessionUser(env, request);
  if (!sess) return json({ error: 'unauthorized' }, 401);
  const codeCount = await getCodeCount(env, sess.user.id);
  return json({
    user: {
      id: sess.user.id,
      email: sess.user.email,
      name: sess.user.name,
      avatar_url: sess.user.avatar_url,
      plan: sess.user.plan,
      codeLimit: sess.user.code_limit,
      codeCount,
      authMethod: sess.session.auth_method || sess.user.auth_provider || 'email',
    },
  });
}
