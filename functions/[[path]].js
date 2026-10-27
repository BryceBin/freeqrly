// Catch-all: serve known static pages, 404 the rest.
// - /manage/* permanently moved to /dashboard/* (301, path + query kept).
// - Localized pages live at /<lang>/<slug>/, /<lang>/blog/... and /<lang>/404.html.

const LANGS = new Set(['zh', 'es', 'hi', 'ar', 'pt', 'fr', 'ru', 'de', 'ja']);
// Localizable content slugs (landing pages + content/auth pages). Dashboard,
// /q/ links and API routes are intentionally NOT localizable.
const LANG_SLUGS = new Set([
  'google-form-qr-code', 'wifi-qr-code', 'vcard-qr-code', 'batch-qr-code',
  'business-card-qr-code', 'google-review-qr-code', 'qr-code-with-logo',
  'wedding-qr-code', 'instagram-qr-code', 'real-estate-qr-code',
  'pdf-qr-code', 'multi-link-qr-code', 'menu-qr-code',
  'payment-qr-code', 'youtube-qr-code', 'whatsapp-qr-code',
  'tiktok-qr-code', 'spotify-qr-code', 'facebook-qr-code',
  'google-maps-qr-code',
  'bitcoin-qr-code', 'coupon-qr-code', 'app-store-qr-code', 'mp3-qr-code',
  'black-friday-qr-code', 'christmas-qr-code',
  'about', 'privacy', 'terms', 'pricing', 'developers', 'scan', 'barcode-generator', 'login', 'reset',
]);

const TOP_LEVEL = new Set([
  'scan', 'barcode-generator', 'about', 'developers', 'login', 'dashboard', 'privacy', 'terms', 'pricing', 'reset',
  'zh', 'es', 'hi', 'ar', 'pt', 'fr', 'ru', 'de', 'ja',
  'sitemap.xml', 'robots.txt', 'llms.txt', 'og.png', 'favicon.ico', '404.html',
  'google-form-qr-code', 'wifi-qr-code', 'vcard-qr-code', 'batch-qr-code',
  'business-card-qr-code', 'google-review-qr-code', 'qr-code-with-logo',
  'wedding-qr-code', 'instagram-qr-code', 'real-estate-qr-code',
  'pdf-qr-code', 'multi-link-qr-code', 'menu-qr-code',
  'payment-qr-code', 'youtube-qr-code', 'whatsapp-qr-code',
  'tiktok-qr-code', 'spotify-qr-code', 'facebook-qr-code',
  'google-maps-qr-code',
  'bitcoin-qr-code', 'coupon-qr-code', 'app-store-qr-code', 'mp3-qr-code',
  'black-friday-qr-code', 'christmas-qr-code',
  'dynamic-qr-code', 'ticket-qr-code']);

function isKnown(path) {
  if (path === '/') return true;
  if (path.startsWith('/assets/') || path.startsWith('/skills/')) return true;
  if (path.startsWith('/api/')) return true;
  if (path === '/mcp') return true;
  if (path === '/dashboard/i18n.json') return true; // Dashboard translations (static JSON)
  if (path === '/blog/' || path.startsWith('/blog/')) return true;
  const clean = path.replace(/\/$/, '');
  const seg = clean.slice(1);
  if (!seg.includes('/') && TOP_LEVEL.has(seg)) return true;
  // Localized pages: /<lang>/<slug>/, /<lang>/blog/... and /<lang>/404.html
  const parts = seg.split('/');
  if (parts.length >= 2 && LANGS.has(parts[0])) {
    if (parts.length === 2 && (LANG_SLUGS.has(parts[1]) || parts[1] === '404.html')) return true;
    if (parts[1] === 'blog' && parts.length <= 3) return true;
  }
  return false;
}

export async function onRequest(context) {
  const url = new URL(context.request.url);
  // Canonical domain: www -> apex (301, path + query kept). NOTE: this has to
  // live here and not only in _redirects — this catch-all function intercepts
  // every request before _redirects is evaluated, so a _redirects-only rule
  // silently never fires (verified 2026-10-20: www returned 200, not 301).
  if (url.hostname === 'www.freeqrly.com') {
    url.hostname = 'freeqrly.com';
    return Response.redirect(url.toString(), 301);
  }
  // /manage/* permanently moved to /dashboard/* (keep path + query).
  if (url.pathname === '/manage' || url.pathname.startsWith('/manage/')) {
    return Response.redirect(new URL(url.pathname.replace(/^\/manage/, '/dashboard') + url.search, url.origin), 301);
  }
  if (isKnown(url.pathname)) {
    return context.env.ASSETS.fetch(context.request);
  }
  try {
    // Serve a localized 404 when the URL starts with a language code.
    const first = url.pathname.split('/')[1];
    const page404 = LANGS.has(first) ? `/${first}/404.html` : '/404.html';
    let notFound = await context.env.ASSETS.fetch(new URL(page404, context.request.url));
    if (!notFound || notFound.status === 404) {
      notFound = await context.env.ASSETS.fetch(new URL('/404.html', context.request.url));
    }
    return new Response(notFound.body, {
      status: 404,
      headers: { 'Content-Type': 'text/html; charset=utf-8' },
    });
  } catch (e) {
    return new Response('Not found', { status: 404 });
  }
}
