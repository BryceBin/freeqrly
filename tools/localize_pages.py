#!/usr/bin/env python3
"""Render localized static pages: /<lang>/<slug>/ from EN source + translations.

Input:  tools/i18n/<lang>.json  -> {page: {en_string: translation}, ...}
        tools/i18n/extract/<page>.en.json (for the page list)
Output: <lang>/<slug>/index.html (and <lang>/404.html) per page.
Rules: longest EN string first; short bare strings (no space/tag) only match
on HTML/quote boundaries so 'Email' never corrupts 'Email address'.
Post: <html lang/data-lang/dir>, full hreflang set, self canonical.
Usage: python3 tools/localize-pages.py [lang ...]  (default: all 9)
"""
import json, os, re, subprocess, sys

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."
I18N_DIR = os.path.join(SITE, "tools/i18n")
LANGS = ["zh", "es", "hi", "ar", "pt", "fr", "ru", "de", "ja"]
BASE = "https://freeqrly.com"

# app.js I18N (client-side translations) — the single source of truth for
# generator UI labels. Loaded lazily via node, exactly like
# build-home-i18n.py (string-aware brace counting, never hardcoded line
# slices). Used by the data-i18n pass in localize_page() below.
_APP_I18N = None
def _app_i18n():
    global _APP_I18N
    if _APP_I18N is None:
        js = subprocess.run(["node", "-e", """
const fs=require('fs');
const app=fs.readFileSync('assets/js/app.js','utf8');
const start=app.indexOf('const I18N = ') + 'const I18N = '.length;
let _i=start, _d=0, _instr=null, _esc=false;
for (; _i<app.length; _i++) {
  const _c=app[_i];
  if (_instr) { if (_esc) _esc=false; else if (_c==='\\\\') _esc=true; else if (_c===_instr) _instr=null; }
  else { if (_c==='"' || _c==="'") _instr=_c; else if (_c==='{') _d++; else if (_c==='}') { _d--; if (_d===0) break; } }
}
const I18N=eval('('+app.slice(start, _i+1)+')');
console.log(JSON.stringify(I18N));
"""], capture_output=True, text=True, cwd=SITE)
        if js.returncode != 0:
            raise RuntimeError(f"node failed to extract app.js I18N: {js.stderr}")
        _APP_I18N = json.loads(js.stdout)
    return _APP_I18N

# page key -> (en source relpath, localized relpath)
PAGES = {
    "login": ("login/index.html", "{lang}/login/index.html"),
    "reset": ("reset/index.html", "{lang}/reset/index.html"),
    "404": ("404.html", "{lang}/404.html"),
    "privacy": ("privacy/index.html", "{lang}/privacy/index.html"),
    "terms": ("terms/index.html", "{lang}/terms/index.html"),
    "pricing": ("pricing/index.html", "{lang}/pricing/index.html"),
    "about": ("about/index.html", "{lang}/about/index.html"),
    "scan": ("scan/index.html", "{lang}/scan/index.html"),
    "barcode-generator": ("barcode-generator/index.html", "{lang}/barcode-generator/index.html"),
    "developers": ("developers/index.html", "{lang}/developers/index.html"),
    "blog-index": ("blog/index.html", "{lang}/blog/index.html"),
}
LANDING = ["google-form-qr-code", "wifi-qr-code", "vcard-qr-code", "batch-qr-code",
           "business-card-qr-code", "google-review-qr-code", "qr-code-with-logo",
           "wedding-qr-code", "instagram-qr-code", "real-estate-qr-code",
           "pdf-qr-code", "multi-link-qr-code", "menu-qr-code",
           "payment-qr-code", "youtube-qr-code", "whatsapp-qr-code",
           "tiktok-qr-code", "spotify-qr-code", "facebook-qr-code",
           "google-maps-qr-code",
           "bitcoin-qr-code", "coupon-qr-code", "app-store-qr-code",
           "mp3-qr-code", "black-friday-qr-code", "christmas-qr-code",
           "dynamic-qr-code", "ticket-qr-code",
           "freeqrly-vs-qr-tiger", "freeqrly-vs-qr-code-monkey",
           "freeqrly-vs-qr-code-generator", "qr-tiger-alternative",
           "qr-code-monkey-alternative"]
for d in LANDING:
        PAGES[f"landing-{d}"] = (f"{d}/index.html", "{lang}/" + d + "/index.html")
for d in sorted(os.listdir(os.path.join(SITE, "blog"))):
    if os.path.isdir(os.path.join(SITE, "blog", d)):
        PAGES[f"blog-{d}"] = (f"blog/{d}/index.html", "{lang}/blog/" + d + "/index.html")

JS_PAGES = {"login": "login.js", "reset": "reset.js", "scan": "scan.js"}

def page_url(key, lang):
    """Canonical URL path for a page in a language (lang='en' -> EN path)."""
    if key == "404":
        return None
    src, _ = PAGES[key]
    if lang == "en":
        return "/" + src.replace("index.html", "") if src != "404.html" else None
    out = PAGES[key][1].format(lang=lang)
    return "/" + out.replace("index.html", "")

def hreflang_block(key):
    lines = []
    en = page_url(key, "en")
    lines.append(f'<link rel="alternate" hreflang="en" href="{BASE}{en}">')
    for lang in LANGS:
        lines.append(f'<link rel="alternate" hreflang="{lang}" href="{BASE}{page_url(key, lang)}">')
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{BASE}{en}">')
    return "\n".join(lines)

def localize_page(key, lang, trans):
    src_rel, out_tmpl = PAGES[key]
    src = open(os.path.join(SITE, src_rel), encoding="utf-8").read()
    out = src
    missing = []
    # JSON-LD blocks are JSON, not HTML. A translation that puts a double
    # quote inside a value (es/pt "gratis") broke the document when the plain
    # substitution loop dropped it in raw: the EN key had no quotes, so no
    # escaped variant existed, and the FAQPage script stopped parsing.
    # Lift the blocks out first, translate them with JSON-escaped strings,
    # and refuse to write a page whose JSON-LD does not parse.
    _jsonld = []

    def _stash(m):
        _jsonld.append(m.group(2))
        return "%s\x00__FQJSONLD_%d\x00%s" % (m.group(1), len(_jsonld) - 1, m.group(3))

    out = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)',
                 _stash, out, flags=re.S)

    def _json_escape(s):
        return (s.replace("\\", "\\\\").replace('"', '\\"')
                 .replace("\r\n", "\\n").replace("\n", "\\n").replace("\r", "\\n"))

    # JSON-LD: string values appear with \" escapes (json.dumps), so the plain
    # EN string never matches inside <script type="application/ld+json">.
    # FAQ answers with <a href="..."> links stayed English in localized pages
    # for exactly this reason. Also replace the escaped variants.
    for en in list(trans.keys()):
        # Identity keys (tr == en) are included too: their escaped forms
        # also need shielding in the main loop below.
        if '"' in en:
            esc_en = en.replace('"', '\\"')
            if esc_en not in trans:
                trans[esc_en] = trans[en].replace('"', '\\"')
    # HTML entity: the extractor decodes &amp; -> & in keys, but the HTML
    # body has &amp;, so a key with a raw & never matches the body
    # (e.g. the print-size-guide 'Flyers & menus' paragraph stayed English
    # in all 9 languages). Add the &amp; variant, plus the combined
    # \" + &amp; variant for JSON-LD strings that contain both.
    for en in list(trans.keys()):
        # Identity keys included too (see the \" variant loop above).
        if '&' in en:
            esc_amp = re.sub(r'&(?!amp;|#\d+;|[a-zA-Z][a-zA-Z0-9]*;)', '&amp;', en)
            esc_amp_tr = re.sub(r'&(?!amp;|#\d+;|[a-zA-Z][a-zA-Z0-9]*;)', '&amp;', trans[en])
            if esc_amp != en and esc_amp not in trans:
                trans[esc_amp] = esc_amp_tr
            if '"' in en:
                esc_both = esc_amp.replace('"', '\\"')
                esc_both_tr = esc_amp_tr.replace('"', '\\"')
                if esc_both not in trans:
                    trans[esc_both] = esc_both_tr
    # Identity-key placeholder protection, interleaved in the main
    # longest-first pass below (not a separate earlier pass).
    # Why not just drop the `tr == en` skip in the loop: replacing a string
    # with itself is a no-op, so a shorter translated key (e.g. the beer
    # style "Hazy IPA") would still match inside a longer proper noun
    # (e.g. the brand "Northbridge Hazy IPA") afterwards. Instead, shield
    # every identity key behind a unique placeholder and restore it after
    # the loop. The shielding MUST run in the same longest-first order as
    # the translations: a longer translatable sentence (e.g. "What is
    # FreeQrly?") is translated BEFORE the shorter identity key inside it
    # ("FreeQrly") is shielded, so the sentence still matches; and the
    # identity key is shielded BEFORE any shorter translated key can match
    # inside it. A separate protect pass before the loop breaks every
    # sentence containing a short identity key (brand names like "FreeQrly",
    # "Google", "PNG" appear inside countless translatable strings).
    _PROTECT_PREFIX = "\x00__FQPROTECT_"
    assert _PROTECT_PREFIX not in src, "protect token collides with source"
    assert all(_PROTECT_PREFIX not in k for k in trans), "protect token collides with a key"
    _protect = {}  # placeholder -> original EN string
    _n = 0
    # longest first so 'Email body' wins over 'Email'
    for en in sorted(trans.keys(), key=len, reverse=True):
        tr = trans[en]
        if not en:
            continue
        if tr == en:
            # Identity key: shield it (see note above), do not translate.
            ph = f"{_PROTECT_PREFIX}{_n}\x00"
            _n += 1
            if "<" in en or " " in en:
                if out.count(en) == 0:
                    continue
                out = out.replace(en, ph)
            else:
                pat = re.compile(r"(>|['\"=])" + re.escape(en) + r"(<|['\"])")
                out, cnt = pat.subn(lambda m: m.group(1) + ph + m.group(2), out)
                if cnt == 0:
                    continue
            _protect[ph] = en
            continue
        if "<" in en or " " in en:
            n = out.count(en)
            if n == 0:
                missing.append(en)
            out = out.replace(en, tr)
        else:
            pat = re.compile(r"(>|['\"=])" + re.escape(en) + r"(<|['\"])")
            out, n = pat.subn(lambda m: m.group(1) + tr + m.group(2), out)
            if n == 0:
                missing.append(en)
    # Restore identity-key placeholders (see protect pass above). This runs
    # right after the main replacement loop and before any post-processing,
    # so the placeholders never reach the HTML rewrites below. If one
    # survived, fail loudly instead of writing a broken page.
    for ph, en in _protect.items():
        out = out.replace(ph, en)
    if _PROTECT_PREFIX in out:
        raise ValueError(f"protect placeholder leaked in {key}/{lang}")
    # Translate the lifted JSON-LD blocks, then put them back.
    #
    # Do this on the parsed object, not on the raw text: a blind string
    # replace rewrote "@type": "FAQPage" into "@type": "常见问题Page", because
    # "FAQPage" also appears as a visible string elsewhere on the page and so
    # has a translation. Schema.org types, property names and URLs are
    # structural — only human-readable values may change.
    _STRUCTURAL = {"@context", "@type", "@id", "url", "image", "logo",
                   "sameAs", "target", "cssSelector"}

    def _tr_node(node, skip=False):
        if isinstance(node, str):
            return trans.get(node, node) if not skip else node
        if isinstance(node, list):
            return [_tr_node(v, skip) for v in node]
        if isinstance(node, dict):
            return {k: _tr_node(v, skip or k in _STRUCTURAL)
                    for k, v in node.items()}
        return node

    for _i, _blk in enumerate(_jsonld):
        try:
            _obj = json.loads(_blk)
        except Exception as _exc:
            raise ValueError(f"source JSON-LD does not parse in {key}/{lang}: {_exc}")
        _new = json.dumps(_tr_node(_obj), ensure_ascii=False, indent=2)
        out = out.replace("\x00__FQJSONLD_%d\x00" % _i, _new)
    if "\x00__FQJSONLD_" in out:
        raise ValueError(f"JSON-LD placeholder leaked in {key}/{lang}")
    # Generator static fallback: elements with data-i18n="KEY" carry the
    # English label as static HTML (shown with JS off / before JS loads).
    # The dictionary never contained these strings, so the loop above
    # leaves them English on every landing page. Replace them from app.js
    # I18N — the same source the homepage generator uses
    # (build-home-i18n.py) and the same text app.js applies at runtime, so
    # static and runtime agree. Only the 33 landing pages have data-i18n
    # elements (43 each + 1 data-i18n-ph); other pages are untouched.
    # Missing keys keep the English fallback. data-i18n-ph (input
    # placeholders) likewise: drop the EN placeholder first, else the tag
    # ends up with two placeholder attributes and browsers use the first
    # (EN) one.
    _app_tr = _app_i18n().get(lang, {})
    out = re.sub(r'(<[^>]*data-i18n="([^"]+)"[^>]*>)(.*?)(</[^>]+>)',
                 lambda m: f"{m.group(1)}{_app_tr.get(m.group(2), m.group(3))}{m.group(4)}",
                 out, flags=re.S)
    def _html_escape(s):
        return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")
    def _ph_tag(m):
        tag = m.group(0)
        tag = re.sub(r'\s*placeholder="[^"]*"', '', tag)
        return re.sub(r'data-i18n-ph="([^"]+)"',
                      lambda mm: f'placeholder="{_html_escape(_app_tr.get(mm.group(1), ""))}"', tag)
    out = re.sub(r'<[^>]*data-i18n-ph="[^"]+"[^>]*>', _ph_tag, out)
    # Same for data-i18n-aria (aria-label on colour dots, upload, etc.):
    # drop the EN aria-label first, else the tag ends up with two
    # aria-label attributes. All 7 aria keys exist in all 9 languages.
    def _aria_tag(m):
        tag = m.group(0)
        tag = re.sub(r'\s*aria-label="[^"]*"', '', tag)
        return re.sub(r'data-i18n-aria="([^"]+)"',
                      lambda mm: f'aria-label="{_html_escape(_app_tr.get(mm.group(1), ""))}"', tag)
    out = re.sub(r'<[^>]*data-i18n-aria="[^"]+"[^>]*>', _aria_tag, out)
    # <html lang/data-lang/dir>
    def html_tag(m):
        attrs = m.group(1) or ""
        attrs = re.sub(r'\s+lang="[^"]*"', "", attrs)
        attrs = re.sub(r'\s+data-lang="[^"]*"', "", attrs)
        attrs = re.sub(r'\s+dir="[^"]*"', "", attrs)
        extra = f' lang="{lang}" data-lang="{lang}"'
        if lang == "ar":
            extra += ' dir="rtl"'
        return f"<html{attrs}{extra}>"
    out = re.sub(r"<html([^>]*)>", html_tag, out, count=1)
    # asset paths: EN sources use depth-relative ../assets/ (correct at their
    # depth), but localized pages sit one level deeper, so ../assets would
    # resolve to /<lang>/assets -> 404 (app.js/CSS never load). Rewrite to
    # root-absolute. (EN pages untouched; bare assets/ only in root index.)
    out = re.sub(r'((?:src|href)=["\'])(?:\.\./)+assets/', r'\1/assets/', out)
    # internal links: /<localizable-path> -> /<lang>/<localizable-path>
    # (absolute https://freeqrly.com/... incl. og:url + JSON-LD "url", and
    # root-relative href="/..." / content="/..."). NOT rewritten: /dashboard/
    # (not localized), /assets/, /q/, /api/, /mcp/, /skills/, external,
    # mailto:, tel:, bare #anchors. Query + fragment preserved.
    _LOCALIZABLE = set(["google-form-qr-code", "wifi-qr-code", "vcard-qr-code",
        "batch-qr-code", "business-card-qr-code", "google-review-qr-code",
        "qr-code-with-logo", "wedding-qr-code", "instagram-qr-code",
        "real-estate-qr-code", "pdf-qr-code", "multi-link-qr-code",
        "menu-qr-code", "payment-qr-code", "youtube-qr-code",
        "whatsapp-qr-code", "tiktok-qr-code", "spotify-qr-code",
        "facebook-qr-code", "google-maps-qr-code", "bitcoin-qr-code",
        "coupon-qr-code", "app-store-qr-code", "mp3-qr-code",
        "black-friday-qr-code", "christmas-qr-code",
        "dynamic-qr-code", "ticket-qr-code",
        "freeqrly-vs-qr-tiger", "freeqrly-vs-qr-code-monkey",
        "freeqrly-vs-qr-code-generator", "qr-tiger-alternative",
        "qr-code-monkey-alternative",
        "about", "privacy", "terms", "pricing", "developers",
        "scan", "barcode-generator", "login", "reset", "blog"])
    def _loc_url(m):
        pre, url = m.group(1), m.group(2)
        mm = re.match(r'^(https://freeqrly\.com)?(/[^?#]*)([?#].*)?$', url)
        if not mm:
            return m.group(0)
        origin, path, suffix = mm.group(1) or '', mm.group(2), mm.group(3) or ''
        if path == '/':
            return pre + origin + f'/{lang}/' + suffix
        seg = path.strip('/').split('/')[0]
        if seg in _LOCALIZABLE:
            return pre + origin + f'/{lang}{path}' + suffix
        return m.group(0)
    out = re.sub(r'((?:href|content)=["\'])((?:https://freeqrly\.com)?/[^"\']*)', _loc_url, out)
    out = re.sub(r'(\"url\"\s*:\s*\")((?:https://freeqrly\.com)?/[^\"]*)', _loc_url, out)
    # hreflang + canonical: skipped for 404 (error pages get neither)
    if key == "404":
        out_path = os.path.join(SITE, out_tmpl.format(lang=lang))
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        open(out_path, "w", encoding="utf-8").write(out)
        return missing
    # noindex 页面（login/reset/dashboard）：Google 不索引，hreflang 对它们
    # 毫无作用；而英文版本身不带反向标签，留着只会让审计工具持续报
    # "missing reciprocal hreflang"。直接整块去掉。
    if re.search(r'<meta name="robots"[^>]*noindex', out):
        out = re.sub(r'(<link rel="alternate" hreflang="[^"]*"[^>]*>\n?)+', "", out)
        out_path = os.path.join(SITE, out_tmpl.format(lang=lang))
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        open(out_path, "w", encoding="utf-8").write(out)
        return missing
    block = hreflang_block(key)
    if "hreflang=" in out:
        out = re.sub(r'(<link rel="alternate" hreflang="[^"]*"[^>]*>\n?)+', block + "\n", out, count=1)
    else:
        m = re.search(r'<meta charset[^>]*>\n?', out)
        if m:
            out = out[:m.end()] + block + "\n" + out[m.end():]
    # canonical -> self
    canon = BASE + page_url(key, lang)
    if 'rel="canonical"' in out:
        out = re.sub(r'<link rel="canonical"[^>]*>', f'<link rel="canonical" href="{canon}">', out, count=1)
    else:
        out = out.replace(block.split("\n")[0], block.split("\n")[0] + f'\n<link rel="canonical" href="{canon}">', 1)
    # og:locale: EN templates ship en_US + alternates; localized pages must
    # carry their own locale as primary (same rule as build-home-i18n.py),
    # otherwise they'd inherit en_US verbatim.
    _LOCALES = {'en':'en_US','zh':'zh_CN','es':'es_ES','hi':'hi_IN','ar':'ar_AR','pt':'pt_BR','fr':'fr_FR','ru':'ru_RU','de':'de_DE','ja':'ja_JP'}
    _alts = ''.join(f'<meta property="og:locale:alternate" content="{v}">\n' for k, v in _LOCALES.items() if k != lang)
    if 'property="og:locale"' in out:
        out = re.sub(r'<meta property="og:locale" content="[^"]*">\n(?:<meta property="og:locale:alternate" content="[^"]*">\n)*',
                     f'<meta property="og:locale" content="{_LOCALES[lang]}">\n{_alts}', out, count=1)
    out_path = os.path.join(SITE, out_tmpl.format(lang=lang))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, "w", encoding="utf-8").write(out)
    return missing

def main():
    langs = sys.argv[1:] or LANGS
    for lang in langs:
        path = os.path.join(I18N_DIR, f"{lang}.json")
        if not os.path.exists(path):
            print(f"{lang}: MISSING {path}, skipped")
            continue
        data = json.load(open(path, encoding="utf-8"))
        total_missing = 0
        for key in PAGES:
            if key == "404" and key not in data and "404" not in data:
                pass
            trans = {}
            trans.update(data.get("shared", {}))
            trans.update(data.get(key, {}))
            if key in JS_PAGES:
                trans.update(data.get(JS_PAGES[key], {}))
            missing = localize_page(key, lang, trans)
            total_missing += len(missing)
        print(f"{lang}: done, {total_missing} missing total")

if __name__ == "__main__":
    main()
