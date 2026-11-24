#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""构建后把「真正变了的页面」推给搜索引擎。

设计原则：只推有变更的 URL。判断依据是 HTML 文件内容的 md5，不是文件时间
戳——build-all.py 会重写所有页面，但内容没变就不该打扰搜索引擎。

用法（一般由 build-all.py 自动调用）：
    from push_indexnow import snapshot, push_changed
    before = snapshot(SITE)
    ... 构建 ...
    push_changed(SITE, before)

也可单独运行：
    python3 tools/push_indexnow.py --since-git   # 推 git 里改过的页面
"""
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

HOST = "freeqrly.com"
BASE = f"https://{HOST}"
CONFIG = os.path.expanduser("~/.config/freeqrly/push.json")

# 不属于可索引页面的文件
SKIP = {"404.html"}


def _key(site):
    """从仓库里的 <key>.txt 读出 IndexNow key（该文件本身就是公开的）。"""
    for name in os.listdir(site):
        if re.fullmatch(r"[A-Za-z0-9-]{8,128}\.txt", name) and name not in ("llms.txt", "robots.txt"):
            return name[:-4]
    return None


def _baidu_token():
    if not os.path.exists(CONFIG):
        return None
    try:
        return json.load(open(CONFIG, encoding="utf-8")).get("baidu_token") or None
    except Exception:
        return None


# 不是站点页面的目录（按路径分段精确匹配，不能做字符串包含——
# 调用方传进来的 site 可能是 ".../repo/tools/.."，那样 "tools" 会命中整棵树）
EXCLUDE_DIRS = {".git", "node_modules", "tools", "functions", "tests"}


def snapshot(site):
    """{相对路径: md5} —— 构建前调用。"""
    site = os.path.realpath(site)
    out = {}
    for root, dirs, files in os.walk(site):
        rel_root = os.path.relpath(root, site)
        parts = [] if rel_root == "." else rel_root.split(os.sep)
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        if any(p in EXCLUDE_DIRS for p in parts):
            continue
        for f in files:
            if not f.endswith(".html") or f in SKIP:
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, site)
            with open(full, "rb") as fh:
                out[rel] = hashlib.md5(fh.read()).hexdigest()
    return out


def changed_urls(site, before, after=None):
    """对比快照，返回变更页面对应的 URL。"""
    after = after or snapshot(site)
    urls = []
    for rel, digest in after.items():
        if before.get(rel) == digest:
            continue
        # index.html → 目录 URL；其他 .html → 原路径
        if rel == "index.html":
            path = "/"
        elif rel.endswith("/index.html"):
            path = "/" + rel[: -len("index.html")]
        else:
            path = "/" + rel
        urls.append(BASE + path)
    return sorted(urls)


def push_indexnow(urls, key):
    body = json.dumps({
        "host": HOST,
        "key": key,
        "keyLocation": f"{BASE}/{key}.txt",
        "urlList": urls,
    }).encode()
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow", data=body,
        headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        r = urllib.request.urlopen(req, timeout=40)
        return r.status, r.read().decode()[:200]
    except urllib.error.HTTPError as e:
        return e.code, e.read()[:200].decode()
    except Exception as e:
        return None, str(e)[:200]


def push_baidu(urls, token, limit=10):
    """百度配额通常是 10 条/天，逐条推，用完即停。"""
    ok = 0
    remain = None
    err = ""
    for u in urls[:limit]:
        endpoint = f"http://data.zz.baidu.com/urls?site={BASE}&token={token}"
        req = urllib.request.Request(endpoint, data=u.encode(),
                                     headers={"Content-Type": "text/plain"})
        try:
            d = json.loads(urllib.request.urlopen(req, timeout=30).read().decode())
            if d.get("error"):
                err = f"{d['error']}: {d.get('message', '')}"
                break
            ok += d.get("success", 0)
            remain = d.get("remain")
            if remain == 0:
                break
        except urllib.error.HTTPError as e:
            # 百度把 over quota 也放在 400 的响应体里，要读 body 才知道原因
            try:
                body = json.loads(e.read().decode())
                msg = body.get("message") or str(e)
                err = "当日配额已用完" if "over quota" in msg else f"HTTP {e.code}: {msg}"
            except Exception:
                err = f"HTTP {e.code}"
            break
        except Exception as e:
            err = str(e)[:120]
            break
        time.sleep(0.4)
    return ok, remain, err


def push_changed(site, before, quiet=False):
    """对比快照并把变更推出去。构建脚本调用这个。"""
    urls = changed_urls(site, before)
    if not urls:
        if not quiet:
            print("  没有页面内容变化，跳过推送")
        return 0

    if not quiet:
        print(f"  检测到 {len(urls)} 个页面有变更")

    key = _key(site)
    if key:
        code, body = push_indexnow(urls, key)
        if not quiet:
            if code in (200, 202):
                print(f"  ✅ IndexNow：{len(urls)} 个 URL → Bing/Yandex/Seznam/Naver/Yep/Amazon")
            else:
                print(f"  ⚠️  IndexNow 失败 HTTP {code}: {body}")
    elif not quiet:
        print("  ⚠️  没找到 IndexNow key 文件，跳过")

    token = _baidu_token()
    if token:
        ok, remain, err = push_baidu(urls, token)
        if not quiet:
            msg = f"  百度：成功 {ok} 条"
            if remain is not None:
                msg += f"，剩余配额 {remain}"
            if err:
                msg += f"（{err}）"
            print(msg)
    elif not quiet:
        print("  百度：未配置 token，跳过")

    return len(urls)


def main():
    site = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if "--since-git" in sys.argv:
        import subprocess
        out = subprocess.run(["git", "diff", "--name-only", "HEAD~1", "HEAD"],
                             cwd=site, capture_output=True, text=True).stdout
        urls = []
        for rel in out.split():
            if not rel.endswith(".html") or os.path.basename(rel) in SKIP:
                continue
            if rel == "index.html":
                urls.append(BASE + "/")
            elif rel.endswith("/index.html"):
                urls.append(BASE + "/" + rel[: -len("index.html")])
            else:
                urls.append(BASE + "/" + rel)
        if not urls:
            print("最近一次提交没有改动页面")
            return
        key = _key(site)
        code, body = push_indexnow(sorted(set(urls)), key) if key else (None, "no key")
        print(f"推送 {len(urls)} 个 URL：HTTP {code}")
        return

    # 无参数：对比工作区与上次快照（用 git stash 不现实，这里只做提示）
    print("用法：")
    print("  python3 tools/push_indexnow.py --since-git   # 推最近一次提交改动的页面")
    print("  或由 build-all.py 自动调用")


if __name__ == "__main__":
    main()
