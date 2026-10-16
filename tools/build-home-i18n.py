#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate static multilingual homepages: /zh/, /es/, etc.
Replaces data-i18n elements with translated static text for SEO."""
import os, re, json, subprocess

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."

def html_escape(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")

# Get I18N via node
js = subprocess.run(["node", "-e", """
const fs=require('fs');
const app=fs.readFileSync('assets/js/app.js','utf8');
// String-aware brace counting: I18N grows as keys are added, so hardcoded
// line slices (previously lines 6-88) silently truncate it. Never slice.
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
I18N = json.loads(js.stdout)

template = open(os.path.join(SITE, "index.html"), encoding="utf-8").read()

LANGS = ['zh','es','hi','ar','pt','fr','ru','de','ja']  # en is the root

for lang in LANGS:
    tr = I18N[lang]
    h = template

    # Set html lang and dir
    bcp = {'zh':'zh-CN','es':'es','hi':'hi','ar':'ar','pt':'pt','fr':'fr','ru':'ru','de':'de','ja':'ja'}[lang]
    h = re.sub(r'<html lang="[^"]*"', f'<html lang="{bcp}" data-lang="{lang}"', h)
    if lang == 'ar':
        h = h.replace('<html lang="ar"', '<html lang="ar" dir="rtl"')

    # Replace data-i18n elements with static text
    # Pattern: <tag ... data-i18n="key">...</tag> -> <tag ...>translated</tag>
    def repl(m):
        tag_open, key, old_text, tag_close = m.groups()
        new_text = tr.get(key, old_text)
        # Keep data-i18n attribute for JS (it will re-apply, harmless)
        return f"{tag_open}{new_text}{tag_close}"

    # Handle elements with data-i18n (both <tag data-i18n="k">text</tag> and self-closing handled separately)
    h = re.sub(r'(<[^>]*data-i18n="([^"]+)"[^>]*>)(.*?)(</[^>]+>)',
               lambda m: f"{m.group(1)}{tr.get(m.group(2), m.group(3))}{m.group(4)}",
               h, flags=re.S)

    # Handle input placeholders with data-i18n-ph. The tag already carries
    # an EN placeholder="..." — drop it first, else the tag ends up with
    # TWO placeholder attributes and browsers use the first (EN) one.
    def _ph_tag(m):
        tag = m.group(0)
        tag = re.sub(r'\s*placeholder="[^"]*"', '', tag)
        return re.sub(r'data-i18n-ph="([^"]+)"',
                      lambda mm: f'placeholder="{html_escape(tr.get(mm.group(1), ""))}"', tag)
    h = re.sub(r'<[^>]*data-i18n-ph="[^"]+"[^>]*>', _ph_tag, h)

    # Update title and meta description
    h = re.sub(r'<title>.*?</title>', f"<title>{html_escape(tr.get('title', ''))}</title>", h)
    h = re.sub(r'<meta name="description" content=".*?"',
               f'<meta name="description" content="{html_escape(tr.get("metaDesc", ""))}"', h)

    # Update canonical and hreflang
    h = re.sub(r'<link rel="canonical" href="[^"]*"',
               f'<link rel="canonical" href="https://freeqrly.com/{lang}/"', h)
    # hreflang: point to language subdirectories
    for l in ['en','zh','es','hi','ar','pt','fr','ru','de','ja']:
        url = "https://freeqrly.com/" if l == 'en' else f"https://freeqrly.com/{l}/"
        h = re.sub(f'hreflang="{l}" href="[^"]*"', f'hreflang="{l}" href="{url}"', h)

    # og:locale: primary must be this page's locale (was copied as en_US);
    # alternates = all 10 locales except self
    _locales = {'en':'en_US','zh':'zh_CN','es':'es_ES','hi':'hi_IN','ar':'ar_AR','pt':'pt_BR','fr':'fr_FR','ru':'ru_RU','de':'de_DE','ja':'ja_JP'}
    _alts = ''.join(f'<meta property="og:locale:alternate" content="{v}">\n' for k, v in _locales.items() if k != lang)
    h = re.sub(r'<meta property="og:locale" content="[^"]*">\n(?:<meta property="og:locale:alternate" content="[^"]*">\n)*',
               f'<meta property="og:locale" content="{_locales[lang]}">\n{_alts}', h, count=1)

    # Fix asset paths: relative -> absolute (page lives in /{lang}/)
    h = re.sub(r'((?:href|src)=")assets/', r'\1/assets/', h)

    # Write to /{lang}/index.html
    outdir = os.path.join(SITE, lang)
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, "index.html"), "w", encoding="utf-8").write(h)
    print(f"Wrote /{lang}/ ({len(h)} bytes)")



print("Done!")
