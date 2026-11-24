#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按资源内容哈希同步 HTML 里的 ?v= 版本号。

设计目标：只有被引用的 CSS/JS 文件内容真的变了，版本号才变。改一页正文、
改一张图片、跑一次构建，都不应该让全站 HTML 的字节发生变化——否则
Googlebot 每次都会看到"整站几百页都被修改了"。

规则：
- 只处理 assets/css/ 和 assets/js/ 下的引用；图片用的是手工维护的
  ?v=t2 / m3 标记，不在本模块职责内。
- 本来就带 ?v= 的引用才更新，不会给没带版本号的引用新增参数。
- 找不到对应文件（外部资源、拼错的路径）时保持原样。
- 相对路径（../assets/css/main.css）相对该 HTML 所在目录解析。
"""
import glob
import hashlib
import os
import re

LINK_RE = re.compile(
    r'(?P<pre>(?:href|src)=")'
    r'(?P<url>[^"?#]*assets/(?:css|js)/[^"?#]+\.[A-Za-z0-9]+)'
    r'(?:\?v=(?P<ver>[^"&]*))?'
    r'(?P<post>[^"]*")'
)


def _resolve(url_path, html_path):
    if url_path.startswith("/"):
        return os.path.join(html_path[:0] or ".", url_path.lstrip("/"))
    return os.path.normpath(os.path.join(os.path.dirname(html_path), url_path))


def sync_versions(site, dry_run=False, html_glob="**/*.html"):
    """就地更新站点下所有 HTML 的资源版本号。

    返回 (改动文件数, 改动处数)。
    """
    cache = {}

    def asset_hash(url_path, html_path):
        if url_path.startswith("/"):
            full = os.path.join(site, url_path.lstrip("/"))
        else:
            full = os.path.normpath(os.path.join(os.path.dirname(html_path), url_path))
        if full in cache:
            return cache[full]
        try:
            with open(full, "rb") as fh:
                v = hashlib.sha256(fh.read()).hexdigest()[:8]
        except (FileNotFoundError, IsADirectoryError, OSError):
            v = None
        cache[full] = v
        return v

    changed_files = 0
    stamp_changes = 0

    for path in glob.glob(os.path.join(site, html_glob), recursive=True):
        html = open(path, encoding="utf-8").read()
        counter = {"n": 0}

        def repl(m, _path=path):
            ver = asset_hash(m.group("url"), _path)
            if ver is None or m.group("ver") is None:
                return m.group(0)
            if m.group("ver") == ver:
                return m.group(0)
            counter["n"] += 1
            return f'{m.group("pre")}{m.group("url")}?v={ver}{m.group("post")}'

        new = LINK_RE.sub(repl, html)
        if new != html:
            changed_files += 1
            stamp_changes += counter["n"]
            if not dry_run:
                open(path, "w", encoding="utf-8").write(new)

    return changed_files, stamp_changes
