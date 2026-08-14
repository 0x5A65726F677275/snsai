#!/usr/bin/env python3
"""Publish queued carousel via Composio CLI helper — run from Cursor Agent with Composio MCP."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUEUE = ROOT / "queue" / "posts.json"

# Public URLs for assets (Higgsfield CDN — Instagram can fetch these)
PUBLIC_URLS = {
    "assets/2026-08-14-carousel-slide1-hook.png": "https://d8j0ntlcm91z4.cloudfront.net/user_3Hp069K5oqOjSuU77Lxx5AcmTpf/hf_20260814_225423_9e207387-2404-492c-9da2-778b29d465f0.png",
    "assets/2026-08-14-trend-dashboard-broll-1x1.png": "https://d8j0ntlcm91z4.cloudfront.net/user_3Hp069K5oqOjSuU77Lxx5AcmTpf/hf_20260814_225304_6efa6d1a-9e21-4beb-8157-bef45d9b6467.png",
}

IG_USER_ID = "27772957595695936"  # @art_of_vector27


def get_due_post() -> dict | None:
    data = json.loads(QUEUE.read_text(encoding="utf-8"))
    for post in data["posts"]:
        if post.get("status") == "scheduled":
            return post
    return None


def build_publish_payload(post: dict) -> dict:
    urls = []
    for img in post["images"]:
        path = img["path"].replace("\\", "/")
        url = img.get("public_url") or PUBLIC_URLS.get(path)
        if url:
            urls.append(url)
    if len(urls) < 2:
        raise RuntimeError(f"Need 2+ public image URLs; got {len(urls)}. Add to PUBLIC_URLS map.")
    return {
        "ig_user_id": IG_USER_ID,
        "caption": post["caption"],
        "child_image_urls": urls,
        "post_id": post["id"],
    }


def main() -> int:
    post = get_due_post()
    if not post:
        print("No scheduled post in queue.")
        return 0
    payload = build_publish_payload(post)
    print("COMPOSIO_PUBLISH_PAYLOAD:")
    print(json.dumps(payload, indent=2))
    print("\nRun via Composio MCP:")
    print("  1. INSTAGRAM_CREATE_CAROUSEL_CONTAINER")
    print("  2. INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
