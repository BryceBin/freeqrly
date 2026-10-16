// Shared helpers for dynamic QR codes (redirect + analytics)
// D1 binding: context.env.DB
// Tables: codes(code, destination, created_at, total_scans)
//         daily_stats(code, date, country, device, count)

// Base62 alphabet excluding ambiguous chars (0/O, 1/l/I)
const ALPHABET = '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz';

export function genCode(len = 7) {
  const arr = new Uint8Array(len);
  crypto.getRandomValues(arr);
  return Array.from(arr, b => ALPHABET[b % ALPHABET.length]).join('');
}

export async function sha256Hex(str) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(str));
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
}

export function isValidDestination(url) {
  try {
    const u = new URL(url);
    if (u.protocol !== 'http:' && u.protocol !== 'https:') return false;
    // Block private / local addresses
    const host = u.hostname.toLowerCase();
    if (host === 'localhost' || host.endsWith('.local') || host.endsWith('.localhost')) return false;
    if (/^(10|127|172\.(1[6-9]|2\d|3[0-1])|192\.168|169\.254|0\.0\.0\.0)\./.test(host)) return false;
    return true;
  } catch { return false; }
}

// Simple device classification from User-Agent
export function deviceFromUA(ua = '') {
  const s = ua.toLowerCase();
  if (/tablet|ipad/.test(s)) return 'tablet';
  if (/mobile|android|iphone|ipod/.test(s)) return 'mobile';
  return 'desktop';
}

// OS classification from User-Agent
export function osFromUA(ua = '') {
  const s = ua.toLowerCase();
  if (/windows/.test(s)) return 'Windows';
  if (/iphone|ipad|ipod/.test(s)) return 'iOS';
  if (/android/.test(s)) return 'Android';
  if (/mac os|macintosh/.test(s)) return 'macOS';
  if (/cros/.test(s)) return 'ChromeOS';
  if (/linux/.test(s)) return 'Linux';
  return 'Other';
}

// Privacy-preserving scan fingerprint: SHA-256(IP + UA + date).
// Cannot be reversed to an IP. Used only for unique-scan counting.
export async function scanFingerprint(ip, ua, date) {
  return sha256Hex([ip || '', ua || '', date].join('|'));
}

export function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' },
  });
}
