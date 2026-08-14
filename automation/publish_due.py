#!/usr/bin/env python3
"""Publish all due posts from automation/queue/posts.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

load_dotenv(ROOT / ".env")

from lib.instagram import publish_carousel  # noqa: E402
from lib.media_host import resolve_public_url  # noqa: E402
from lib.queue import due_posts, mark_status  # noqa: E402


def workspace_root() -> Path:
    return ROOT.parent


def resolve_image(path_str: str) -> Path:
    p = Path(path_str)
    if p.is_absolute():
        return p
    return workspace_root() / p


def publish_post(post: dict) -> dict:
    caption = post["caption"]
    urls = []
    for img in post["images"]:
        local = resolve_image(img["path"])
        if not local.exists():
            raise FileNotFoundError(f"Missing image: {local}")
        if img.get("public_url"):
            urls.append(img["public_url"])
        else:
            urls.append(resolve_public_url(local))
    return publish_carousel(urls, caption)


def main() -> int:
    pending = due_posts()
    if not pending:
        print("No posts due.")
        return 0

    for post in pending:
        post_id = post["id"]
        print(f"Publishing {post_id}...")
        try:
            result = publish_post(post)
            mark_status(post_id, "published", {"instagram_media_id": result.get("id")})
            print(f"OK: {post_id} -> media {result.get('id')}")
        except Exception as exc:
            mark_status(post_id, "failed", {"error": str(exc)})
            print(f"FAILED: {post_id} -> {exc}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
