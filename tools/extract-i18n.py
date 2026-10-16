#!/usr/bin/env python3
"""Extract user-visible strings from EN pages for translation.

Output: tools/i18n/extract/shared.en.json (strings in 2+ pages)
        tools/i18n/extract/<page>.en.json (page-specific strings)
        tools/i18n/extract/<page>.js.en.json (user-visible JS strings, login/reset/scan)
Rules: block-level innerHTML (keeps whole sentences incl. links), skip
data-i18n elements (translated by app.js at runtime), skip code/pre,
skip script/style except ld+json string values.
"""
import re, json, os, sys
from html.parser import HTMLParser
from collections import Counter, OrderedDict

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."
OUT = os.path.join(SITE, "tools/i18n/extract")
BLOCKS = {"p", "h1", "h2", "h3", "h4", "li", "button", "label", "title",
          "figcaption", "td", "th", "dt", "dd", "small", "summary", "a", "option"}
SKIP_TAGS = {"script", "style", "pre"}

def clean_ws(s):
    return " ".join(s.split())

def visible_text(html_fragment):
    t = re.sub(r"<[^>]+>", " ", html_fragment)
    t = clean_ws(t)
    return t

def junk(t):
    if len(t) < 2:
        return True
    if re.fullmatch(r"[\d\s→←·•✓✕×+*/<>=(){}\[\]|\\\-_.,:;!?&;#'\"…]+", t):
        return True
    if re.fullmatch(r"https?://\S+|www\.\S+|[\w.+-]+@[\w-]+\.[\w.]+", t):
        return True
    if re.fullmatch(r"[A-Z0-9_]{2,}|[a-z0-9_-]{1,30}", t) and " " not in t and not any(c.isalpha() for c in t):
        return True
    if t in ("theme", "website", "GET", "POST", "Free", "Qrly", "404", "© 2026 FreeQrly"):
        return True
    return False

class P(HTMLParser):
    """Collect innerHTML of blocks that contain NO nested block element.
    <a>/<span>/<em>/<strong>/<br>/<small>/<code> are inline (kept as tags).
    Blocks with block children are discarded; their children are units."""
    BLOCKS = {"p", "h1", "h2", "h3", "h4", "li", "button", "label", "title",
              "figcaption", "td", "th", "dt", "dd", "summary", "option",
              "div", "nav", "footer", "section", "article", "header", "main",
              "aside", "figure", "blockquote", "details", "cite"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.strings = []
        self.skip_depth = 0
        self.stack = []  # [tag, inner_html_parts, has_block_child, has_i18n]

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if tag == "meta":
            ad = dict(attrs)
            if ad.get("name") == "description" or ad.get("property") in ("og:title", "og:description", "twitter:title", "twitter:description"):
                if ad.get("content"):
                    self.strings.append(ad["content"].strip())
            return
        if tag in ("input", "img"):
            ad = dict(attrs)
            for k in ("placeholder", "alt", "aria-label"):
                if ad.get(k, "").strip():
                    self.strings.append(ad[k].strip())
            return
        if tag == "html":
            return
        if "data-i18n" in dict(attrs):
            for f in self.stack:
                f[3] = True
        # record raw tag into all open frames
        raw = self.get_starttag_text()
        for f in self.stack:
            f[1].append(raw)
        if tag in self.BLOCKS:
            # mark parent frames as having a block child
            for f in self.stack:
                f[2] = True
            self.stack.append([tag, [], False, "data-i18n" in dict(attrs)])
        elif tag == "br":
            for f in self.stack:
                f[1].append(" ")

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if tag in self.BLOCKS and self.stack and self.stack[-1][0] == tag:
            _, parts, has_child, has_i18n = self.stack.pop()
            raw = self.get_starttag_text()
            for f in self.stack:
                f[1].append(f"</{tag}>")
            if not has_child and not has_i18n:
                t = clean_ws("".join(parts))
                if "<svg" in t:
                    t = visible_text(t)
                if t and not junk(visible_text(t)) and visible_text(t):
                    self.strings.append(t)
        elif self.stack:
            for f in self.stack:
                f[1].append(f"</{tag}>")

    def handle_data(self, data):
        if self.skip_depth:
            return
        for f in self.stack:
            f[1].append(data)

def extract_html(path):
    s = open(path, encoding="utf-8").read()
    p = P()
    p.feed(s)
    out = []
    for t in p.strings:
        if t not in out and not junk(visible_text(t)):
            out.append(t)
    # JSON-LD string values
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            data = json.loads(m.group(1))
        except Exception:
            continue
        def walk(o):
            if isinstance(o, dict):
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
            elif isinstance(o, str) and " " in o and len(o) > 3 and not o.startswith("http"):
                if o not in out and not junk(o):
                    out.append(o)
        walk(data)
    return out

JS_KEEP = re.compile(r"[A-Za-z]{3,}")

def extract_js(path):
    s = open(path, encoding="utf-8").read()
    scripts = re.findall(r"<script>(.*?)</script>", s, re.S)
    out = []
    for js in scripts:
        for pat in (r'"([^"\n]{4,160})"', r"'([^'\n]{4,160})'", r"`([^`\n]{4,160})`"):
         for m in re.finditer(pat, js):
            t = m.group(1)
            if not JS_KEEP.search(t):
                continue
            if re.search(r"^(https?://|/api|/|\.|#|function|return|const |let |var |if \(|===|!==|=>|addEvent|querySel|getElement|localStorage|sessionStorage|JSON\.|fetch\()", t):
                continue
            if any(x in t for x in ("function", "${", "document.", "window.", "style.", "classList",
                                   "textContent", "innerHTML", "addEventListener", "querySelector",
                                   "getElementById", "application/json", "Content-Type", "same-origin",
                                   "turnstile_failed", "aria-", "current-password", "new-password",
                                   "text/vcard", "prefers-color-scheme", "freeqrly-theme", "data-theme",
                                   "dontInvert", "environment", "noopener", "scan_", "pagehide")):
                continue
            if t not in out and (re.search(r'[A-Za-z] [A-Za-z]', t) or t in (
                    'Log in', 'Create account', 'Logging in…', 'Creating account…',
                    'Sending…', 'Updating…', 'Send reset link', 'Update password',
                    'Choose a new password', 'Camera unavailable: ', 'Start camera',
                    'Stop', 'Upload image', 'Copy', 'Open link', 'Scan another')):
                out.append(t)
    return out

PAGES = {
    "login": "login/index.html",
    "reset": "reset/index.html",
    "404": "404.html",
    "privacy": "privacy/index.html",
    "terms": "terms/index.html",
    "about": "about/index.html",
    "scan": "scan/index.html",
    "developers": "developers/index.html",
    "blog-index": "blog/index.html",
}
# landing + blog posts from generated EN pages
LANDING = ["google-form-qr-code", "wifi-qr-code", "vcard-qr-code", "batch-qr-code",
           "business-card-qr-code", "google-review-qr-code", "qr-code-with-logo",
           "wedding-qr-code", "instagram-qr-code", "real-estate-qr-code"]
for d in LANDING:
    PAGES[f"landing-{d}"] = f"{d}/index.html"
for d in sorted(os.listdir(os.path.join(SITE, "blog"))):
    if os.path.isdir(os.path.join(SITE, "blog", d)):
        PAGES[f"blog-{d}"] = f"blog/{d}/index.html"

def main():
    os.makedirs(OUT, exist_ok=True)
    per_page = {}
    for key, rel in PAGES.items():
        per_page[key] = extract_html(os.path.join(SITE, rel))
    counts = Counter()
    for strs in per_page.values():
        for t in set(strs):
            counts[t] += 1
    shared = sorted([t for t, c in counts.items() if c >= 2])
    json.dump(shared, open(os.path.join(OUT, "shared.en.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"shared: {len(shared)}")
    for key, strs in per_page.items():
        own = [t for t in strs if counts[t] < 2]
        json.dump(own, open(os.path.join(OUT, f"{key}.en.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"{key}: {len(own)} (+{len(strs) - len(own)} shared)")
    for key in ("login", "reset", "scan"):
        js = extract_js(os.path.join(SITE, PAGES[key]))
        json.dump(js, open(os.path.join(OUT, f"{key}.js.en.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"{key}.js: {len(js)}")

if __name__ == "__main__":
    main()
