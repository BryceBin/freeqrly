/* Catch-all: Pages Functions run before static assets, so we manually
   fall through to the asset server first. Only truly unknown paths get
   the branded 404 (fixes soft-404s hurting SEO). */
const STATIC_PREFIXES = ['/assets/', '/skills/'];
const STATIC_FILES = new Set([
  '/', '/sitemap.xml', '/robots.txt', '/llms.txt', '/og.png', '/favicon.ico',
  '/404.html', '/scan/', '/about/', '/blog/',
  '/developers/', '/api/qr', '/mcp',
  '/google-form-qr-code/', '/wifi-qr-code/', '/vcard-qr-code/',
  '/batch-qr-code/', '/business-card-qr-code/', '/google-review-qr-code/',
  '/qr-code-with-logo/', '/wedding-qr-code/', '/instagram-qr-code/',
  '/real-estate-qr-code/',
  '/blog/how-to-scan-a-qr-code/', '/blog/why-is-my-qr-code-not-working/',
  '/blog/qr-code-print-size-guide/', '/blog/qr-codes-for-restaurants/',
  '/blog/free-qr-codes-that-dont-expire/', '/blog/do-qr-codes-expire/',
  '/blog/static-vs-dynamic-qr-codes/',
]);

function isKnown(path) {
  if (STATIC_FILES.has(path)) return true;
  if (path.endsWith('/') && STATIC_FILES.has(path.slice(0, -1))) return true;
  return STATIC_PREFIXES.some(p => path.startsWith(p));
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
