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
import json, os, re, sys

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."
I18N_DIR = os.path.join(SITE, "tools/i18n")
LANGS = ["zh", "es", "hi", "ar", "pt", "fr", "ru", "de", "ja"]
BASE = "https://freeqrly.com"

# page key -> (en source relpath, localized relpath)
PAGES = {
    "login": ("login/index.html", "{lang}/login/index.html"),
    "reset": ("reset/index.html", "{lang}/reset/index.html"),
    "404": ("404.html", "{lang}/404.html"),
    "privacy": ("privacy/index.html", "{lang}/privacy/index.html"),
    "terms": ("terms/index.html", "{lang}/terms/index.html"),
    "about": ("about/index.html", "{lang}/about/index.html"),
    "scan": ("scan/index.html", "{lang}/scan/index.html"),
    "developers": ("developers/index.html", "{lang}/developers/index.html"),
    "blog-index": ("blog/index.html", "{lang}/blog/index.html"),
}
LANDING = ["google-form-qr-code", "wifi-qr-code", "vcard-qr-code", "batch-qr-code",
           "business-card-qr-code", "google-review-qr-code", "qr-code-with-logo",
           "wedding-qr-code", "instagram-qr-code", "real-estate-qr-code",
           "pdf-qr-code", "multi-link-qr-code", "menu-qr-code",
           "payment-qr-code", "youtube-qr-code", "whatsapp-qr-code"]
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
    # JSON-LD: string values appear with \" escapes (json.dumps), so the plain
    # EN string never matches inside <script type="application/ld+json">.
    # FAQ answers with <a href="..."> links stayed English in localized pages
    # for exactly this reason. Also replace the escaped variants.
    for en in list(trans.keys()):
        if '"' in en and trans[en] != en:
            esc_en = en.replace('"', '\\"')
            if esc_en not in trans:
                trans[esc_en] = trans[en].replace('"', '\\"')
    # longest first so 'Email body' wins over 'Email'
    for en in sorted(trans.keys(), key=len, reverse=True):
        tr = trans[en]
        if tr == en or not en:
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
        "whatsapp-qr-code", "about", "privacy", "terms", "developers",
        "scan", "login", "reset", "blog"])
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
