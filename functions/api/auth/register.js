// POST /api/auth/register — email + password registration.
// Body: { email, password, next?, turnstileToken? }
// - email format validated; password must be ≥ 8 chars (else weak_password).
// - If the email already exists via ANY method → 409 already_registered
//   ("already registered, please log in") — never reveals which method.
// - Else creates the user (email_verified=0, password_hash set) + a single-use
//   email-verification token (purpose=verify, 24 h expiry, SHA-256 hash only)
//   and sends the verification email via Resend from FreeQrly <login@freeqrly.com>.
// - Optional `next` is validated (same-origin path only) and embedded in the
//   verification link; verify redirects to /login/?verified=1&next=<next>.
// Always { ok: true } on success — the user must verify before they can log in.
import { json } from '../../_lib/dynamic.js';
import {
  appUrl, getClientIp, verifyTurnstile, checkRateLimit, getUserByEmail,
  createPasswordUser, createEmailToken, sendResendEmail, hashPassword,
  validateNext, EMAIL_RE, MIN_PASSWORD_LEN, VERIFY_TOKEN_TTL_MS,
} from '../../_lib/auth.js';

export async function onRequestPost({ request, env }) {
  if (!env.DB) return json({ error: 'Auth not configured yet' }, 503);
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const email = String(body.email || '').trim().toLowerCase();
  const password = String(body.password || '');
  const next = validateNext(body.next);
  if (!email || email.length > 254 || !EMAIL_RE.test(email)) return json({ error: 'Invalid email' }, 400);
  if (!password || password.length < MIN_PASSWORD_LEN) return json({ error: 'weak_password' }, 400);

  const ip = getClientIp(request);
  const ts = await verifyTurnstile(env, body.turnstileToken || '', ip);
  if (!ts.ok) return json({ error: 'turnstile_failed' }, 400);

  // Per-IP registration limit (D1 counting, create_limits-style)
  if (!(await checkRateLimit(env, 'register:ip:' + ip, 10))) return json({ error: 'rate_limited' }, 429);

  if (!env.RESEND_API_KEY) return json({ error: 'email_login_unavailable' }, 503);

  // Existing email (ANY method) → 409. Never reveal which method they used.
  const existing = await getUserByEmail(env, email);
  if (existing) return json({ error: 'already_registered', message: 'already registered, please log in' }, 409);

  const passwordHash = await hashPassword(password);
  const user = await createPasswordUser(env, email, passwordHash);
  const token = await createEmailToken(env, user.id, 'verify', VERIFY_TOKEN_TTL_MS);
  const link = `${appUrl(env)}/api/auth/verify?token=${token}&next=${encodeURIComponent(next)}`;
  await sendResendEmail(env, {
    to: email,
    subject: 'Verify your FreeQrly email',
    html: `<p>Thanks for signing up for FreeQrly. Click the link below to verify your email. It expires in 24 hours.</p>`
      + `<p><a href="${link}">Verify my email</a></p>`
      + `<p>If you didn't create this account, you can ignore this email.</p>`,
    text: `Verify your FreeQrly email:\n\n${link}\n\nThis link expires in 24 hours. If you didn't create this account, ignore this email.`,
  });
  return json({ ok: true });
}
