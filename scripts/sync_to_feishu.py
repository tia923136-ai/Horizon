# -*- coding: utf-8 -*-
"""
sync_to_feishu.py — Horizon 采集结果同步到飞书统一表

在 GitHub Actions 中运行，读取 docs/_posts/ 下当天的 summary markdown，
提取标题、链接、评分，写入飞书统一表 tblPie8ayjpjWNuW。

无外部依赖，仅用 urllib。
"""

import os
import re
import json
import time
import hashlib
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path
from typing import Optional

# 飞书配置（从环境变量读取）
APP_ID = os.environ.get("FEISHU_APP_ID", "")
APP_SECRET = os.environ.get("FEISHU_APP_SECRET", "")
BITABLE_APP_TOKEN = os.environ.get("FEISHU_BITABLE_APP_TOKEN", "GsUYbsjPgaQpVYsSJc7cMYFTnCd")
TABLE_ID = os.environ.get("FEISHU_TABLE_ID", "tblPie8ayjpjWNuW")


def get_token() -> Optional[str]:
    if not APP_ID or not APP_SECRET:
        print("[sync] Missing FEISHU_APP_ID or FEISHU_APP_SECRET")
        return None
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    data = json.dumps({"app_id": APP_ID, "app_secret": APP_SECRET}).encode("utf-8")
    try:
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("code") == 0:
                return result.get("tenant_access_token")
            print(f"[sync] Token error: {result}")
    except Exception as e:
        print(f"[sync] Token exception: {e}")
    return None


def check_url_exists(token: str, url: str) -> bool:
    search_url = (
        f"https://open.feishu.cn/open-apis/bitable/v1/apps/"
        f"{BITABLE_APP_TOKEN}/tables/{TABLE_ID}/records/search"
    )
    body = {
        "page_size": 1,
        "filter": {
            "conjunction": "and",
            "conditions": [{"field_name": "链接", "operator": "is", "value": [url]}],
        },
    }
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    try:
        req = urllib.request.Request(search_url, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result.get("data", {}).get("total", 0) > 0
    except Exception:
        return False


def write_record(token: str, fields: dict) -> bool:
    url = (
        f"https://open.feishu.cn/open-apis/bitable/v1/apps/"
        f"{BITABLE_APP_TOKEN}/tables/{TABLE_ID}/records"
    )
    data = json.dumps({"fields": fields}, ensure_ascii=False).encode("utf-8")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=15) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                if result.get("code") == 0:
                    return True
                print(f"[sync] Write error: {result.get('msg')}")
        except Exception as e:
            print(f"[sync] Write exception (attempt {attempt+1}): {e}")
        time.sleep(2**attempt)
    return False


def parse_summary_md(filepath: Path) -> list:
    """从 Horizon summary markdown 提取条目"""
    content = filepath.read_text(encoding="utf-8")
    items = []
    # 按 ## 标题分割
    sections = re.split(r"^## ", content, flags=re.MULTILINE)

    for section in sections:
        match = re.match(r"\[(.+?)\]\((.+?)\)\s*⭐️?\s*([\d.]+)/10", section)
        if not match:
            continue
        title = match.group(1).strip()
        url = match.group(2).strip()
        score = float(match.group(3))

        # 提取摘要（第一段正文）
        lines = section.split("\n")
        summary_lines = []
        for line in lines[1:]:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("<") or line.startswith("**"):
                if summary_lines:
                    break
                continue
            summary_lines.append(line)
        summary = " ".join(summary_lines)[:500]

        # 提取来源（格式: hackernews · author · date）
        source_match = re.search(r"^(\w+)\s*·\s*(.+?)\s*·", section, re.MULTILINE)
        source = source_match.group(1) if source_match else "Horizon"
        author = source_match.group(2).strip() if source_match else ""

        items.append(
            {
                "title": title,
                "url": url,
                "score": score,
                "summary": summary,
                "source": source,
                "author": author,
            }
        )

    return items


def main():
    print("[sync] Horizon -> Feishu unified table")

    token = get_token()
    if not token:
        print("[sync] Failed to get token, exiting")
        return

    # 查找今天的 summary 文件
    docs_dir = Path("docs/_posts")
    if not docs_dir.exists():
        print(f"[sync] {docs_dir} not found")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    files = list(docs_dir.glob(f"{today}-summary*.md"))
    if not files:
        # 找最新的
        files = sorted(docs_dir.glob("*-summary*.md"))
        if files:
            files = [files[-1]]

    if not files:
        print("[sync] No summary files found")
        return

    total_written = 0
    total_skipped = 0

    for filepath in files:
        print(f"[sync] Processing: {filepath.name}")
        items = parse_summary_md(filepath)
        print(f"[sync] Found {len(items)} items")

        for item in items:
            if check_url_exists(token, item["url"]):
                total_skipped += 1
                continue

            fields = {
                "标题": item["title"][:100],
                "链接": item["url"],
                "摘要": item["summary"],
                "来源": item["source"],
                "来源工具": "Horizon",
                "来源渠道": "feedloop",
                "作者": item["author"],
                "内容哈希": hashlib.md5(item["url"].encode()).hexdigest(),
                "采集时间": int(datetime.now().timestamp() * 1000),
                "状态": "待处理",
                "AI评分": item["score"],
            }

            if write_record(token, fields):
                total_written += 1
                print(f"  + {item['title'][:40]}")
            else:
                print(f"  ! Failed: {item['title'][:40]}")

    print(f"\n[sync] Done: written={total_written}, skipped={total_skipped}")


if __name__ == "__main__":
    main()
