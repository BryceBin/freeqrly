// POST /api/auth/login — email + password login.
// Body: { email, password, turnstileToken? }
// - No user / wrong password / user has NULL password_hash (OAuth-only
//   account) → the SAME generic 401 invalid_credentials (no user enumeration).
// - Correct password but email_verified=0 → 403 email_not_verified
//   ("verify your email first") + a fresh verification email is sent.
// - 5 failures per IP+email → 15 min lockout (429 rate_limited).
// - Success: session (opaque token, SHA-256 hash in D1, 30-day expiry),
//   HttpOnly/Secure/SameSite=Lax cookie, { ok: true, user: { id, email } }.
//   password_hash is NEVER returned.
import { json, sha256Hex } from '../../_lib/dynamic.js';
import {
  appUrl, getClientIp, verifyTurnstile, checkRateLimit, getUserByEmail,
  verifyPassword, createSession, sessionCookie, createEmailToken,
  sendResendEmail, loginLockoutKey, checkLoginLockout, recordLoginFailure,
  clearLoginFailures, EMAIL_RE, VERIFY_TOKEN_TTL_MS,
} from '../../_lib/auth.js';

export async function onRequestPost({ request, env }) {
  if (!env.DB) return json({ error: 'Auth not configured yet' }, 503);
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const email = String(body.email || '').trim().toLowerCase();
  const password = String(body.password || '');
  if (!email || !password || !EMAIL_RE.test(email)) return json({ error: 'invalid_credentials' }, 400);

  const ip = getClientIp(request);
  const ts = await verifyTurnstile(env, body.turnstileToken || '', ip);
  if (!ts.ok) return json({ error: 'turnstile_failed' }, 400);

  const lockKey = await loginLockoutKey(ip, email);
  const lock = await checkLoginLockout(env, lockKey);
  if (lock.locked) {
    return json({ error: 'rate_limited', retry_after_seconds: lock.retryAfterSeconds }, 429);
  }

  const user = await getUserByEmail(env, email);
  // Generic failure for all three cases: no user, no password_hash (OAuth-only
  // account), wrong password. No enumeration.
  if (!user || !user.password_hash || !(await verifyPassword(password, user.password_hash))) {
    await recordLoginFailure(env, lockKey);
    return json({ error: 'invalid_credentials' }, 401);
  }

  // Correct password but unverified email → ask to verify + resend the link
  // (resend itself rate-limited per email so this can't be used to spam).
  if (!user.email_verified) {
    if (await checkRateLimit(env, 'verify-resend:email:' + (await sha256Hex(email)), 5)) {
      const token = await createEmailToken(env, user.id, 'verify', VERIFY_TOKEN_TTL_MS);
      const link = `${appUrl(env)}/api/auth/verify?token=${token}&next=${encodeURIComponent('/dashboard/')}`;
      await sendResendEmail(env, {
        to: email,
        subject: 'Verify your FreeQrly email',
        html: `<p>Click the link below to verify your FreeQrly email. It expires in 24 hours.</p>`
          + `<p><a href="${link}">Verify my email</a></p>`
          + `<p>If you didn't request this, you can ignore this email.</p>`,
        text: `Verify your FreeQrly email:\n\n${link}\n\nThis link expires in 24 hours. If you didn't request it, ignore this email.`,
      });
    }
    return json({ error: 'email_not_verified', message: 'verify your email first' }, 403);
  }

  await clearLoginFailures(env, lockKey);
  await env.DB.prepare('UPDATE users SET last_login_at = ? WHERE id = ?').bind(Date.now(), user.id).run();
  const sessionToken = await createSession(env, user.id, request);
  return new Response(JSON.stringify({ ok: true, user: { id: user.id, email: user.email } }), {
    status: 200,
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', 'Set-Cookie': sessionCookie(sessionToken) },
  });
}
