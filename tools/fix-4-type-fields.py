#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix 2026-10-19 add-4-types.py bug: field defs went into types{} (dead dup
keys) instead of fields{}. Moves them to fields{} for all 10 languages and
removes the dead duplicates from types{}."""
import re

PATH = "assets/js/app.js"
src = open(PATH, encoding="utf-8").read()

FIELD_TR = {  # field_id, {lang: label}, placeholder  (copied from add-4-types.py)
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
NEWTYPE_ORDER = ["review", "mp3", "google-form", "menu"]
LANGS = ["en", "zh", "es", "pt", "fr", "de", "ja", "ru", "hi", "ar"]  # file order


def find_matching(s, i, op, cl):
    depth = 0; instr = None; esc = False
    for j in range(i, len(s)):
        c = s[j]
        if instr:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == instr: instr = None
            continue
        if c in '"\'' : instr = c; continue
        if c == op: depth += 1
        elif c == cl:
            depth -= 1
            if depth == 0: return j
    raise ValueError("unbalanced")


base = src.index('const I18N = {')
i18n_end = src.index('\n};', base)
i18n = src[base:i18n_end]
bounds = []
for m in re.finditer(r'[{,]\s*(en|zh|es|hi|ar|pt|fr|ru|de|ja):\{', i18n):
    bounds.append((m.group(1), m.start() + 1))
bounds.sort(key=lambda x: x[1])
assert len(bounds) == 10, f"found {len(bounds)} langs"
assert [b[0] for b in bounds] == LANGS, [b[0] for b in bounds]

parts = []
for idx, (lg, pos) in enumerate(bounds):
    end = bounds[idx + 1][1] - 1 if idx + 1 < len(bounds) else len(i18n)
    ob = i18n[pos:end]
    orig_ob = ob

    # 1. Remove dead field-def duplicates from types{} (keep tab labels)
    ti = ob.index('types:{')
    te = find_matching(ob, ob.index('{', ti), '{', '}')
    types_region = ob[ti:te + 1]
    for t in NEWTYPE_ORDER:
        pat = f'"{t}":[['
        di = types_region.find(pat)
        assert di != -1, f"{lg}: dead dup for {t} not found in types"
        de = find_matching(types_region, di + len(pat) - 2, '[', ']')
        # entry is `"t":[[...]],` — de points at final ']'; expect comma after
        assert types_region[de + 1] == ',', f"{lg}: no comma after dead dup {t}"
        types_region = types_region[:di] + types_region[de + 2:]
    ob = ob[:ti] + types_region + ob[te + 1:]
    # sanity: exactly one "review" key left in types (the tab label)
    ti2 = ob.index('types:{')
    te2 = find_matching(ob, ob.index('{', ti2), '{', '}')
    assert ob[ti2:te2 + 1].count('"review":') == 1, f"{lg}: types still has dup review"

    # 2. Insert field defs into fields{} after "appstore" value
    fi = ob.index('fields:{')
    ai = ob.index('"appstore":', fi)
    ab = ob.index('[', ai)
    ae = find_matching(ob, ab, '[', ']')
    fins = []
    for t in NEWTYPE_ORDER:
        fid, labels, ph = FIELD_TR[t]
        fins.append(f'"{t}":[[\"{fid}\",\"{labels[lg]}\",\"{ph}\"]]')
    ob = ob[:ae + 1] + "," + ",".join(fins) + ob[ae + 1:]
    # sanity: fields now has the 4 types
    fi2 = ob.index('fields:{')
    fe2 = find_matching(ob, ob.index('{', fi2), '{', '}')
    for t in NEWTYPE_ORDER:
        assert f'"{t}":[[' in ob[fi2:fe2 + 1], f"{lg}: fields missing {t}"

    assert ob != orig_ob
    parts.append((pos, end, ob))

for pos, end, ob in reversed(parts):
    i18n = i18n[:pos] + ob + i18n[end:]
src = src[:base] + i18n + src[i18n_end:]
open(PATH, "w", encoding="utf-8").write(src)
print("fix-4-type-fields.py OK")
