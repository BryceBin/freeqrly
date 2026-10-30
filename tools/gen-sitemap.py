#!/usr/bin/env python3
"""Generate sitemap.xml from the index.html files actually present in the repo.

Includes: homepage (EN + 9 languages), landing pages, blog index + posts,
about / privacy / terms / developers / scan (each EN + localized versions).
Excludes: login / reset / dashboard (functional, auth-gated), 404, API/MCP,
/q/ short links (noindex), assets, skills.
"""
import os

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


def collect():
    urls = set()
    for root, dirs, files in os.walk(SITE):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]
        if "index.html" not in files:
            continue
        rel = os.path.relpath(os.path.join(root, "index.html"), SITE)
        parts = rel.split(os.sep)[:-1]  # drop index.html
        if not parts:
            urls.add("/")
            continue
        if parts[0] in LANGS:
            rest = parts[1:]
            if rest == []:
                urls.add(f"/{parts[0]}/")
            elif rest[0] == "blog":
                urls.add("/" + "/".join(parts) + "/")
            elif rest[0] in CONTENT:
                urls.add("/" + "/".join(parts) + "/")
            continue
        if parts[0] == "blog":
            urls.add("/" + "/".join(parts) + "/")
        elif parts[0] in CONTENT:
            urls.add("/" + "/".join(parts) + "/")
    return urls


def main():
    urls = sorted(collect(), key=lambda u: (u != "/", u))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        lines.append(f"  <url><loc>{BASE}{u}</loc></url>")
    lines.append("</urlset>")
    out = os.path.join(SITE, "sitemap.xml")
    open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"sitemap.xml: {len(urls)} URLs")


if __name__ == "__main__":
    main()
