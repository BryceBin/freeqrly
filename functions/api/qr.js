import QR from '../_lib/qrcode.js';

const qrcode = QR && QR.default ? QR.default : QR;
const HEX = /^[0-9a-fA-F]{6}$/;

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, OPTIONS',
  'Access-Control-Max-Age': '86400',
};

function err(msg, status = 400) {
  return new Response(JSON.stringify({ error: msg }), {
    status,
    headers: { 'Content-Type': 'application/json', ...CORS },
  });
}

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS });
}

// GET /api/qr?data=TEXT&size=1024&margin=4&color=2F4A62&bgcolor=ffffff&ecc=M
// Returns image/svg+xml. Free, no key, CORS open — built for agents.
export async function onRequestGet({ request }) {
  const q = new URL(request.url).searchParams;
  const data = q.get('data') || '';

  if (!data) return err('Missing required query param: data');
  if (data.length > 2000) return err('data too long (max 2000 chars)');

  let size = parseInt(q.get('size') || '1024', 10);
  if (!Number.isFinite(size)) return err('size must be a number');
  size = Math.min(2048, Math.max(128, size));

  let margin = parseInt(q.get('margin') || '4', 10);
  if (!Number.isFinite(margin)) return err('margin must be a number');
  margin = Math.min(10, Math.max(0, margin));

  const color = (q.get('color') || '2F4A62').replace(/^#/, '');
  const bgcolor = (q.get('bgcolor') || 'ffffff').replace(/^#/, '');
  if (!HEX.test(color)) return err('color must be a 6-digit hex value');
  if (!HEX.test(bgcolor)) return err('bgcolor must be a 6-digit hex value');

  const ecc = (q.get('ecc') || 'M').toUpperCase();
  if (!['L', 'M', 'Q', 'H'].includes(ecc)) return err('ecc must be one of L, M, Q, H');

  let qr;
  try {
    qr = qrcode(0, ecc);
    qr.addData(data);
    qr.make();
  } catch (e) {
    return err('Could not encode data as QR: ' + String(e && e.message || e), 422);
  }

  let svg = qr.createSvgTag(1, margin);
  // Recolor: background rect + module path, then pin output size.
  svg = svg
    .replace('fill="white"', `fill="#${bgcolor}"`)
    .replace('<path d="', `<path fill="#${color}" d="`)
    .replace(/width="[^"]*" height="[^"]*"/, `width="${size}" height="${size}"`);

  return new Response(svg, {
    status: 200,
    headers: {
      'Content-Type': 'image/svg+xml; charset=utf-8',
      'Cache-Control': 'public, max-age=31536000, immutable',
      'Content-Disposition': 'inline; filename="freeqrly.svg"',
      ...CORS,
    },
  });
}
