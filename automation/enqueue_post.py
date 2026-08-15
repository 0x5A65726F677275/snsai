#!/usr/bin/env python3
"""Add a post to the publish queue."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from lib.guard import assert_enabled  # noqa: E402
from lib.queue import enqueue  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Enqueue Instagram carousel post")
    parser.add_argument("--content-file", required=True, help="JSON file with caption + images")
    parser.add_argument(
        "--publish-at",
        required=True,
        help="ISO datetime e.g. 2026-08-15T09:00:00-04:00",
    )
    args = parser.parse_args()
    assert_enabled()

    payload = json.loads(Path(args.content_file).read_text(encoding="utf-8"))
    post = {
        "id": payload.get("id") or str(uuid4()),
        "status": "scheduled",
        "format": "carousel",
        "publish_at": args.publish_at,
        "caption": payload["caption"],
        "images": payload["images"],
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    enqueue(post)
    print(f"Queued: {post['id']} at {post['publish_at']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
