#!/usr/bin/env python3
"""Verify localized pages: no leftover EN (where tr != en), correct html attrs,
hreflang set (11 links), self canonical. Usage: verify-localized.py [lang ...]"""
import json, os, re, sys
SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."
I18N_DIR = os.path.join(SITE, "tools/i18n")
LANGS = ["zh", "es", "hi", "ar", "pt", "fr", "ru", "de", "ja"]
BASE = "https://freeqrly.com"
sys.path.insert(0, os.path.join(SITE, "tools"))
from localize_pages import PAGES, JS_PAGES, page_url

def bounded_left(en, out):
    """Mirror the replacer's matching: plain substring for long/tagged strings,
    HTML/quote-bounded match for short bare strings."""
    if "<" in en or " " in en:
        return en in out
    return re.search(r"(>|['\"=])" + re.escape(en) + r"(<|['\"])", out) is not None

TAG_COUNT = ["a ", "code", "span", "button", "option", "strong", "em", "b ", "small", "li", "p ", "h1", "h2", "h3", "data-i18n"]

def check(lang):
    data = json.load(open(os.path.join(I18N_DIR, f"{lang}.json"), encoding="utf-8"))
    problems = []
    for key in PAGES:
        src_rel, out_tmpl = PAGES[key]
        out_path = os.path.join(SITE, out_tmpl.format(lang=lang))
        if not os.path.exists(out_path):
            problems.append(f"{key}: MISSING FILE")
            continue
        out = open(out_path, encoding="utf-8").read()
        trans = {}
        trans.update(data.get("shared", {}))
        trans.update(data.get(key, {}))
        if key in JS_PAGES:
            trans.update(data.get(JS_PAGES[key], {}))
        # leftover EN (replacer-equivalent matching)
        for en, tr in trans.items():
            if tr == en or not en:
                continue
            if bounded_left(en, out):
                problems.append(f"{key}: LEFTOVER EN: {en[:90]}")
        # html attrs
        m = re.search(r"<html([^>]*)>", out)
        attrs = m.group(1) if m else ""
        if f'lang="{lang}"' not in attrs or f'data-lang="{lang}"' not in attrs:
            problems.append(f"{key}: BAD html attrs: {attrs[:120]}")
        if (lang == "ar") != ('dir="rtl"' in attrs):
            problems.append(f"{key}: dir=rtl mismatch (ar={lang == 'ar'})")
        if key != "404":
            if out.count("hreflang=") != 11:
                problems.append(f"{key}: hreflang count {out.count('hreflang=')} != 11")
            canon = BASE + page_url(key, lang)
            if f'<link rel="canonical" href="{canon}">' not in out:
                problems.append(f"{key}: canonical missing/wrong")
        # structural: tag counts must match EN source (translations preserve tags)
        src = open(os.path.join(SITE, src_rel), encoding="utf-8").read()
        for tag in TAG_COUNT:
            if tag == "li":
                a = len(re.findall(r"<li[ >]", src)); b = len(re.findall(r"<li[ >]", out))
            else:
                a, b = src.count("<" + tag), out.count("<" + tag)
            if a != b:
                problems.append(f"{key}: TAG COUNT {tag.strip()}: EN={a} vs {lang}={b}")
    return problems

def main():
    langs = sys.argv[1:] or LANGS
    bad = 0
    for lang in langs:
        probs = check(lang)
        bad += len(probs)
        print(f"{lang}: {len(probs)} problems")
        for p in probs[:25]:
            print(f"  - {p}")
    print("TOTAL:", bad)

if __name__ == "__main__":
    main()
