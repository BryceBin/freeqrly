// Shared dynamic-code business logic for the Dashboard UI, the REST API
// (Bearer token) and MCP. All three surfaces behave identically: same
// validation, same quota (code_limit per user), same ownership checks.
// Errors are thrown as ApiError(status, body) so HTTP handlers can return
// json(body, status) and MCP handlers can map them to JSON-RPC errors.
import { genCode } from './dynamic.js';
import { getCodeCount } from './auth.js';
import { sanitizeStyle, parseStyle } from './style.js';
import { getLiveSubscription, resolveCodeLimit } from './billing.js';

export const VALID_TYPES = new Set([
  'url', 'text', 'wifi', 'vcard', 'email', 'sms', 'phone',
  'geo', 'event', 'bitcoin', 'coupon', 'appstore',
  'review', 'mp3', 'google-form', 'menu',
]);

export class ApiError extends Error {
  constructor(status, body) {
    super(body && body.error ? String(body.error) : 'error');
    this.status = status;
    this.body = body;
  }
}

function assertUrl(payload) {
  try {
    const u = new URL(payload);
    if (u.protocol !== 'http:' && u.protocol !== 'https:') throw new Error('bad');
  } catch {
    throw new ApiError(400, { error: 'Invalid URL' });
  }
}

// Types whose payload is a bare link (rendered/scanned as a URL).
const LINK_TYPES = new Set(['review', 'mp3', 'google-form', 'menu']);

function assertPrefix(payload, prefixes) {
  const lower = payload.toLowerCase();
  if (!prefixes.some((p) => lower.startsWith(p))) {
    throw new ApiError(400, { error: 'Invalid payload' });
  }
}

// Scheme allowlist per type. Payloads are rendered as clickable links on the
// /q/ hosted pages, so a payload like `javascript:...` must never be stored:
// without this, one click on a hosted-page button would run a script in the
// freeqrly.com origin. (Defense in depth: hosted.js also filters at render.)
function assertPayloadScheme(type, payload) {
  switch (type) {
    case 'url':
      assertUrl(payload);
      break;
    case 'email':
      assertPrefix(payload, ['mailto:']);
      break;
    case 'sms':
      assertPrefix(payload, ['sms:', 'smsto:']);
      break;
    case 'phone':
      assertPrefix(payload, ['tel:']);
      break;
    case 'geo': {
      assertPrefix(payload, ['geo:']);
      const coords = payload.slice(4).split(/[?;]/)[0];
      if (!/^-?\d+(\.\d+)?,-?\d+(\.\d+)?$/.test(coords)) {
        throw new ApiError(400, { error: 'Invalid payload' });
      }
      break;
    }
    case 'bitcoin':
      assertPrefix(payload, ['bitcoin:']);
      break;
    case 'appstore':
      for (const line of payload.split('\n')) {
        const u = line.trim();
        if (u) assertUrl(u);
      }
      break;
    case 'vcard':
      // Every URL property inside the vCard must be http(s).
      for (const m of payload.matchAll(/^URL[^:\r\n]*:(.+)$/gim)) {
        assertUrl(m[1].trim());
      }
      break;
    default:
      if (LINK_TYPES.has(type)) assertUrl(payload);
  }
}

// Validate + normalize { type, payload }. `requireType` for PATCH (type is mandatory there).
export function validateCodeInput(type, payload, { requireType = false } = {}) {
  type = (type || (requireType ? '' : 'url')).trim();
  payload = (payload || '').trim();
  if (!type || !VALID_TYPES.has(type)) throw new ApiError(400, { error: 'Invalid type' });
  if (!payload) throw new ApiError(400, { error: requireType ? 'Invalid payload' : 'payload is required' });
  if (payload.length > 8000) throw new ApiError(400, { error: requireType ? 'Invalid payload' : 'Payload too large' });
  assertPayloadScheme(type, payload);
  return { type, payload };
}

function sanitizeStyleOrThrow(style, userId) {
  try {
    return sanitizeStyle(style, userId);
  } catch {
    throw new ApiError(400, { error: 'Invalid style' });
  }
}

async function checkCreateRateLimit(env, ip) {
  const hour = new Date().toISOString().slice(0, 13);
  try {
    const cnt = await env.DB.prepare(
      'SELECT count FROM create_limits WHERE ip = ? AND hour = ?'
    ).bind(ip, hour).first();
    if (cnt && cnt.count >= 10) throw new ApiError(429, { error: 'Rate limit: too many codes created' });
    await env.DB.prepare(
      `INSERT INTO create_limits (ip, hour, count) VALUES (?, ?, 1)
       ON CONFLICT(ip, hour) DO UPDATE SET count = count + 1`
    ).bind(ip, hour).run();
  } catch (e) {
    if (e instanceof ApiError) throw e;
    /* rate limit failure is non-fatal */
  }
}

// Promotional policy (2026-10-20): existing users have code_limit = UNLIMITED
// ("limited-time, unlimited quantity"). New signups default to 8, so ending the
// promo needs no code change — just stop raising new users' limits.
export const UNLIMITED_LIMIT = 999999;

// Create a dynamic code for `user`. `origin` = e.g. https://freeqrly.com (for shortUrl).
export async function createDynamicCode(env, user, { type, payload, style }, { origin, ip }) {
  const v = validateCodeInput(type, payload);
  const used = await getCodeCount(env, user.id);
  const limit = resolveCodeLimit(user, await getLiveSubscription(env, user.id));
  const unlimited = !limit || limit >= UNLIMITED_LIMIT;
  if (!unlimited && used >= limit) throw new ApiError(403, { error: 'quota_exceeded', hint: 'upgrade' });
  const cleanStyle = style !== undefined ? sanitizeStyleOrThrow(style, user.id) : null;
  await checkCreateRateLimit(env, ip || 'unknown');

  for (let attempt = 0; attempt < 5; attempt++) {
    const candidate = genCode(7);
    try {
      await env.DB.prepare(
        'INSERT INTO codes (code, destination, type, payload, created_at, total_scans, user_id, style) VALUES (?, ?, ?, ?, ?, 0, ?, ?)'
      ).bind(candidate, v.type === 'url' ? v.payload : '', v.type, v.payload, Date.now(), user.id,
        cleanStyle ? JSON.stringify(cleanStyle) : null).run();
      return { code: candidate, shortUrl: `${origin}/q/${candidate}`, type: v.type };
    } catch (e) {
      if (String(e.message || e).includes('UNIQUE')) continue;
      throw new ApiError(500, { error: 'Failed to create code' });
    }
  }
  throw new ApiError(500, { error: 'Failed to generate unique code' });
}

async function ownedCode(env, user, code) {
  const row = await env.DB.prepare('SELECT user_id, style FROM codes WHERE code = ?').bind(code).first();
  if (!row) throw new ApiError(404, { error: 'Code not found' });
  if (row.user_id !== user.id) throw new ApiError(403, { error: 'forbidden' });
  return row;
}

export async function updateDynamicCode(env, user, code, { type, payload, style }) {
  code = (code || '').trim();
  const v = validateCodeInput(type, payload, { requireType: true });
  await ownedCode(env, user, code);

  let styleSql = '', styleVal = null;
  if (style !== undefined) {
    const clean = sanitizeStyleOrThrow(style, user.id);
    styleSql = ', style = ?';
    styleVal = clean ? JSON.stringify(clean) : null;
  }
  await env.DB.prepare(
    `UPDATE codes SET type = ?, payload = ?, destination = ?${styleSql} WHERE code = ?`
  ).bind(v.type, v.payload, v.type === 'url' ? v.payload : '', ...(styleSql ? [styleVal] : []), code).run();
  return { ok: true, code, type: v.type, payload: v.payload };
}

export async function deleteDynamicCode(env, user, code) {
  code = (code || '').trim();
  const row = await ownedCode(env, user, code);

  const style = parseStyle(row.style);
  const logoKey = style && style.logoKey ? style.logoKey : null;

  await env.DB.batch([
    env.DB.prepare('DELETE FROM codes WHERE code = ?').bind(code),
    env.DB.prepare('DELETE FROM daily_stats WHERE code = ?').bind(code),
    env.DB.prepare('DELETE FROM scan_fingerprints WHERE code = ?').bind(code),
  ]);

  // Best-effort R2 cleanup: only delete the uploaded logo when no other
  // code of this user still references it.
  if (logoKey && env.LOGOS) {
    try {
      const others = await env.DB.prepare(
        'SELECT COUNT(*) AS n FROM codes WHERE user_id = ? AND style LIKE ?'
      ).bind(user.id, `%${logoKey}%`).first();
      if (!others || others.n === 0) await env.LOGOS.delete(logoKey);
    } catch { /* orphaned logo is harmless */ }
  }
  return { ok: true, code };
}

export async function listDynamicCodes(env, user) {
  const rows = await env.DB.prepare(
    'SELECT code, type, destination, payload, style, total_scans, created_at FROM codes WHERE user_id = ? ORDER BY created_at DESC LIMIT 100'
  ).bind(user.id).all();
  const used = await getCodeCount(env, user.id);
  const limit = resolveCodeLimit(user, await getLiveSubscription(env, user.id));
  return {
    codes: (rows.results || []).map((r) => ({
      code: r.code,
      type: r.type || 'url',
      destination: String(r.destination || r.payload || '').slice(0, 120),
      payload: r.payload || '',
      style: parseStyle(r.style),
      totalScans: r.total_scans || 0,
      created_at: r.created_at,
    })),
    quota: { used, limit },
  };
}

export async function getCodeStats(env, user, code) {
  code = (code || '').trim();
  const row = await env.DB.prepare(
    'SELECT user_id, type, payload, destination, total_scans, created_at FROM codes WHERE code = ?'
  ).bind(code).first();
  if (!row) throw new ApiError(404, { error: 'Code not found' });
  if (row.user_id !== user.id) throw new ApiError(403, { error: 'forbidden' });

  const byDate = await env.DB.prepare(
    `SELECT date, SUM(count) AS scans FROM daily_stats WHERE code = ? GROUP BY date ORDER BY date DESC LIMIT 30`
  ).bind(code).all();
  const byCountry = await env.DB.prepare(
    `SELECT country, SUM(count) AS scans FROM daily_stats WHERE code = ? GROUP BY country ORDER BY scans DESC LIMIT 10`
  ).bind(code).all();
  const byDevice = await env.DB.prepare(
    `SELECT device, SUM(count) AS scans FROM daily_stats WHERE code = ? GROUP BY device ORDER BY scans DESC LIMIT 10`
  ).bind(code).all();
  const byCity = await env.DB.prepare(
    `SELECT city, SUM(count) AS scans FROM daily_stats WHERE code = ? AND city != '' GROUP BY city ORDER BY scans DESC LIMIT 10`
  ).bind(code).all();
  const byOS = await env.DB.prepare(
    `SELECT os, SUM(count) AS scans FROM daily_stats WHERE code = ? GROUP BY os ORDER BY scans DESC LIMIT 10`
  ).bind(code).all();
  const uniqueRow = await env.DB.prepare(
    `SELECT COUNT(DISTINCT fingerprint) AS n FROM scan_fingerprints WHERE code = ?`
  ).bind(code).first();
  const uniqueByDate = await env.DB.prepare(
    `SELECT date, COUNT(*) AS uniques FROM scan_fingerprints WHERE code = ? GROUP BY date ORDER BY date DESC LIMIT 30`
  ).bind(code).all();

  return {
    code,
    type: row.type || 'url',
    payload: row.payload || row.destination || '',
    destination: row.destination || '',
    totalScans: row.total_scans,
    createdAt: row.created_at,
    byDate: byDate.results || [],
    byCountry: byCountry.results || [],
    byDevice: byDevice.results || [],
    byCity: byCity.results || [],
    byOS: byOS.results || [],
    uniqueScans: (uniqueRow && uniqueRow.n) || 0,
    uniqueByDate: uniqueByDate.results || [],
  };
}
