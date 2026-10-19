#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add 4 new QR types (review, mp3, google-form, menu) to app.js + update counts 13->17."""
import re, sys

PATH = "assets/js/app.js"
src = open(PATH, encoding="utf-8").read()
orig = src

def rep(old, new, count=1):
    global src
    assert src.count(old) == count, f"pattern found {src.count(old)}x (expected {count}): {old[:60]!r}"
    src = src.replace(old, new, count)

LANGS = ["en","zh","es","hi","ar","pt","fr","ru","de","ja"]

# ---------- translations ----------
TYPE_TR = {
 'review': {
  'en': ["Reviews","get 5-star reviews"], 'zh': ["评价","获取五星好评"],
  'es': ["Reseñas","reseñas de 5 estrellas"], 'hi': ["समीक्षाएं","5-स्टार रिव्यू पाएं"],
  'ar': ["التقييمات","احصل على تقييم 5 نجوم"], 'pt': ["Avaliações","avaliações 5 estrelas"],
  'fr': ["Avis","avis 5 étoiles"], 'ru': ["Отзывы","собирайте отзывы"],
  'de': ["Bewertungen","5-Sterne-Bewertungen"], 'ja': ["レビュー","高評価を集める"]},
 'mp3': {
  'en': ["Audio","MP3 & sound"], 'zh': ["音频","MP3 音乐"],
  'es': ["Audio","MP3 y sonido"], 'hi': ["ऑडियो","MP3 और साउंड"],
  'ar': ["الصوت","MP3 وصوتيات"], 'pt': ["Áudio","MP3 e som"],
  'fr': ["Audio","MP3 et son"], 'ru': ["Аудио","MP3 и звук"],
  'de': ["Audio","MP3 & Sound"], 'ja': ["音声","MP3・サウンド"]},
 'google-form': {
  'en': ["Google Form","collect responses"], 'zh': ["谷歌表单","收集问卷填写"],
  'es': ["Formulario","recoge respuestas"], 'hi': ["Google फ़ॉर्म","जवाब इकट्ठा करें"],
  'ar': ["نموذج Google","اجمع الردود"], 'pt': ["Formulário","colete respostas"],
  'fr': ["Formulaire","recueillez des réponses"], 'ru': ["Google-форма","собирайте ответы"],
  'de': ["Formular","Antworten sammeln"], 'ja': ["フォーム","回答を集める"]},
 'menu': {
  'en': ["Menu","restaurant menu"], 'zh': ["菜单","餐厅菜单"],
  'es': ["Menú","carta del restaurante"], 'hi': ["मेनू","रेस्तरां मेनू"],
  'ar': ["القائمة","قائمة المطعم"], 'pt': ["Cardápio","menu do restaurante"],
  'fr': ["Menu","carte du restaurant"], 'ru': ["Меню","меню ресторана"],
  'de': ["Speisekarte","Restaurantmenü"], 'ja': ["メニュー","レストランメニュー"]},
}
FIELD_TR = {  # field_id, {lang: label}, placeholder
 'review': ("rvlink", {
  'en': "Review page link", 'zh': "评价页面链接", 'es': "Enlace de reseñas",
  'hi': "समीक्षा पेज लिंक", 'ar': "رابط صفحة التقييمات", 'pt': "Link de avaliações",
  'fr': "Lien de la page d'avis", 'ru': "Ссылка на отзывы", 'de': "Link zur Bewertungsseite",
  'ja': "レビューページのリンク"}, "https://g.page/your-business/review"),
 'mp3': ("mp3link", {
  'en': "Audio file link", 'zh': "音频文件链接", 'es': "Enlace del audio",
  'hi': "ऑडियो फ़ाइल लिंक", 'ar': "رابط الملف الصوتي", 'pt': "Link do áudio",
  'fr': "Lien du fichier audio", 'ru': "Ссылка на аудио", 'de': "Link zur Audiodatei",
  'ja': "音声ファイルのリンク"}, "https://example.com/song.mp3"),
 'google-form': ("gflink", {
  'en': "Form link", 'zh': "表单链接", 'es': "Enlace del formulario",
  'hi': "फ़ॉर्म लिंक", 'ar': "رابط النموذج", 'pt': "Link do formulário",
  'fr': "Lien du formulaire", 'ru': "Ссылка на форму", 'de': "Link zum Formular",
  'ja': "フォームのリンク"}, "https://forms.gle/abc123XYZ"),
 'menu': ("mnlink", {
  'en': "Menu link", 'zh': "菜单链接", 'es': "Enlace del menú",
  'hi': "मेनू लिंक", 'ar': "رابط القائمة", 'pt': "Link do cardápio",
  'fr': "Lien du menu", 'ru': "Ссылка на меню", 'de': "Link zur Speisekarte",
  'ja': "メニューのリンク"}, "https://example.com/menu"),
}
F2D = {  # (append_text, batch_separator)
 'en': (", reviews, audio, Google Forms, menus", " — plus Batch mode"),
 'zh': ("、评价、音频、谷歌表单、菜单", "，另有批量模式"),
 'es': (", reseñas, audio, formularios de Google, menús", " — más modo lote"),
 'hi': (", समीक्षाएं, ऑडियो, Google फ़ॉर्म, मेनू", " — साथ में बैच मोड"),
 'ar': ("، التقييمات، الصوت، نماذج Google، القوائم", " — بالإضافة إلى الوضع الجماعي"),
 'pt': (", avaliações, áudio, formulários do Google, cardápios", " — mais modo lote"),
 'fr': (", avis, audio, formulaires Google, menus", " — plus le mode lot"),
 'ru': (", отзывы, аудио, Google-формы, меню", " — плюс пакетный режим"),
 'de': (", Bewertungen, Audio, Google-Formulare, Speisekarten", " — plus Stapelmodus"),
 'ja': ("、レビュー、音声、Google フォーム、メニュー", " — 一括モード"),
}
NEWTYPE_ORDER = ["review", "mp3", "google-form", "menu"]

# ---------- A. structural edits ----------
rep('const ORDER = ["url","text","wifi","vcard","email","sms","phone","geo","event","bitcoin","coupon","appstore","batch"];',
    'const ORDER = ["url","text","wifi","vcard","email","sms","phone","geo","event","bitcoin","coupon","appstore","review","mp3","google-form","menu","batch"];')

rep('bitcoin:"₿",coupon:"🎟️",appstore:"📱",batch:"📚"};',
    'bitcoin:"₿",coupon:"🎟️",appstore:"📱",review:"⭐",mp3:"🎵","google-form":"📋",menu:"🍽️",batch:"📚"};')

old_appstore = '''    case "appstore": {
      const ios = v("appios"), and = v("appand");
      // Return a simple landing format - iOS first, fallback Android
      return ios || and || "";
    }'''
rep(old_appstore, old_appstore + '''
    case "review": return v("rvlink")||"";
    case "mp3": return v("mp3link")||"";
    case "google-form": return v("gflink")||"";
    case "menu": return v("mnlink")||"";''')

rep('''  event: "Party | 2026-10-20T19:00 | 2026-10-20T22:00 | Home | Bring snacks",
};''',
    '''  event: "Party | 2026-10-20T19:00 | 2026-10-20T22:00 | Home | Bring snacks",
  review: "https://g.page/your-business/review",
  mp3: "https://example.com/song.mp3",
  "google-form": "https://forms.gle/abc123XYZ",
  menu: "https://example.com/menu",
};''')

rep('const types = ["url","text","email","sms","phone","geo","wifi","vcard","event","bitcoin","coupon","appstore"];',
    'const types = ["url","text","email","sms","phone","geo","wifi","vcard","event","bitcoin","coupon","appstore","review","mp3","google-form","menu"];')

# batch template sheets: insert after appstore sheet
old_sheet = '''      appstore: [["App Store Link","Google Play Link"], ["https://apps.apple.com/app/...","https://play.google.com/store/apps/..."], ["https://apps.apple.com/app/...","https://play.google.com/store/apps/..."]],'''
rep(old_sheet, old_sheet + '''
      review: [["Review Link"], ["https://g.page/your-business/review"], ["https://example.com/reviews"]],
      mp3: [["Audio Link"], ["https://example.com/song.mp3"], ["https://example.com/episode1.mp3"]],
      "google-form": [["Form Link"], ["https://forms.gle/abc123XYZ"], ["https://docs.google.com/forms/d/e/xyz/viewform"]],
      menu: [["Menu Link"], ["https://example.com/menu"], ["https://restaurant.com/menu.pdf"]],''')

# ---------- B. per-language i18n edits ----------
base = src.index('const I18N = {')
i18n_end = src.index('\n};', base)
i18n = src[base:i18n_end]
bounds = []
for m in re.finditer(r'[{,]\s*(en|zh|es|hi|ar|pt|fr|ru|de|ja):\{', i18n):
    bounds.append((m.group(1), m.start()+1))
bounds.sort(key=lambda x: x[1])
assert len(bounds) == 10, f"found {len(bounds)} langs"

def find_matching(s, i, op, cl):
    """i points at op; return index of matching cl. Skips string literals."""
    depth = 0; instr = None; esc = False
    for j in range(i, len(s)):
        c = s[j]
        if instr:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == instr: instr = None
            continue
        if c in '"\'': instr = c; continue
        if c == op: depth += 1
        elif c == cl:
            depth -= 1
            if depth == 0: return j
    raise ValueError("unbalanced")

new_i18n_parts = []
prev = 0
for idx, (lg, pos) in enumerate(bounds):
    end = bounds[idx+1][1]-1 if idx+1 < len(bounds) else len(i18n)
    block = i18n[pos:end]
    ob = block

    # 1. types{}: insert 4 entries before "batch":
    bi = ob.index('"batch":')
    be = find_matching(ob, ob.index('[', bi), '[', ']')
    ins = "".join(f'"{t}":["{TYPE_TR[t][lg][0]}","{TYPE_TR[t][lg][1]}"],' for t in NEWTYPE_ORDER)
    ob = ob[:bi] + ins + ob[bi:]

    # 2. fields{}: insert 4 entries after "appstore" value.
    # MUST scope to fields{} — ob.index('"appstore":') alone finds types{} first
    # (2026-10-19 bug: field defs landed in types{} as dead dup keys, fields{} got nothing)
    fi = ob.index('fields:{')
    ai = ob.index('"appstore":', fi)
    ab = ob.index('[', ai)
    ae = find_matching(ob, ab, '[', ']')
    fins = []
    for t in NEWTYPE_ORDER:
        fid, labels, ph = FIELD_TR[t]
        fins.append(f'"{t}":[["{fid}","{labels[lg]}","{ph}"]]')
    ob = ob[:ae+1] + "," + ",".join(fins) + ob[ae+1:]

    # 3. f2t: 13 -> 17
    ob2, n = re.subn(r'f2t:"13', 'f2t:"17', ob)
    assert n == 1, f"{lg}: f2t replacements={n}"
    ob = ob2

    # 4. f2d: append new type names before batch separator
    app, sep = F2D[lg]
    assert sep in ob, f"{lg}: separator not found"
    ob = ob.replace(sep, app + sep, 1)

    new_i18n_parts.append((pos, end, ob))

# reassemble (from last to first to keep offsets valid)
for pos, end, ob in reversed(new_i18n_parts):
    i18n = i18n[:pos] + ob + i18n[end:]
src = src[:base] + i18n + src[i18n_end:]

open(PATH, "w", encoding="utf-8").write(src)
print("app.js updated OK")
# sanity: no '13 QR' left in f2t, counts
print("f2t 17 count:", len(re.findall(r'f2t:"17', src)))
print("f2t 13 left:", len(re.findall(r'f2t:"13', src)))
print("review types entries:", len(re.findall(r'"review":\["', src)))
print("BATCH order has 17:", src.count('"google-form","menu","batch"'))
