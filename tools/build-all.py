#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FreeQrly 一键构建脚本。

维护时只需要改源码，然后跑这一个命令：
    python3 tools/build-all.py

它会自动：
1. 用 tools/gen-landing.py 重新生成 10 个落地页（含 studio 区块同步）
2. 用 tools/build-home-i18n.py 重新生成 9 个语言的静态首页
3. 统一 bump 所有 HTML 的 CSS/JS ?v= 版本号

改源码的位置：
- 首页结构/文案      → index.html
- 生成器逻辑/UI文案   → assets/js/app.js （I18N 翻译也在里面）
- 落地页英文文案      → tools/gen-landing.py 的 PAGES 定义
- 样式               → assets/css/main.css
"""
import os, re, sys, glob, subprocess
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."
TODAY = date.today().strftime("%Y%m%d")

# --dry-run：只报告会改什么，不写任何文件（包括前两步的生成结果）。
DRY_RUN = "--dry-run" in sys.argv
# --no-push：构建但不通知搜索引擎。
NO_PUSH = "--no-push" in sys.argv

# 构建前记录每个 HTML 的内容哈希，末尾对比，只推真正变了的页面。
from push_indexnow import snapshot, push_changed
BEFORE = {} if DRY_RUN else snapshot(SITE)

def run(cmd):
    r = subprocess.run(cmd, cwd=SITE, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAILED: {' '.join(cmd)}\n{r.stderr}")
        sys.exit(1)
    return r.stdout.strip()

if DRY_RUN:
    print("（--dry-run：前两步生成跳过，只预演版本号同步）")
else:
    # 1. 重新生成落地页
    print("→ 生成落地页...")
    out = run([sys.executable, "tools/gen-landing.py"])
    print(f"  {out.split(chr(10))[-1] if out else 'ok'}")

    # 2. 重新生成多语言首页
    print("→ 生成 9 语言静态首页...")
    out = run([sys.executable, "tools/build-home-i18n.py"])
    for line in out.split("\n"):
        if line.startswith("Wrote"):
            print(f"  {line}")

    # 2.1 重新生成本地化子页（/<lang>/<slug>/）。
    #     以前这一步只在手工调用时才跑，于是英文页改过之后，各语言的落地页
    #     长期停在旧版本上：App Store 页的正文在 9 种语言里都还是英文。
    print("→ 重新生成本地化子页...")
    out = run([sys.executable, "tools/localize_pages.py"])
    for line in out.split("\n")[-3:]:
        if line.strip():
            print(f"  {line}")

    # 2.5. 合并首页 CSS（只首页用 bundle，子页/落地页仍用 3 个源文件）：
    #     main + acct-menu + site-header 按原引用顺序拼接，省 2 个渲染阻塞请求。
    #     bundle 是生成物，源文件不动；顺序即层叠顺序，不可调换。
    print("→ 合并首页 CSS...")
    bundle = ""
    for _name in ["main.css", "acct-menu.css", "site-header.css"]:
        bundle += open(os.path.join(SITE, "assets/css", _name), encoding="utf-8").read() + "\n"
    open(os.path.join(SITE, "assets/css/home-bundle.css"), "w", encoding="utf-8").write(bundle)
    print(f"  home-bundle.css ({len(bundle)} 字节)")

    # 2.6. 重建 sitemap。
    #     这一步以前不在构建里，于是新写的博客从来没进过 sitemap：线上 819 条，
    #     实际有 849 条，30 个已上线、可访问的页面搜索引擎一无所知。
    #     lastmod 只取自页面自身的日期值（见 gen-sitemap.py），所以改文案、
    #     跑构建都不会让它变——只有页面内容日期真的更新时才会变。
    print("→ 重建 sitemap...")
    out = run([sys.executable, "tools/gen-sitemap.py"])
    print(f"  {out.split(chr(10))[-1] if out else 'ok'}")

# 3. 同步 ?v= 版本号：按资源内容哈希，只有文件真的变了才变。
#
# 旧做法是每次构建把所有页面的版本号字母 +1，于是哪怕只改一页文案，全站
# 每个 HTML 的字节都会变，Googlebot 看到的是"整站 600 多页都被修改了"。
# 现在每个资源用自己的内容哈希当版本号：改一个 CSS 只影响引用它的页面，
# 改一页正文则完全不动版本号。逻辑见 tools/version_sync.py。
print("→ 同步 ?v= 版本号（按资源内容哈希）...")
DRY_RUN = "--dry-run" in sys.argv
from version_sync import sync_versions
changed, stamps = sync_versions(SITE, dry_run=DRY_RUN)
verb = "将改动" if DRY_RUN else "已改动"
print(f"  {verb} {changed} 个 HTML，{stamps} 处 ?v=")
if DRY_RUN:
    print("  （--dry-run：未写入任何文件）")
elif changed == 0:
    print("  所有版本号已是最新，无需改动")

# 4. 通知搜索引擎：只推内容真的变了的页面
if not DRY_RUN and not NO_PUSH:
    print("→ 通知搜索引擎...")
    try:
        push_changed(SITE, BEFORE)
    except Exception as e:
        # 推送失败不影响构建结果
        print(f"  ⚠️  推送出错（不影响构建）：{e}")
elif DRY_RUN:
    print("\n（--dry-run：跳过搜索引擎推送）")

print("\n完成。检查 git status，确认无误后 commit + push 即可上线。")
