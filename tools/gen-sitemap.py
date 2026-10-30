#!/usr/bin/env python3
"""Generate sitemap.xml from the index.html files actually present in the repo.

Includes: homepage (EN + 9 languages), landing pages, blog index + posts,
about / privacy / terms / developers / scan (each EN + localized versions).
Excludes: login / reset / dashboard (functional, auth-gated), 404, API/MCP,
/q/ short links (noindex), assets, skills, and /zh/ticket-qr-code/ (the
Chinese ticket page was never approved; its directory is untracked and its
URL 404s, so it must not be listed).

lastmod comes ONLY from each page's own date value: JSON-LD dateModified
(landing pages, updated posts), else JSON-LD datePublished (blog posts),
else the comparison pages' "checked <date>" line, else a visible
"Last updated: <date>" line. Localized URLs inherit their EN source's date
(the content and its update are the same). A page with no date value gets
NO lastmod — never invented, never taken from git log (sitewide ?v= bumps
make every file look freshly modified).
"""
import os
import re

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."
BASE = "https://freeqrly.com"
LANGS = ["zh", "es", "hi", "ar", "pt", "fr", "ru", "de", "ja"]
# Top-level content dirs that are indexable (EN version at /<slug>/).
CONTENT = {
    "", "google-form-qr-code", "wifi-qr-code", "vcard-qr-code", "batch-qr-code",
    "business-card-qr-code", "google-review-qr-code", "qr-code-with-logo",
    "wedding-qr-code", "instagram-qr-code", "real-estate-qr-code",
    "pdf-qr-code", "multi-link-qr-code", "menu-qr-code",
    "payment-qr-code", "youtube-qr-code", "whatsapp-qr-code",
    "tiktok-qr-code", "spotify-qr-code", "facebook-qr-code",
    "google-maps-qr-code",
    "bitcoin-qr-code", "coupon-qr-code", "app-store-qr-code", "mp3-qr-code",
    "black-friday-qr-code", "christmas-qr-code",
    "dynamic-qr-code", "ticket-qr-code",
    "freeqrly-vs-qr-tiger", "freeqrly-vs-qr-code-monkey",
    "freeqrly-vs-qr-code-generator", "qr-tiger-alternative",
    "qr-code-monkey-alternative",
    "about", "privacy", "terms", "pricing", "developers", "scan", "barcode-generator",
}
EXCLUDE_DIRS = {"assets", "skills", "api", "functions", "tools", "login", "reset",
                 "dashboard", "node_modules", ".git"}
EXCLUDE_URLS = {"/zh/ticket-qr-code/"}

MONTHS = {name: f"{i:02d}" for i, name in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}


def long_to_iso(s):
    m = re.match(r"([A-Za-z]+) (\d{1,2}), (\d{4})$", s.strip())
    if not m or m.group(1) not in MONTHS:
        return None
    return f"{m.group(3)}-{MONTHS[m.group(1)]}-{int(m.group(2)):02d}"


_date_cache = {}


def page_date(rel):
    """A page's own date value (ISO), or None when the page has none."""
    if rel in _date_cache:
        return _date_cache[rel]
    try:
        html = open(os.path.join(SITE, rel), encoding="utf-8").read()
    except OSError:
        html = ""
    d = None
    m = re.search(r'"dateModified"\s*:\s*"(\d{4}-\d{2}-\d{2})"', html)
    if m:
        d = m.group(1)
    else:
        m = re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})"', html)
        if m:
            d = m.group(1)
        else:
            m = re.search(r'checked ([A-Z][a-z]+ \d{1,2}, \d{4})', html)
            if m:
                d = long_to_iso(m.group(1))
            else:
                m = re.search(r'Last updated: ([A-Z][a-z]+ \d{1,2}, \d{4})', html)
                if m:
                    d = long_to_iso(m.group(1))
    _date_cache[rel] = d
    return d


def collect():
    """url path -> EN source relpath (EN source carries the date)."""
    urls = {}
    for root, dirs, files in os.walk(SITE):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]
        if "index.html" not in files:
            continue
        rel = os.path.relpath(os.path.join(root, "index.html"), SITE)
        parts = rel.split(os.sep)[:-1]  # drop index.html
        if not parts:
            urls["/"] = "index.html"
            continue
        if parts[0] in LANGS:
            rest = parts[1:]
            if rest == []:
                urls[f"/{parts[0]}/"] = "index.html"
            elif rest[0] == "blog":
                urls["/" + "/".join(parts) + "/"] = "blog/" + "/".join(rest[1:]) + "/index.html"
            elif rest[0] in CONTENT:
                urls["/" + "/".join(parts) + "/"] = rest[0] + "/index.html"
            continue
        if parts[0] == "blog":
            urls["/" + "/".join(parts) + "/"] = rel
        elif parts[0] in CONTENT:
            urls["/" + "/".join(parts) + "/"] = rel
    for u in EXCLUDE_URLS:
        urls.pop(u, None)
    return urls


def main():
    urls = collect()
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    n_dated = 0
    for u in sorted(urls, key=lambda u: (u != "/", u)):
        lm = page_date(urls[u])
        if lm:
            lines.append(f"  <url><loc>{BASE}{u}</loc><lastmod>{lm}</lastmod></url>")
            n_dated += 1
        else:
            lines.append(f"  <url><loc>{BASE}{u}</loc></url>")
    lines.append("</urlset>")
    out = os.path.join(SITE, "sitemap.xml")
    open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"sitemap.xml: {len(urls)} URLs, {n_dated} with lastmod")


if __name__ == "__main__":
    main()
