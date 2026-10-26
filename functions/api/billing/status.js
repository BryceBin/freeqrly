// GET /api/billing/status — current plan, usage and live subscription.
// SESSION-ONLY. Prices are the published Pro prices (her 2026-10-22 decision).
import { json } from '../../_lib/dynamic.js';
import { getSessionUser, getCodeCount } from '../../_lib/auth.js';
import { getLiveSubscription, resolveCodeLimit, PRO_LIMIT } from '../../_lib/billing.js';
import { waffoConfigured } from '../../_lib/waffo.js';

export async function onRequestGet({ request, env }) {
  if (!env.DB) return json({ error: 'Not configured' }, 503);
  let sess = null;
  try { sess = await getSessionUser(env, request); } catch { sess = null; }
  if (!sess) return json({ error: 'unauthorized' }, 401);

  const sub = await getLiveSubscription(env, sess.user.id);
  const used = await getCodeCount(env, sess.user.id);
  return json({
    plan: sub ? 'pro' : (sess.user.plan || 'free'),
    billingEnabled: waffoConfigured(env),
    usage: { used, limit: resolveCodeLimit(sess.user, sub) },
    proLimit: PRO_LIMIT,
    prices: { monthly: 9, yearly: 90, currency: 'USD' },
    subscription: sub ? {
      status: sub.status,
      period: sub.period,
      currentPeriodEnd: sub.current_period_end,
      startedAt: sub.created_at,
    } : null,
  });
}
