// Pro tier state: D1 `subscriptions` rows driven by Waffo webhooks.
// users.plan mirrors liveness ('pro' while a subscription is active /
// canceling / past_due). Quota rule (her policy): Pro = 100 dynamic codes,
// but billing must never *lower* a limit — during the unlimited promo
// (code_limit >= UNLIMITED_LIMIT) everyone keeps the promo limit.
// Mirrors UNLIMITED_LIMIT in codes_api.js (kept local to avoid an import cycle).
const UNLIMITED_LIMIT = 999999;

export const PRO_LIMIT = 100;
const LIVE_STATUSES = new Set(['active', 'canceling', 'past_due']);

export async function getLiveSubscription(env, userId) {
  const row = await env.DB.prepare(
    `SELECT * FROM subscriptions WHERE user_id = ? AND status IN ('active','canceling','past_due')
     ORDER BY created_at DESC LIMIT 1`
  ).bind(userId).first();
  return row || null;
}

export function resolveCodeLimit(user, sub) {
  const base = user.code_limit ?? 8;
  if (sub && LIVE_STATUSES.has(sub.status)) {
    if (base >= UNLIMITED_LIMIT) return UNLIMITED_LIMIT;
    return Math.max(PRO_LIMIT, base);
  }
  return base;
}

async function syncUserPlan(env, userId) {
  const sub = await getLiveSubscription(env, userId);
  await env.DB.prepare('UPDATE users SET plan = ? WHERE id = ?')
    .bind(sub ? 'pro' : 'free', userId).run();
  return sub;
}

async function upsertSubscription(env, { userId, orderId, buyerEmail, period, status, periodEnd }) {
  const now = Date.now();
  const existing = await env.DB.prepare('SELECT id FROM subscriptions WHERE waffo_order_id = ?')
    .bind(orderId).first();
  if (existing) {
    await env.DB.prepare(
      `UPDATE subscriptions SET status = ?, current_period_end = COALESCE(?, current_period_end),
       buyer_email = COALESCE(?, buyer_email), period = COALESCE(?, period), updated_at = ? WHERE id = ?`
    ).bind(status, periodEnd || null, buyerEmail || null, period || null, now, existing.id).run();
  } else {
    await env.DB.prepare(
      `INSERT INTO subscriptions (id, user_id, provider, waffo_order_id, buyer_email, period, status, current_period_end, created_at, updated_at)
       VALUES (?, ?, 'waffo', ?, ?, ?, ?, ?, ?, ?)`
    ).bind(`sub_${orderId}`, userId, orderId, buyerEmail || null, period || null, status, periodEnd || null, now, now).run();
  }
}

// Apply one verified Waffo webhook event. Returns true when the event was
// new and processed, false when it was a duplicate delivery.
// User linkage: checkout metadata { userId } echoes back as orderMetadata;
// orderMerchantExternalId carries the same id as a fallback. Events whose
// order we already know resolve through the stored row instead.
export async function applyWaffoEvent(env, evt) {
  const key = `${evt.eventType}:${evt.eventId}`;
  const seen = await env.DB.prepare('SELECT event_key FROM webhook_events WHERE event_key = ?').bind(key).first();
  if (seen) return false;
  await env.DB.prepare('INSERT INTO webhook_events (event_key, received_at) VALUES (?, ?)').bind(key, Date.now()).run();

  const d = evt.data || {};
  const orderId = d.orderId;
  if (!orderId) return true;

  let userId = (d.orderMetadata && d.orderMetadata.userId) || d.orderMerchantExternalId || null;
  if (!userId) {
    const row = await env.DB.prepare('SELECT user_id FROM subscriptions WHERE waffo_order_id = ?').bind(orderId).first();
    if (row) userId = row.user_id;
  }
  if (!userId) return true; // not one of ours (e.g. dashboard test event) — recorded, nothing to apply

  const period = (d.orderMetadata && d.orderMetadata.period) || d.billingPeriod || null;
  const periodEnd = d.currentPeriodEnd || null;
  const base = { userId, orderId, buyerEmail: d.buyerEmail || null, period, periodEnd };

  switch (evt.eventType) {
    case 'subscription.activated':
      await upsertSubscription(env, { ...base, status: 'active' });
      break;
    case 'subscription.renewed':
    case 'subscription.recovered':
      await upsertSubscription(env, { ...base, status: 'active' });
      break;
    case 'subscription.canceling':
      await upsertSubscription(env, { ...base, status: 'canceling' });
      break;
    case 'subscription.uncanceled':
      await upsertSubscription(env, { ...base, status: 'active' });
      break;
    case 'subscription.past_due':
      await upsertSubscription(env, { ...base, status: 'past_due' });
      break;
    case 'subscription.canceled':
      await upsertSubscription(env, { ...base, status: 'canceled', periodEnd: null });
      break;
    default:
      // payment_succeeded / refunds / plan changes: recorded above; plan
      // state moves only on the subscription lifecycle events.
      return true;
  }
  await syncUserPlan(env, userId);
  return true;
}
