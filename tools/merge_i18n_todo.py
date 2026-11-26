#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge translated strings from tools/i18n/todo/<lang>.done.json into
tools/i18n/<lang>.json.

Why this exists: the translation tables are keyed by the exact English
string, so a page that gets rewritten (the App Store landing page was, twice)
leaves every new string untranslated while the old keys sit there unused.
`extract-i18n.py` + this merge keeps the tables in step with the EN source.

Guards, because a bad merge silently ships English or broken markup:
  - every key must exist in the page's EN extract (no invented strings);
  - HTML tag counts must match the source string;
  - JSON must round-trip.

Usage: python3 tools/merge_i18n_todo.py [lang ...] [--dry-run]
"""
import json
import os
import re
import sys

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."
TODO = os.path.join(SITE, "tools/i18n/todo")
EXTRACT = os.path.join(SITE, "tools/i18n/extract")
LANGS = ["zh", "ja", "de", "es", "fr", "pt", "ru", "hi", "ar"]
TAGS = ("<span", "</span>", "<b>", "</b>", "<code>", "</code>")


def en_strings(page):
    path = os.path.join(EXTRACT, page + ".en.json")
    if not os.path.exists(path):
        return None
    return set(json.load(open(path, encoding="utf-8")))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    langs = args or LANGS
    total = 0
    for lang in langs:
        # Several agents may each deliver a slice (zh.done.json, zh.ticket.done.json).
        slices = sorted(
            os.path.join(TODO, f) for f in os.listdir(TODO)
            if re.fullmatch(re.escape(lang) + r"(\.[a-z-]+)?\.done\.json", f))
        if not slices:
            print(f"{lang}: 没有 {lang}.done.json，跳过")
            continue
        done = {}
        for src in slices:
            for page, pairs in json.load(open(src, encoding="utf-8")).items():
                done.setdefault(page, {}).update(pairs)
        table_path = os.path.join(SITE, "tools/i18n", lang + ".json")
        table = json.load(open(table_path, encoding="utf-8"))
        added = 0
        problems = []
        for page, pairs in done.items():
            known = en_strings(page)
            if known is None:
                problems.append(f"{page}: 没有 EN extract，无法校验")
                continue
            bucket = table.setdefault(page, {})
            for en, tr in pairs.items():
                if en not in known:
                    problems.append(f"{page}: 源串不在 EN extract 里 → {en[:50]}")
                    continue
                for tag in TAGS:
                    if en.count(tag) != tr.count(tag):
                        problems.append(
                            f"{page}: 标签数不符 {tag} ({en.count(tag)} vs {tr.count(tag)}) → {en[:40]}")
                if not tr.strip():
                    problems.append(f"{page}: 空翻译 → {en[:50]}")
                    continue
                if bucket.get(en) != tr:
                    bucket[en] = tr
                    added += 1
        if problems:
            print(f"{lang}: {len(problems)} 个问题，未写入")
            for p in problems[:12]:
                print("   ", p)
            continue
        if not dry:
            with open(table_path, "w", encoding="utf-8") as fh:
                json.dump(table, fh, ensure_ascii=False, indent=1)
                fh.write("\n")
        total += added
        print(f"{lang}: 合并 {added} 条{'（演练）' if dry else ''}")
    print(f"合计 {total} 条")


if __name__ == "__main__":
    main()
