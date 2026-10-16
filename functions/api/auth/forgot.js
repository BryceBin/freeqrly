// POST /api/auth/forgot — request a password-reset email.
// Body: { email, next?, turnstileToken? }
// ALWAYS { ok: true } regardless of whether the email exists (no enumeration).
// Only if the user exists AND has a password_hash (i.e. a password account):
// create a single-use reset token (purpose=reset, 1 h expiry, SHA-256 hash
// only) and send a reset email with a link to /reset/?token=...
// (plus validated `next` when provided). Per-IP / per-email sends are
// silently capped — the response stays { ok: true } either way.
import { json, sha256Hex } from '../../_lib/dynamic.js';
import {
  appUrl, getClientIp, verifyTurnstile, checkRateLimit, getUserByEmail,
  createEmailToken, sendResendEmail, validateNext, EMAIL_RE, RESET_TOKEN_TTL_MS,
} from '../../_lib/auth.js';

export async function onRequestPost({ request, env }) {
  if (!env.DB) return json({ error: 'Auth not configured yet' }, 503);
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const email = String(body.email || '').trim().toLowerCase();
  const next = validateNext(body.next);
  if (!email || email.length > 254 || !EMAIL_RE.test(email)) return json({ error: 'Invalid email' }, 400);

  const ip = getClientIp(request);
  const ts = await verifyTurnstile(env, body.turnstileToken || '', ip);
  if (!ts.ok) return json({ error: 'turnstile_failed' }, 400);

  // Silent abuse caps (never reflected in the response — always { ok: true }).
  const ipAllowed = await checkRateLimit(env, 'forgot:ip:' + ip, 20);
  const emailAllowed = await checkRateLimit(env, 'forgot:email:' + (await sha256Hex(email)), 5);

  const user = await getUserByEmail(env, email);
  if (user && user.password_hash && ipAllowed && emailAllowed && env.RESEND_API_KEY) {
    const token = await createEmailToken(env, user.id, 'reset', RESET_TOKEN_TTL_MS);
    const link = `${appUrl(env)}/reset/?token=${token}&next=${encodeURIComponent(next)}`;
    await sendResendEmail(env, {
      to: email,
      subject: 'Reset your FreeQrly password',
      html: `<p>Click the link below to reset your FreeQrly password. It expires in 1 hour.</p>`
        + `<p><a href="${link}">Reset my password</a></p>`
        + `<p>If you didn't request this, you can ignore this email — your password won't change.</p>`,
      text: `Reset your FreeQrly password:\n\n${link}\n\nThis link expires in 1 hour. If you didn't request it, ignore this email — your password won't change.`,
    });
  }
  return json({ ok: true });
}
