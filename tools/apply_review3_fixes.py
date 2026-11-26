#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Third-pass fixes, applied to the live strings a native reviewer flagged.

Same shape as apply_review_fixes.py: (lang, page, needle, replacement), plus
whole-value SETS for strings where a needle would be ambiguous. Rules are
idempotent — a needle may not be a substring of its own replacement — so the
script can be re-run safely after a rebuild.
"""
import json
import os
import re
import sys

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."
LANGS = ["zh", "ja", "de", "es", "fr", "pt", "ru", "hi", "ar"]

TAG_LONG = "Made quietly — static codes in your browser."

# The footer tagline exists twice in each table — once under "shared" (used by
# the landing pages) and once under "about" — with different wording, so the
# same sentence read differently depending on the page. Unify on the "about"
# version, which keeps both "quietly" and "static codes".
UNIFY_TAGLINE = True

FIXES = [
    # ---------- German ----------
    ("de", "about", "nicht auf dem Server von irgendwem",
     "nicht auf den Server von jemand anderem"),
    ("de", "landing-app-store-qr-code", "QR-Codes im Batch", "QR-Codes im Stapel"),
    ("de", "landing-app-store-qr-code", "eine Weiterleitung, die feuert,",
     "eine Weiterleitung, die ausgelöst wird,"),
    ("de", "landing-app-store-qr-code", "ist größer sicherer",
     "ist ein größerer Code sicherer"),
    ("de", "landing-app-store-qr-code", "Ein Code auf eine Router-Seite",
     "Ein Code, der auf eine Weiterleitungsseite zeigt"),

    # ---------- Spanish ----------
    ("es", "landing-app-store-qr-code", "Pie del ticket", "Pie del recibo"),
    ("es", "landing-app-store-qr-code", "detecta el user agent",
     "detecta el agente de usuario"),
    ("es", "landing-app-store-qr-code", "Generador de QR App Store:",
     "Generador de QR para App Store:"),
    ("es", "landing-app-store-qr-code", "Bueno saberlo", "Conviene saberlo"),
    ("es", "about", "se escanea dentro de diez años",
     "se seguirá escaneando dentro de diez años"),
    ("es", "landing-app-store-qr-code", "Un código a una página enrutadora",
     "Un código hacia una página enrutadora"),
    ("es", "landing-app-store-qr-code", "sin «iPhone» y «Android»",
     "sin “iPhone” y “Android”"),
    ("es", "landing-app-store-qr-code", "aloja una pequeña página de redirección",
     "aloja una pequeña página enrutadora"),

    # ---------- French ----------
    ("fr", "landing-app-store-qr-code", "Pubs, emballages, tickets, visuels",
     "Pubs, emballages, reçus, visuels"),
    ("fr", "landing-app-store-qr-code", "Préréglages fêtes", "Préréglages de fêtes"),
    ("fr", "landing-ticket-qr-code", "marge de silence", "zone de silence"),
    ("fr", "landing-app-store-qr-code", "une petite page de redirection",
     "une petite page routeur"),
    ("fr", "landing-app-store-qr-code", "pour app store",
     "pour boutique d’applications"),

    # ---------- Portuguese ----------
    ("pt", "landing-app-store-qr-code", "Rodapé do cupom", "Rodapé do recibo"),
    ("pt", "landing-app-store-qr-code", "detecta o user agent",
     "detecta o agente de usuário"),
    ("pt", "landing-app-store-qr-code", "Gerador de QR code App Store:",
     "Gerador de QR code para App Store:"),
    ("pt", "landing-app-store-qr-code", "página de redirecionamento",
     "página roteadora"),
    ("pt", "landing-ticket-qr-code", "margem de silêncio", "zona de silêncio"),
    ("pt", "landing-ticket-qr-code", "marca-d'água", "marca d'água"),
    ("pt", "about", "escaneia daqui a dez anos", "vai escanear daqui a dez anos"),
    ("pt", "landing-ticket-qr-code", "um código que lê de primeira",
     "um código que escaneia de primeira"),
    ("pt", "landing-app-store-qr-code", "fichas de iOS e Android",
     "páginas de iOS e Android"),

    # ---------- Russian ----------
    ("ru", "landing-app-store-qr-code", "Умный баннер магазинов",
     "Смарт-баннер магазина"),
    ("ru", "landing-app-store-qr-code", "Слайд к запуску приложения",
     "Слайд запуска приложения"),
    ("ru", "landing-app-store-qr-code", "если знать где", "если знать, где искать"),
    ("ru", "landing-app-store-qr-code", "мягче, чем мгновенный переход",
     "удобнее, чем мгновенный переход"),
    ("ru", "about", "ничего не загружается, не отслеживается и не оплачивается",
     "ничего не загружается и не отслеживается, и с вас не берут денег"),

    # ---------- Arabic ----------
    ("ar", "landing-ticket-qr-code", "نموذج تسجيل دخول", "نموذج تسجيل الحضور"),
    ("ar", "about", "رموز QR بالجملة", "رموز QR بالدفعات"),
    ("ar", "about", "رهينة وراء تجربة", "رهينة وراء فترة تجريبية"),
    ("ar", "landing-app-store-qr-code", "صفحتا iOS وأندرويد",
     "صفحتا iOS وAndroid"),
    ("ar", "about", "تعيش في النقش نفسه", "تعيش في النمط نفسه"),
    ("ar", "landing-app-store-qr-code", "لا يوجد داخل النقش", "لا يوجد داخل النمط"),

    # ---------- Japanese ----------
    ("ja", "landing-app-store-qr-code", "ロジックは短いです", "ロジックはシンプルです"),
    ("ja", "landing-app-store-qr-code", "レシート、発表スライドに。",
     "レシート、発表スライドなどに使えます。"),
    ("ja", "landing-ticket-qr-code", "学校行事に。", "学校行事などに使えます。"),
    ("ja", "landing-app-store-qr-code", "1〜2mで読む", "1〜2m離れて読み取る"),
    ("ja", "landing-app-store-qr-code", "2〜3mから読む", "2〜3mから読み取る"),

    # ---------- Chinese ----------
    ("zh", "landing-app-store-qr-code", "逻辑很短", "逻辑很简单"),
    ("zh", "landing-app-store-qr-code", "不会。静态码只带着链接", "不能。静态码只带着链接"),
    ("zh", "about", "FreeQrly是什么？", "FreeQrly 是什么？"),
    ("zh", "landing-app-store-qr-code", "App Store 上架页和 Play 上架页",
     "App Store 商店页和 Play 商店页"),
    ("zh", "landing-ticket-qr-code", "购票页或签到页", "门票页或签到页"),
    ("zh", "landing-ticket-qr-code", "活动改期时，", "活动有变动（改期或换场地）时，"),

    # ---------- Hindi ----------
    ("hi", "landing-app-store-qr-code", "स्थिर", "स्टैटिक"),
    ("hi", "landing-app-store-qr-code", "गतिशील", "डायनामिक"),
    ("hi", "about", "डायनैमिक", "डायनामिक"),
    ("hi", "about", "डायनेमिक", "डायनामिक"),
    ("hi", "landing-ticket-qr-code", "डायनेमिक", "डायनामिक"),
    ("hi", "about", "FreeQrlyक्या है?", "FreeQrly क्या है?"),
    ("hi", "landing-app-store-qr-code",
     "स्टैटिक कोड में सिर्फ लिंक होता है और वे कुछ भी वापस नहीं भेजते।",
     "स्टैटिक कोड में सिर्फ लिंक होता है और वह कुछ भी वापस नहीं भेजता।"),
    ("hi", "landing-ticket-qr-code", "एक कोड, एक डेस्टिनेशन",
     "एक कोड, एक गंतव्य"),
    ("hi", "landing-app-store-qr-code", "जो user agent पढ़कर",
     "जो यूज़र एजेंट पढ़कर"),
    ("hi", "landing-ticket-qr-code", "किससे लिंक होना चाहिए?",
     "किस पेज से लिंक होना चाहिए?"),
    ("hi", "landing-app-store-qr-code", "विज्ञापन, पैकेजिंग, रसीद, लॉन्च स्लाइड।",
     "विज्ञापन, पैकेजिंग, रसीद और लॉन्च स्लाइड के लिए।"),
    ("hi", "landing-ticket-qr-code", "वर्कशॉप, स्कूल इवेंट।",
     "वर्कशॉप और स्कूल इवेंट के लिए।"),
]

# Whole-value replacements (key -> new value), by language.
SETS = {
    "de": {
        "landing-app-store-qr-code": {
            "Ein Tipp: Tinte, Papier & Rahmen": "Ein Fingertipp: Tinte, Papier & Rahmen",
        },
    },
}


def apply(lang, page, needle, repl, dry):
    """Search every bucket of the language, not just `page`.

    localize_pages merges the "shared" bucket into each page's table, so a
    string that renders on the app-store page may physically live under
    "shared" — scoping the search to one page silently misses those.
    """
    path = os.path.join(SITE, "tools/i18n", lang + ".json")
    table = json.load(open(path, encoding="utf-8"))
    if needle in repl and needle != repl:
        return f"{lang}/{page}: 规则不幂等 → {needle[:30]}"
    hits = 0
    for bucket in table.values():
        if not isinstance(bucket, dict):
            continue
        for key, val in list(bucket.items()):
            if needle in val:
                bucket[key] = val.replace(needle, repl)
                hits += 1
    if not hits:
        for bucket in table.values():
            if isinstance(bucket, dict) and any(repl in v for v in bucket.values()):
                return None
        return f"{lang}/{page}: 找不到 “{needle[:40]}”"
    if not dry:
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(table, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    return None


def main():
    dry = "--dry-run" in sys.argv
    problems = []
    for lang, page, needle, repl in FIXES:
        err = apply(lang, page, needle, repl, dry)
        if err:
            problems.append(err)
    for lang, pages in SETS.items():
        path = os.path.join(SITE, "tools/i18n", lang + ".json")
        table = json.load(open(path, encoding="utf-8"))
        for page, pairs in pages.items():
            for old, new in pairs.items():
                hits = [k for k, v in table.get(page, {}).items() if old in v]
                for k in hits:
                    table[page][k] = table[page][k].replace(old, new)
        if not dry:
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(table, fh, ensure_ascii=False, indent=1)
                fh.write("\n")
    if UNIFY_TAGLINE:
        for lang in LANGS:
            path = os.path.join(SITE, "tools/i18n", lang + ".json")
            table = json.load(open(path, encoding="utf-8"))
            src = table.get("about", {}).get(TAG_LONG)
            shared = table.get("shared")
            if not src or not shared or TAG_LONG not in shared:
                problems.append(f"{lang}: 页脚标语无法统一")
                continue
            if shared[TAG_LONG] != src:
                shared[TAG_LONG] = src
                if not dry:
                    with open(path, "w", encoding="utf-8") as fh:
                        json.dump(table, fh, ensure_ascii=False, indent=1)
                        fh.write("\n")
    if problems:
        print(f"{len(problems)} 处未能应用：")
        for p in problems:
            print("  ", p)
    else:
        print(f"全部 {len(FIXES)} 处 + 页脚统一{'（演练）' if dry else ''}")


if __name__ == "__main__":
    main()
