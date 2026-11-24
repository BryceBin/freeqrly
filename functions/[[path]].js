// Catch-all: serve known static pages, 404 the rest.
// - /manage/* permanently moved to /dashboard/* (301, path + query kept).
// - ?lang= retired for content pages: ?lang=<code> 301s to the matching
//   /<lang>/ path (?lang=en / unknown values 301 to the clean path).
//   Only home, landing slugs and /blog/... redirect; dashboard, /api/,
//   /q/ and other non-localizable routes keep reading ?lang= client-side.
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
  'dynamic-qr-code', 'ticket-qr-code',
  'freeqrly-vs-qr-tiger', 'freeqrly-vs-qr-code-monkey',
  'freeqrly-vs-qr-code-generator', 'qr-tiger-alternative',
  'qr-code-monkey-alternative',
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
  'dynamic-qr-code', 'ticket-qr-code',
  'freeqrly-vs-qr-tiger', 'freeqrly-vs-qr-code-monkey',
  'freeqrly-vs-qr-code-generator', 'qr-tiger-alternative',
  'qr-code-monkey-alternative']);

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

// Visitor's preferred UI language, or null when it cannot be determined.
// Order: an explicit choice stored by the language menu, then the browser's
// Accept-Language (already ordered by q-value). Unknown values are ignored.
// 'en' is a real answer here — it means "stay on /".
function pickLanguage(request) {
  const cookie = request.headers.get('Cookie') || '';
  const saved = cookie.match(/(?:^|;\s*)fq_lang=(en|zh|es|hi|ar|pt|fr|ru|de|ja)(?:;|$)/);
  if (saved) return saved[1];
  const accept = request.headers.get('Accept-Language') || '';
  for (const part of accept.split(',')) {
    const tag = part.split(';')[0].trim().toLowerCase();
    if (!tag || tag === '*') continue;
    const base = tag.split('-')[0];
    if (base === 'en') return 'en';
    if (LANGS.has(base)) return base;
  }
  return null;
}

function isLocalizable(path) {
  if (path === '/') return true;
  if (path === '/blog' || path === '/blog/' || path.startsWith('/blog/')) return true;
  const clean = path.replace(/\/$/, '');
  const seg = clean.slice(1);
  if (!seg.includes('/') && LANG_SLUGS.has(seg)) return true;
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
  // ?lang= retired for content pages: redirect to the matching /<lang>/ path
  // (or the clean path for ?lang=en / unknown values). Other query params
  // are kept. GET/HEAD only; POSTs and non-localizable routes are untouched.
  if ((context.request.method === 'GET' || context.request.method === 'HEAD') && url.searchParams.has('lang')) {
    const raw = url.searchParams.get('lang') || '';
    let base = url.pathname;
    const first = base.split('/')[1];
    if (LANGS.has(first)) {
      base = base.slice(first.length + 1) || '/';
      if (!base.startsWith('/')) base = '/' + base;
    }
    if (isLocalizable(base)) {
      const params = new URLSearchParams(url.search);
      params.delete('lang');
      const rest = params.toString();
      const suffix = rest ? '?' + rest : '';
      let target;
      if (raw === 'en') target = base;
      else if (LANGS.has(raw)) target = base === '/' ? `/${raw}/` : `/${raw}${base}`;
      else target = base;
      const dest = new URL(target + suffix, url.origin);
      if (dest.toString() !== url.toString()) {
        return Response.redirect(dest.toString(), 301);
      }
    }
  }
  // Homepage language negotiation: 302 to the visitor's language.
  //
  // Only the homepage used to localize itself (every other page carries an
  // explicit data-lang), and it did so client-side, which left the served
  // HTML in one language while <html lang>, the title and the canonical
  // declared another. Deciding here keeps the response, the canonical and
  // the hreflang in agreement.
  //
  // English stays on /, so the canonical URL and hreflang are unchanged and
  // Googlebot (Accept-Language: en-US) is never redirected. The redirect is
  // 302 with Vary: Accept-Language so caches key on the header, and an
  // explicit choice from the language menu (cookie fq_lang) always wins.
  if ((context.request.method === 'GET' || context.request.method === 'HEAD')
      && url.pathname === '/' && !url.searchParams.has('lang')) {
    const chosen = pickLanguage(context.request);
    if (chosen && chosen !== 'en') {
      const dest = new URL(`/${chosen}/`, url.origin);
      dest.search = url.search;
      return new Response(null, {
        status: 302,
        headers: {
          Location: dest.toString(),
          Vary: 'Accept-Language, Cookie',
          'Cache-Control': 'private, max-age=0, must-revalidate',
        },
      });
    }
  }
  if (isKnown(url.pathname)) {
    const res = await context.env.ASSETS.fetch(context.request);
    // The homepage response depends on Accept-Language / Cookie, so caches
    // must key on them. Other pages are language-independent.
    if (url.pathname === '/') {
      const headers = new Headers(res.headers);
      headers.set('Vary', 'Accept-Language, Cookie');
      return new Response(res.body, { status: res.status, headers });
    }
    return res;
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
