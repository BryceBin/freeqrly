#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply the native-review fixes to the translation tables.

Each entry is (lang, page, needle, replacement): `needle` is a fragment of the
current translation, replaced in place. Every string containing the needle is
updated — the same copy appears twice on a page, once wrapped in <span>/<b>
and once plain, and both must change.

Title fixes run first: a body rule such as "store -> boutique" would otherwise
rewrite the title before its own rule could match.

Keeping the fixes in a script (rather than hand-editing JSON) means the same
change can be re-applied after a re-extract, and every edit is auditable.
"""
import json
import os
import sys

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."

# Run before anything else.
TITLE_FIXES = [
    # The French title uses a non-breaking space before the colon.
    ("fr", "landing-app-store-qr-code",
     "Générateur de QR code App Store\xa0: un code par store | FreeQrly",
     "QR code App Store\xa0: un code par boutique | FreeQrly"),
    ("fr", "landing-ticket-qr-code",
     "Générateur gratuit de billet avec QR code | FreeQrly",
     "Générateur de QR code pour billets, gratuit | FreeQrly"),
    ("pt", "landing-ticket-qr-code",
     "Gerador de QR Code do Ingresso Grátis | FreeQrly",
     "Gerador de QR code para ingressos grátis | FreeQrly"),
    ("pt", "landing-app-store-qr-code",
     "Gerador de QR code da App Store: um código por loja | FreeQrly",
     "Gerador de QR code App Store: um código por loja | FreeQrly"),
    ("de", "about", "Über FreeQrly — Statische QR-Codes ohne Anmeldung und Ablauf",
     "Über FreeQrly — Kostenlose QR-Codes ohne Anmeldung"),
    ("fr", "about", "À propos de FreeQrly — QR codes statiques, sans inscription",
     "À propos de FreeQrly — QR codes gratuits, sans inscription"),
]

FIXES = [
    # ---------- German ----------
    ("de", "landing-ticket-qr-code", "Batch-Modus", "Stapelmodus"),
    ("de", "landing-ticket-qr-code", "mit Batch<", "mit Stapelmodus<"),
    ("de", "about", "und enthalten 20 kostenlose, mit einem",
     "und enthalten 20 kostenlose Codes, mit einem"),
    ("de", "landing-ticket-qr-code", "zeige die Seite hinter dem Code auf die neuen Details",
     "richte die Seite hinter dem Code auf die neuen Details aus"),
    ("de", "landing-app-store-qr-code", "denn ein guter Teil der Scans",
     "denn ein nicht unerheblicher Teil der Scans"),
    ("de", "landing-app-store-qr-code", "den erkannten hervorzuheben ist",
     "den erkannten hervorzuheben, ist"),
    ("de", "landing-app-store-qr-code", "auch wenn der App-Name es tut",
     "auch wenn sich der App-Name ändert"),
    ("de", "landing-app-store-qr-code", "Bon-Fußzeile", "Kassenbon-Fußzeile"),
    ("de", "landing-app-store-qr-code", "ohne „iPhone“ und „Android“",
     "ohne die Beschriftung „iPhone“ und „Android“"),
    ("de", "landing-app-store-qr-code", "Erkennt er das Handy automatisch?",
     "Erkennt er das Handy und leitet automatisch weiter?"),
    ("de", "landing-app-store-qr-code", "senden nichts nach Hause", "senden keine Daten"),
    ("de", "about", "nicht auf irgendjemandes Server", "nicht auf dem Server von irgendwem"),
    ("de", "about", "Ein unabhängiger Maker", "Ein unabhängiger Macher"),
    ("de", "landing-ticket-qr-code", "Für jedes Ticket einen anderen Code nötig?",
     "Brauchst du für jedes Ticket einen anderen Code?"),
    ("de", "landing-ticket-qr-code", "mit klarem freiem Rand",
     "mit einer klar abgegrenzten Ruhezone"),

    # ---------- Spanish ----------
    ("es", "landing-ticket-qr-code", "modo masivo", "modo lote"),
    ("es", "landing-app-store-qr-code", "slides de lanzamiento", "diapositivas de lanzamiento"),
    ("es", "landing-app-store-qr-code", "Dos códigos es la opción", "Dos códigos son la opción"),
    ("es", "landing-app-store-qr-code", "es más tolerante que reenviar",
     "funciona mejor que reenviar"),
    ("es", "about", "Sin pruebas ni códigos desactivados",
     "Sin periodos de prueba ni códigos desactivados"),
    ("es", "about", 'los generadores "gratis"', "los generadores “gratis”"),
    ("es", "landing-ticket-qr-code", "llegan directamente a tu entrada o página de registro",
     "llegan directamente a tu página de entradas o de registro"),
    ("es", "landing-ticket-qr-code", "fuente de verdad para la entrada",
     "la referencia para el acceso"),
    ("es", "landing-ticket-qr-code", "margen de silencio despejado",
     "zona de silencio despejada"),
    ("es", "landing-app-store-qr-code", "Banner inteligente de la tienda",
     "Banner inteligente de la app"),

    # ---------- French ----------
    ("fr", "landing-app-store-qr-code", "un code par store", "un code par boutique"),
    ("fr", "landing-app-store-qr-code", "lien de store", "lien de boutique"),
    ("fr", "landing-app-store-qr-code", "choisir un store", "choisir une boutique"),
    ("fr", "landing-app-store-qr-code", "le bon store", "la bonne boutique"),
    ("fr", "landing-app-store-qr-code", "les deux stores", "les deux boutiques"),
    ("fr", "landing-app-store-qr-code", "fiches de store", "fiches de boutique"),
    ("fr", "landing-app-store-qr-code", "sur 2", "sur au moins 2"),
    ("fr", "landing-app-store-qr-code", "cm minimum", "cm"),
    ("fr", "landing-app-store-qr-code", "slides de lancement", "visuels de lancement"),
    ("fr", "landing-app-store-qr-code", "sur un portable", "sur un ordinateur portable"),
    ("fr", "landing-app-store-qr-code", "plus tolérant qu", "plus robuste qu"),
    ("fr", "landing-app-store-qr-code", "Détecte-t-il le téléphone tout seul ?",
     "Détecte-t-il le téléphone et redirige-t-il automatiquement ?"),
    ("fr", "landing-ticket-qr-code", "mode Lot", "mode lot"),
    ("fr", "landing-ticket-qr-code", "Liez votre page de billet",
     "Pointez vers votre page de billet"),

    # ---------- Portuguese ----------
    ("pt", "landing-ticket-qr-code", "nunca expira.", "nunca expiram."),
    ("pt", "landing-ticket-qr-code", "modo em massa", "modo lote"),
    ("pt", "landing-ticket-qr-code", "QR Codes", "QR codes"),
    ("pt", "landing-ticket-qr-code", "QR Code", "QR code"),
    ("pt", "landing-ticket-qr-code", "sem fila de ingresso", "sem fila na entrada"),
    ("pt", "landing-ticket-qr-code", "O visitante escaneia", "O convidado escaneia"),
    ("pt", "about", "Sem testes, sem códigos desativados",
     "Sem períodos de teste, sem códigos desativados"),
    ("pt", "about", "marca d’água", "marca d'água"),
    ("pt", "about", 'geradores "grátis"', "geradores “grátis”"),
    ("pt", "landing-app-store-qr-code", "Dois códigos é a opção", "Dois códigos são a opção"),
    ("pt", "landing-app-store-qr-code", "mais tolerante do que encaminhar",
     "funciona melhor do que encaminhar"),

    # ---------- Russian ----------
    ("ru", "landing-app-store-qr-code", "слайды презентации", "слайды запуска"),
    ("ru", "landing-app-store-qr-code", "Он сам определяет телефон?",
     "Сам ли он определяет телефон и направляет в нужный магазин?"),
    ("ru", "landing-app-store-qr-code", "ваши страницы в iOS и Android — два разных URL",
     "страницы приложения в App Store и Google Play — два разных URL"),
    ("ru", "landing-app-store-qr-code", "зайдите в App Information и скопируйте URL App Store",
     "перейдите в раздел «Информация о приложении» и скопируйте URL App Store"),
    ("ru", "landing-ticket-qr-code", "один код, одно назначение",
     "один код — один адрес назначения"),
    ("ru", "landing-ticket-qr-code", "направьте страницу за кодом на новые детали",
     "направьте страницу, на которую ведёт код, на новые детали"),
    ("ru", "landing-ticket-qr-code", "а источником истины для входа пусть остаётся сама страница",
     "а точкой входа пусть остаётся сама страница"),
    ("ru", "landing-ticket-qr-code", "при экспорте от 1024 px и выше",
     "при экспорте от 1024 px"),
    ("ru", "about", "и они включают 20 бесплатно", "и включают 20 кодов бесплатно"),

    # ---------- Arabic ----------
    ("ar", "landing-ticket-qr-code", "صفحة تذكرتك أو تسجيل الدخول",
     "صفحة تذكرتك أو صفحة تسجيل الحضور"),
    ("ar", "landing-ticket-qr-code", "نموذج تسجيل الدخول", "نموذج تسجيل الحضور"),
    ("ar", "landing-app-store-qr-code", "ماذا لو كان لدي منصة واحدة فقط؟",
     "ماذا لو كانت لديّ منصة واحدة فقط؟"),
    ("ar", "about", "أسئلة، مجابة", "أسئلة وأجوبة"),
    ("ar", "about", 'المولّدات "المجانية"', "المولّدات “المجانية”"),
    ("ar", "landing-app-store-qr-code", "ويسهل العثور عليه في كليهما",
     "ويسهل العثور عليهما"),
    ("ar", "about", "والرسائل والمكالمات والمواقع", "والرسائل والمكالمات والمواقع الجغرافية"),
    ("ar", "about", "لا تجارب، لا رموز معطّلة", "لا فترات تجريبية، لا رموز معطّلة"),
    ("ar", "about", "بدون تجربة", "بدون فترة تجريبية"),
    ("ar", "landing-ticket-qr-code", "مسحة واحدة عند الباب", "مسحة واحدة عند المدخل"),
    ("ar", "landing-ticket-qr-code", "إلى ماذا يجب أن يربط رمز QR لتذكرة الفعالية؟",
     "إلى أي صفحة يجب أن يقود رمز QR الخاص بالتذكرة؟"),
    ("ar", "landing-ticket-qr-code", "أبقِ الصفحة نفسها مصدر الحقيقة للدخول",
     "أبقِ الصفحة نفسها المرجع المعتمد للدخول"),
    ("ar", "landing-ticket-qr-code", "وجّه الصفحة خلف الرمز إلى التفاصيل الجديدة",
     "وجّه الصفحة التي يفتحها الرمز إلى التفاصيل الجديدة"),
    ("ar", "landing-ticket-qr-code", "يُبقي الطابور متحركًا", "يمنع تكدّس الطابور"),
    ("ar", "landing-app-store-qr-code", "أكثر تسامحًا من التحويل الفوري",
     "أقل عرضة للخطأ من التحويل الفوري"),
    ("ar", "about", "خادم API و MCP", "واجهة API وخادم MCP"),

    # ---------- Chinese ----------
    ("zh", "landing-ticket-qr-code", "下方工作区", "下方工作室"),
    ("zh", "landing-app-store-qr-code", "报 Android，去 Play", "报安卓，去 Play"),
    ("zh", "landing-ticket-qr-code", "并留出足够的空白边距", "并留足静区"),
    ("zh", "landing-app-store-qr-code", "最诚实、也最省事", "最实在、也最省事"),
    ("zh", "landing-app-store-qr-code", "逻辑很短：", "逻辑很简单："),
    ("zh", "landing-app-store-qr-code", "App Store 或 Google Play 链接免费生成二维码。",
     "为 App Store 或 Google Play 链接免费生成二维码。"),

    # ---------- Japanese ----------
    ("ja", "about", "バッチ生成", "一括生成"),
    ("ja", "landing-ticket-qr-code", "クワイエットマージン", "クワイエットゾーン"),
    ("ja", "landing-app-store-qr-code", "これが効くのは", "これが重要なのは"),
    ("ja", "landing-app-store-qr-code", "ロジックは短いです", "ロジックはシンプルです"),
    ("ja", "landing-app-store-qr-code", "実際には2つのことで壊れます",
     "実際には、このページは2つの理由でうまく動かなくなります"),
    ("ja", "landing-app-store-qr-code", "即座に転送するより寛容です",
     "即座に転送するよりやさしいです"),
    ("ja", "landing-ticket-qr-code", "イベントが移動した場合は",
     "イベントの日程や会場が変わった場合は"),
    ("ja", "landing-ticket-qr-code", "1回で読み取れるコードが列を進めます",
     "一発で読み取れるコードなら、列が止まりません"),
    ("ja", "landing-ticket-qr-code", "無料 QRコードチケットジェネレーター",
     "無料QRコードチケットジェネレーター"),

    # ---------- Hindi ----------
    ("hi", "about", "FreeQrly के बारे में — मुफ़्त QR कोड, बिना साइन-अप, बिना एक्सपायरी",
     "FreeQrly के बारे में — मुफ़्त स्टैटिक QR कोड, बिना एक्सपायरी"),
    ("hi", "about", "स्टैटिक कोड 100% आपके ब्राउज़र में — बिना साइन-अप",
     "स्टैटिक कोड 100% आपके ब्राउज़र में चलते हैं — बिना साइन-अप"),
    ("hi", "about", "पूरे साइट पर दिखता है", "पूरी साइट पर दिखता है"),
    ("hi", "about", "उच्च-रिज़ॉल्यूशन निर्यात शामिल है",
     "हाई-रेज़ोल्यूशन एक्सपोर्ट शामिल है"),
    ("hi", "about", "क्वाइट ज़ोन का सम्मान", "क्वाइट ज़ोन बरकरार"),
    ("hi", "about", "सवाल, जवाब के साथ", "सवाल और जवाब"),
    ("hi", "landing-app-store-qr-code", "1 (आपकी साइट के लिए)", "1 (आपकी साइट पर)"),
    ("hi", "landing-app-store-qr-code", "ज़्यादा सुरक्षित है",
     "ज़्यादा बेहतर काम करता है"),
    ("hi", "landing-app-store-qr-code", "user agent पढ़कर", "यूज़र एजेंट पढ़कर"),
    ("hi", "landing-app-store-qr-code", "हां, अगर पेज डायनामिक हो",
     "हाँ, अगर पेज डायनामिक हो"),
    ("hi", "about", "हां — व्यावसायिक इस्तेमाल मुफ़्त है",
     "हाँ — कमर्शियल इस्तेमाल मुफ़्त है"),
    ("hi", "landing-app-store-qr-code", "स्टोर लिंक कहां से लें", "स्टोर लिंक कहाँ से लें"),
]


TICKET_DESC = ("Create free QR codes for tickets: link to your ticket or check-in "
               "page, print one code per ticket with Batch mode, no sign-up for "
               "static codes, never expires.")

# Whole-value replacements: the ticket meta description ran 182–199 characters
# in five languages and would have been truncated in the SERP.
SET_VALUES = [
    ("de", "landing-ticket-qr-code", TICKET_DESC,
     "Kostenlose QR-Codes für Tickets: ein Code pro Ticket per Stapelmodus, "
     "ohne Anmeldung für statische Codes, laufen nie ab."),
    ("es", "landing-ticket-qr-code", TICKET_DESC,
     "Códigos QR gratis para entradas: un código por entrada con el modo lote, "
     "sin registro para los estáticos y sin caducidad."),
    ("fr", "landing-ticket-qr-code", TICKET_DESC,
     "QR codes gratuits pour vos billets\xa0: un code par billet avec le mode lot, "
     "sans inscription pour les codes statiques et sans expiration."),
    ("pt", "landing-ticket-qr-code", TICKET_DESC,
     "QR codes grátis para ingressos: um código por ingresso com o modo lote, "
     "sem cadastro para códigos estáticos — eles nunca expiram."),
    ("ru", "landing-ticket-qr-code", TICKET_DESC,
     "Бесплатные QR-коды для билетов: по коду на каждый билет в пакетном режиме, "
     "без регистрации для статических кодов, без срока действия."),
    # Chinese packs ~2x the information per character; 41 was thin for a SERP
    # snippet, so this adds the use cases the English carries.
    ("zh", "landing-ticket-qr-code", TICKET_DESC,
     "免费做门票二维码：链接到购票页或签到页，批量模式一票一码，静态码免注册、"
     "永不过期，演唱会、会议、校园活动都能用。"),
]


def apply(lang, page, needle, repl, dry):
    path = os.path.join(SITE, "tools/i18n", lang + ".json")
    table = json.load(open(path, encoding="utf-8"))
    bucket = table.get(page)
    if not bucket:
        return f"{lang}/{page}: 页面不存在"
    hits = [k for k, v in bucket.items() if needle in v]
    if not hits:
        # Already done by an earlier rule (or by a previous run): the
        # replacement is present, so there is nothing left to change.
        if any(repl in v for v in bucket.values()):
            return None
        return f"{lang}/{page}: 找不到 “{needle[:40]}”"
    for key in hits:
        bucket[key] = bucket[key].replace(needle, repl)
    if not dry:
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(table, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    return None


def main():
    dry = "--dry-run" in sys.argv
    problems = []
    for lang, page, needle, repl in TITLE_FIXES + FIXES:
        err = apply(lang, page, needle, repl, dry)
        if err:
            problems.append(err)
    for lang, page, key, value in SET_VALUES:
        path = os.path.join(SITE, "tools/i18n", lang + ".json")
        table = json.load(open(path, encoding="utf-8"))
        bucket = table.get(page, {})
        if key not in bucket:
            problems.append(f"{lang}/{page}: 缺 {key[:40]}")
            continue
        if bucket[key] != value:
            bucket[key] = value
            if not dry:
                with open(path, "w", encoding="utf-8") as fh:
                    json.dump(table, fh, ensure_ascii=False, indent=1)
                    fh.write("\n")
    if problems:
        print(f"{len(problems)} 处未能应用：")
        for p in problems:
            print("  ", p)
    else:
        print(f"全部 {len(TITLE_FIXES) + len(FIXES)} 处已应用{'（演练）' if dry else ''}")


if __name__ == "__main__":
    main()
