"""Post queue for scheduled Instagram publishing."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .guard import is_enabled

QUEUE_PATH = Path(__file__).resolve().parent.parent / "queue" / "posts.json"


def load_queue() -> dict[str, Any]:
    if not QUEUE_PATH.exists():
        return {"posts": []}
    return json.loads(QUEUE_PATH.read_text(encoding="utf-8"))


def save_queue(data: dict[str, Any]) -> None:
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUEUE_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def enqueue(post: dict[str, Any]) -> None:
    if not is_enabled():
        raise RuntimeError("HALTED: automation disabled — will not enqueue")
    data = load_queue()
    data["posts"].append(post)
    save_queue(data)


def due_posts(now: datetime | None = None) -> list[dict[str, Any]]:
    if not is_enabled():
        return []
    now = now or datetime.now(timezone.utc)
    data = load_queue()
    due = []
    for post in data["posts"]:
        if post.get("status") != "scheduled":
            continue
        publish_at = datetime.fromisoformat(post["publish_at"].replace("Z", "+00:00"))
        if publish_at <= now:
            due.append(post)
    return due


def mark_status(post_id: str, status: str, extra: dict | None = None) -> None:
    data = load_queue()
    for post in data["posts"]:
        if post["id"] == post_id:
            post["status"] = status
            post["updated_at"] = datetime.now(timezone.utc).isoformat()
            if extra:
                post.update(extra)
            break
    save_queue(data)
