#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Normalize blank/articles/articles-data.js (JS is the only article source)."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARTICLES = ROOT / "articles"
DATA_JS = ARTICLES / "articles-data.js"


def load_list() -> list:
    if not DATA_JS.exists():
        return []
    text = DATA_JS.read_text(encoding="utf-8-sig")
    match = re.search(
        r"window\.__BLANK_(?:TXT_)?ARTICLES\s*=\s*(\[[\s\S]*\])\s*;?\s*$",
        text,
    )
    if not match:
        raise SystemExit(f"cannot parse {DATA_JS}")
    return json.loads(match.group(1))


def normalize(item: dict) -> dict | None:
    if not isinstance(item, dict):
        return None
    title = str(item.get("title") or "").strip()
    article_id = str(item.get("id") or "").strip()
    if not title or not article_id:
        return None
    return {
        "id": article_id,
        "category": str(item.get("category") or "随笔").strip() or "随笔",
        "date": str(item.get("date") or "").strip(),
        "title": title,
        "body": "" if item.get("body") is None else str(item.get("body")),
    }


def main() -> None:
    ARTICLES.mkdir(parents=True, exist_ok=True)
    items = [x for x in (normalize(item) for item in load_list()) if x]
    items.sort(key=lambda x: (x.get("date") or "", x.get("id") or ""), reverse=True)
    DATA_JS.write_text(
        "window.__BLANK_ARTICLES = "
        + json.dumps(items, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"wrote {len(items)} articles -> {DATA_JS.relative_to(ROOT)}")
    for item in items:
        print(f"  - {item['id']}  ({item['title']})")


if __name__ == "__main__":
    main()
