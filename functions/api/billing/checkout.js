// POST /api/billing/checkout — start a Waffo checkout for Pro.
// SESSION-ONLY. Body: { period: "monthly" | "yearly" }.
// Returns { checkoutUrl } — the client redirects the browser there.
// The user id rides in the checkout metadata and comes back as
// orderMetadata on every webhook, which is how billing.js links events.
import { json } from '../../_lib/dynamic.js';
import { getSessionUser } from '../../_lib/auth.js';
import { createCheckoutSession, waffoConfigured } from '../../_lib/waffo.js';
import { getLiveSubscription } from '../../_lib/billing.js';

export async function onRequestPost({ request, env }) {
  if (!env.DB) return json({ error: 'Not configured' }, 503);
  let sess = null;
  try { sess = await getSessionUser(env, request); } catch { sess = null; }
  if (!sess) return json({ error: 'unauthorized' }, 401);
  if (!waffoConfigured(env)) return json({ error: 'billing_not_configured' }, 503);

  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const period = body.period === 'yearly' ? 'yearly' : 'monthly';

  const existing = await getLiveSubscription(env, sess.user.id);
  if (existing) return json({ error: 'already_subscribed' }, 409);

  const origin = new URL(request.url).origin;
  try {
    const session = await createCheckoutSession(env, {
      period,
      buyerEmail: sess.user.email,
      userId: sess.user.id,
      successUrl: `${origin}/dashboard/?billing=success`,
    });
    return json({ checkoutUrl: session.checkoutUrl });
  } catch (e) {
    return json({ error: 'checkout_failed', detail: String(e.message || e).slice(0, 200) }, 502);
  }
}
