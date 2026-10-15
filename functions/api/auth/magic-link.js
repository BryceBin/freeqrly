// POST /api/auth/magic-link — request a sign-in email link.
// Body: { email, turnstileToken }
// ALWAYS 200 { ok: true } even if the email is unknown (anti-enumeration).
// 400 invalid email / failed Turnstile, 429 rate limited, 503 email login unavailable.
import { json, sha256Hex } from '../../_lib/dynamic.js';
import {
  appUrl, genToken, getClientIp, verifyTurnstile, checkRateLimit, upsertUser,
  MAGIC_LINK_TTL_MS,
} from '../../_lib/auth.js';

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

export async function onRequestPost({ request, env }) {
  if (!env.DB) return json({ error: 'Auth not configured yet' }, 503);
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400); }
  const email = String(body.email || '').trim().toLowerCase();
  const turnstileToken = body.turnstileToken || '';
  if (!email || email.length > 254 || !EMAIL_RE.test(email)) return json({ error: 'Invalid email' }, 400);

  // Turnstile (server-side siteverify; skipped with a warning when no secret is configured)
  const ip = getClientIp(request);
  const ts = await verifyTurnstile(env, turnstileToken, ip);
  if (!ts.ok) return json({ error: 'turnstile_failed' }, 400);

  // Rate limits: 5/hr per email AND 5/hr per IP (D1 counting, create_limits-style)
  const emailKey = 'magic:email:' + (await sha256Hex(email));
  if (!(await checkRateLimit(env, emailKey, 5))) return json({ error: 'rate_limited' }, 429);
  if (!(await checkRateLimit(env, 'magic:ip:' + ip, 5))) return json({ error: 'rate_limited' }, 429);

  if (!env.RESEND_API_KEY) return json({ error: 'email_login_unavailable' }, 503);

  // Upsert user (auth_provider='email'), create one-time token (hash only in DB)
  const user = await upsertUser(env, { email, name: null, avatar_url: null, auth_provider: 'email' });
  const token = genToken(32);
  const tokenHash = await sha256Hex(token);
  await env.DB.prepare(
    'INSERT INTO email_tokens (token_hash, user_id, purpose, expires_at, used) VALUES (?, ?, ?, ?, 0)'
  ).bind(tokenHash, user.id, 'magic_login', Date.now() + MAGIC_LINK_TTL_MS).run();

  const link = `${appUrl(env)}/api/auth/verify?token=${token}`;
  try {
    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: 'FreeQrly <login@freeqrly.com>',
        to: email,
        subject: 'Sign in to FreeQrly',
        html: `<p>Click the link below to sign in to FreeQrly. It expires in 15 minutes.</p>`
          + `<p><a href="${link}">Sign in to FreeQrly</a></p>`
          + `<p>If you didn't request this, you can ignore this email.</p>`,
        text: `Sign in to FreeQrly:\n\n${link}\n\nThis link expires in 15 minutes. If you didn't request it, ignore this email.`,
      }),
    });
    if (!res.ok) console.error('Resend send failed:', res.status, await res.text().catch(() => ''));
  } catch (e) {
    console.error('Resend send error:', e);
  }
  // Always 200 — never reveal whether the email exists or whether sending failed.
  return json({ ok: true });
}
