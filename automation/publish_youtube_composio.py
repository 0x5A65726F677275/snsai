#!/usr/bin/env python3
"""Build the Composio payload for today's queued YouTube Short.

Does not upload by itself. The Cloud Agent must:
1. Stage the MP4 into Composio S3 (name + mimetype + s3key)
2. Call YOUTUBE_MULTIPART_UPLOAD_VIDEO
3. Optionally YOUTUBE_UPDATE_THUMBNAIL
4. Remind: uncheck Made for kids in YouTube Studio
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from lib.guard import assert_enabled  # noqa: E402

QUEUE = ROOT / "youtube" / "queue.json"

TAGS = [
    "faceless youtube",
    "composio mcp",
    "youtube shorts upload",
    "0 competition youtube",
    "ai video every day",
    "weak supply seo",
    "art of vector",
    "vector-ope",
    "faceless ai shorts",
    "youtube automation 2026",
]

DESCRIPTION = """I Connected Composio to YouTube and Post a Faceless AI Short Every Day

0 competition is not an empty niche. It is weak supply — old videos, small channels, bad packaging.

Every morning I:
1. Search YouTube with Composio
2. Score the keyword with a 5-filter
3. Generate a faceless AI Short
4. Upload through Composio the same day

No filming. Human POV. Invisible AI.

Subscribe — I post this loop every day on @vector-ope

#FacelessYouTube #Composio #AIShorts #YouTubeSEO #ArtOfVector

Chapters:
0:00 The saturated trap
0:05 Weak supply
0:08 Composio connect
0:12 AI generate + upload

Altered or synthetic content: Yes
"""


def next_ready() -> dict | None:
    data = json.loads(QUEUE.read_text(encoding="utf-8"))
    for video in data.get("videos", []):
        if video.get("status") in {"ready", "generating"} and video.get("video_url"):
            return video
    return None


def main() -> int:
    assert_enabled()
    video = next_ready()
    if not video:
        print("No YouTube video with a public video_url in automation/youtube/queue.json")
        return 1
    payload = {
        "tool": "YOUTUBE_MULTIPART_UPLOAD_VIDEO",
        "title": video["title"],
        "description": DESCRIPTION,
        "categoryId": video.get("category_id", "28"),
        "privacyStatus": video.get("privacy", "public"),
        "tags": TAGS,
        "videoFile": {
            "name": f"{video['id']}.mp4",
            "mimetype": "video/mp4",
            "s3key": "STAGE_VIA_COMPOSIO_WORKBENCH_upload_local_file",
        },
        "thumbnailUrl": video.get("thumbnail_url"),
        "after_upload": [
            "YOUTUBE_UPDATE_THUMBNAIL",
            "YouTube Studio → uncheck Made for kids",
        ],
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
