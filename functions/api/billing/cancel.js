// POST /api/billing/cancel — cancel the caller's Pro subscription at Waffo.
// Cancellation takes effect at period end (Waffo semantics): the local row
// flips to 'canceling' optimistically and the subscription.canceling
// webhook confirms it; Pro access continues until subscription.canceled.
import { json } from '../../_lib/dynamic.js';
import { getSessionUser } from '../../_lib/auth.js';
import { cancelSubscription } from '../../_lib/waffo.js';
import { getLiveSubscription } from '../../_lib/billing.js';

export async function onRequestPost({ request, env }) {
  if (!env.DB) return json({ error: 'Not configured' }, 503);
  let sess = null;
  try { sess = await getSessionUser(env, request); } catch { sess = null; }
  if (!sess) return json({ error: 'unauthorized' }, 401);

  const sub = await getLiveSubscription(env, sess.user.id);
  if (!sub) return json({ error: 'no_active_subscription' }, 404);
  if (sub.status === 'canceling') return json({ ok: true, status: 'canceling', currentPeriodEnd: sub.current_period_end });

  try {
    await cancelSubscription(env, sub.waffo_order_id);
  } catch (e) {
    return json({ error: 'cancel_failed', detail: String(e.message || e).slice(0, 200) }, 502);
  }
  await env.DB.prepare('UPDATE subscriptions SET status = ?, updated_at = ? WHERE id = ?')
    .bind('canceling', Date.now(), sub.id).run();
  return json({ ok: true, status: 'canceling', currentPeriodEnd: sub.current_period_end });
}
