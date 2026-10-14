/* Catch-all: Pages Functions run before static assets, so we manually
   fall through to the asset server for known path patterns. Only truly
   unknown paths get the branded 404 (fixes soft-404s hurting SEO).
   Pattern-based (not enumerated) so new blog posts/pages just work. */
const TOP_LEVEL = new Set([
  'scan', 'about', 'developers',
  'sitemap.xml', 'robots.txt', 'llms.txt', 'og.png', 'favicon.ico', '404.html',
  'google-form-qr-code', 'wifi-qr-code', 'vcard-qr-code', 'batch-qr-code',
  'business-card-qr-code', 'google-review-qr-code', 'qr-code-with-logo',
  'wedding-qr-code', 'instagram-qr-code', 'real-estate-qr-code',
]);

function isKnown(path) {
  if (path === '/') return true;
  if (path.startsWith('/assets/') || path.startsWith('/skills/')) return true;
  if (path.startsWith('/api/')) return true;
  if (path === '/mcp') return true;
  if (path === '/blog/' || path.startsWith('/blog/')) return true;
  const seg = path.replace(/\/$/, '').slice(1);
  if (!seg.includes('/') && TOP_LEVEL.has(seg)) return true;
  return false;
}

export async function onRequest(context) {
  const url = new URL(context.request.url);
  if (isKnown(url.pathname)) {
    return context.env.ASSETS.fetch(context.request);
  }
  try {
    const notFound = await context.env.ASSETS.fetch(
      new URL('/404.html', context.request.url)
    );
    return new Response(notFound.body, {
      status: 404,
      headers: { 'Content-Type': 'text/html; charset=utf-8' },
    });
  } catch (e) {
    return new Response('Not found', { status: 404 });
  }
}
