// POST /api/billing/webhook — Waffo Pancake event receiver.
// No session: authenticity comes from the RSA-SHA256 signature, verified
// against Waffo's platform public key for the payload's mode (test/prod).
// Always 200 on verified events (duplicates included) so Waffo stops
// retrying; 401 on bad signatures; processing is idempotent via
// webhook_events (see billing.js applyWaffoEvent).
import { json } from '../../_lib/dynamic.js';
import { verifyWebhook } from '../../_lib/waffo.js';
import { applyWaffoEvent } from '../../_lib/billing.js';

export async function onRequestPost({ request, env }) {
  if (!env.DB) return json({ error: 'Not configured' }, 503);
  const raw = await request.text();
  const evt = await verifyWebhook(raw, request.headers.get('X-Waffo-Signature'));
  if (!evt) return json({ error: 'invalid_signature' }, 401);
  try {
    await applyWaffoEvent(env, evt);
  } catch (e) {
    // Return 500 so Waffo retries — the event row write is idempotent, and
    // a transient D1 failure should not silently drop a lifecycle event.
    return json({ error: 'processing_failed' }, 500);
  }
  return json({ ok: true });
}
