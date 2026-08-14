"""Instagram Graph API — carousel publish."""

from __future__ import annotations

import os
import time
from typing import Iterable

import requests

GRAPH = "https://graph.facebook.com"
API_VERSION = os.getenv("GRAPH_API_VERSION", "v21.0")


def _post(path: str, params: dict) -> dict:
    resp = requests.post(f"{GRAPH}/{API_VERSION}/{path}", data=params, timeout=120)
    resp.raise_for_status()
    return resp.json()


def _get(path: str, params: dict) -> dict:
    resp = requests.get(f"{GRAPH}/{API_VERSION}/{path}", params=params, timeout=60)
    resp.raise_for_status()
    return resp.json()


def _wait_container(container_id: str, token: str, timeout_sec: int = 120) -> None:
    deadline = time.time() + timeout_sec
    while time.time() < deadline:
        data = _get(
            container_id,
            {"fields": "status_code", "access_token": token},
        )
        status = data.get("status_code")
        if status == "FINISHED":
            return
        if status == "ERROR":
            raise RuntimeError(f"Container {container_id} failed: {data}")
        time.sleep(3)
    raise TimeoutError(f"Container {container_id} not ready after {timeout_sec}s")


def publish_carousel(
    image_urls: Iterable[str],
    caption: str,
    ig_user_id: str | None = None,
    access_token: str | None = None,
) -> dict:
    ig_user_id = ig_user_id or os.environ["IG_USER_ID"]
    access_token = access_token or os.environ["IG_ACCESS_TOKEN"]
    urls = list(image_urls)
    if not urls:
        raise ValueError("At least one image URL required")
    if len(urls) > 10:
        raise ValueError("Instagram carousel max 10 items")

    child_ids = []
    for url in urls:
        child = _post(
            f"{ig_user_id}/media",
            {
                "image_url": url,
                "is_carousel_item": "true",
                "access_token": access_token,
            },
        )
        _wait_container(child["id"], access_token)
        child_ids.append(child["id"])

    if len(child_ids) == 1:
        parent = _post(
            f"{ig_user_id}/media",
            {
                "image_url": urls[0],
                "caption": caption,
                "access_token": access_token,
            },
        )
    else:
        parent = _post(
            f"{ig_user_id}/media",
            {
                "media_type": "CAROUSEL",
                "caption": caption,
                "children": ",".join(child_ids),
                "access_token": access_token,
            },
        )

    _wait_container(parent["id"], access_token)
    published = _post(
        f"{ig_user_id}/media_publish",
        {"creation_id": parent["id"], "access_token": access_token},
    )
    return published
