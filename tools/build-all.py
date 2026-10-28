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

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."
TODAY = date.today().strftime("%Y%m%d")

def run(cmd):
    r = subprocess.run(cmd, cwd=SITE, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAILED: {' '.join(cmd)}\n{r.stderr}")
        sys.exit(1)
    return r.stdout.strip()

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

# 2.5. 合并首页 CSS（只首页用 bundle，子页/落地页仍用 3 个源文件）：
#     main + acct-menu + site-header 按原引用顺序拼接，省 2 个渲染阻塞请求。
#     bundle 是生成物，源文件不动；顺序即层叠顺序，不可调换。
print("→ 合并首页 CSS...")
bundle = ""
for _name in ["main.css", "acct-menu.css", "site-header.css"]:
    bundle += open(os.path.join(SITE, "assets/css", _name), encoding="utf-8").read() + "\n"
open(os.path.join(SITE, "assets/css/home-bundle.css"), "w", encoding="utf-8").write(bundle)
print(f"  home-bundle.css ({len(bundle)} 字节)")

# 3. 统一版本号：找当前最大的 b3x 后缀，+1
print("→ 统一 ?v= 版本号...")
versions = set()
for f in glob.glob(os.path.join(SITE, "**/*.html"), recursive=True):
    h = open(f, encoding="utf-8").read()
    versions.update(re.findall(r'\?v=(b3[a-z]*-\d{8})', h))
if not versions:
    print("  未找到旧版本号，跳过")
else:
    cur = sorted(versions)[-1]
    m = re.match(r'b3([a-z]*)-(\d{8})', cur)
    letter = m.group(1)
    def bump_letter(s):
        if not s:
            return 'a'
        chars = list(s)
        i = len(chars) - 1
        while i >= 0:
            if chars[i] != 'z':
                chars[i] = chr(ord(chars[i]) + 1)
                return ''.join(chars)
            chars[i] = 'a'
            i -= 1
        return 'a' + ''.join(chars)
    nxt = f"b3{bump_letter(letter)}-{TODAY}"
    n = 0
    for f in glob.glob(os.path.join(SITE, "**/*.html"), recursive=True):
        h = open(f, encoding="utf-8").read()
        h2, c = re.subn(r'\?v=b3[a-z]*-\d{8}', f'?v={nxt}', h)
        if c:
            open(f, "w", encoding="utf-8").write(h2)
            n += 1
    print(f"  {cur} → {nxt} ({n} 个文件)")

print("\n完成。检查 git status，确认无误后 commit + push 即可上线。")
