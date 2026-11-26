#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render a translation table for review: EN string above, translation below.

Used to hand a reviewer a compact, readable file instead of raw JSON, and to
catch the mechanical problems automatically so a human (or reviewing agent)
only has to judge the language itself.

Usage:
    python3 tools/review_i18n.py zh            # one language, stdout
    python3 tools/review_i18n.py zh --write    # -> tools/i18n/review/zh.md

Automatic checks per string:
  - HTML tag counts match the source
  - the translation is not identical to the English (untranslated)
  - the translation is not mostly Latin text for a non-Latin language
  - title length (<= 60 chars) and description length (120-160 chars)
    for strings that look like a <title> or a meta description
"""
import json
import os
import re
import sys

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."
EXTRACT = os.path.join(SITE, "tools/i18n/extract")
TAGS = ("<span", "</span>", "<b>", "</b>", "<code>", "</code>")
LATIN_SCRIPT = {"de", "es", "fr", "pt"}
NON_LATIN = {"zh", "ja", "ru", "hi", "ar"}


def load(lang):
    return json.load(open(os.path.join(SITE, "tools/i18n", lang + ".json"), encoding="utf-8"))


def _meta_descriptions():
    """The exact EN strings used in <meta name="description"> on the pages
    being reviewed. Only these get a length rule — body paragraphs start with
    the same words and are not subject to it."""
    out = set()
    for rel in ("app-store-qr-code/index.html", "about/index.html",
                "ticket-qr-code/index.html"):
        path = os.path.join(SITE, rel)
        if not os.path.exists(path):
            continue
        m = re.search(r'<meta name="description" content="([^"]*)"',
                      open(path, encoding="utf-8").read())
        if m:
            out.add(m.group(1))
    return out


META_DESCRIPTIONS = _meta_descriptions()


def check(lang, en, tr):
    out = []
    for tag in TAGS:
        if en.count(tag) != tr.count(tag):
            out.append(f"标签 {tag} 数量 {en.count(tag)}→{tr.count(tag)}")
    if en.strip() == tr.strip():
        out.append("未翻译（与英文相同）")
    if lang in NON_LATIN:
        latin = len(re.findall(r"[A-Za-z]", tr))
        other = len(re.findall(r"[^\x00-\x7F]", tr))
        # Brand names and code samples are legitimately Latin; only flag when
        # the string is essentially English.
        if latin > 20 and other == 0:
            out.append("疑似未翻译（全拉丁字符）")
    plain = re.sub(r"<[^>]+>", "", tr)
    if "| FreeQrly" in tr and len(plain) > 60:
        out.append(f"标题过长 {len(plain)} 字符")
    if en in META_DESCRIPTIONS:
        # CJK packs ~2× the information per character, so the Latin 120–160
        # rule does not apply; the site's own zh pages run 60–76 and ja 95–98.
        lo, hi = (55, 100) if lang in ("zh", "ja") else (110, 165)
        if not (lo <= len(plain) <= hi):
            out.append(f"描述长度 {len(plain)}（建议 {lo}–{hi}）")
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write = "--write" in sys.argv
    langs = args or ["zh", "ja", "de", "es", "fr", "pt", "ru", "hi", "ar"]
    for lang in langs:
        table = load(lang)
        lines = [f"# {lang}\n"]
        issues = 0
        for page in ("landing-app-store-qr-code", "about", "landing-ticket-qr-code"):
            pairs = table.get(page)
            if not pairs:
                continue
            ext_path = os.path.join(EXTRACT, page + ".en.json")
            if not os.path.exists(ext_path):
                continue
            order = json.load(open(ext_path, encoding="utf-8"))
            lines.append(f"\n## {page}\n")
            for en in order:
                if en not in pairs:
                    continue
                tr = pairs[en]
                bad = check(lang, en, tr)
                if bad:
                    issues += 1
                    lines.append(f"⚠️ {', '.join(bad)}")
                lines.append(f"EN: {en}")
                lines.append(f"→  {tr}\n")
        text = "\n".join(lines)
        if write:
            outdir = os.path.join(SITE, "tools/i18n/review")
            os.makedirs(outdir, exist_ok=True)
            path = os.path.join(outdir, lang + ".md")
            open(path, "w", encoding="utf-8").write(text)
            print(f"{lang}: {issues} 个自动告警 → {path}")
        else:
            print(text)


if __name__ == "__main__":
    main()
