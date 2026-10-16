// GET /api/logos/:key — serve a user-uploaded logo from R2.
// No session check: the key is 128-bit random (a capability URL).
// SVGs are served with a sandbox CSP so a crafted SVG cannot run script
// even if someone navigates directly to the URL (in <img> tags SVGs are
// inert anyway). Long-lived cache: logo keys are immutable.
const KEY_RE = /^u_[A-Za-z0-9_-]+_[0-9a-f]{32}\.(png|jpg|jpeg|webp|gif|svg)$/;
const CT = { png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg', webp: 'image/webp', gif: 'image/gif', svg: 'image/svg+xml' };

export async function onRequestGet(context) {
  const { env, params } = context;
  const key = params.key || '';
  if (!KEY_RE.test(key)) return new Response('Not found', { status: 404 });
  if (!env.LOGOS) return new Response('Logo storage not configured', { status: 503 });
  const obj = await env.LOGOS.get(key);
  if (!obj) return new Response('Not found', { status: 404 });
  const ext = key.split('.').pop().toLowerCase();
  return new Response(obj.body, {
    headers: {
      'Content-Type': obj.httpMetadata?.contentType || CT[ext] || 'application/octet-stream',
      'Cache-Control': 'public, max-age=31536000, immutable',
      'Content-Security-Policy': "default-src 'none'; sandbox",
      'X-Content-Type-Options': 'nosniff',
    },
  });
}
