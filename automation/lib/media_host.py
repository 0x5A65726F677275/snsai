"""Upload local images to public URLs for Instagram Graph API."""

from __future__ import annotations

import base64
import os
from pathlib import Path

import requests


def upload_imgbb(image_path: Path, api_key: str) -> str:
    with image_path.open("rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    resp = requests.post(
        "https://api.imgbb.com/1/upload",
        data={"key": api_key, "image": encoded},
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    if not data.get("success"):
        raise RuntimeError(f"ImgBB upload failed: {data}")
    return data["data"]["url"]


def resolve_public_url(image_path: Path) -> str:
    base = os.getenv("PUBLIC_MEDIA_BASE_URL", "").rstrip("/")
    if base:
        rel = image_path.as_posix().split("/assets/")[-1]
        return f"{base}/assets/{rel}"

    api_key = os.getenv("IMGBB_API_KEY", "")
    if not api_key:
        raise RuntimeError(
            "Set IMGBB_API_KEY or PUBLIC_MEDIA_BASE_URL in automation/.env"
        )
    return upload_imgbb(image_path, api_key)
