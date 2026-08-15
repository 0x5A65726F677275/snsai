"""Master kill switch. All publish/enqueue entry points must call this first."""

from __future__ import annotations

import json
import sys
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.json"
HALT_MESSAGE = (
    "HALTED: automation is disabled as of 2026-08-15T04:49:00Z. "
    "No generate / enqueue / publish. Set automation/config.json enabled=true to resume."
)


def is_enabled() -> bool:
    if not CONFIG_PATH.exists():
        return False
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return bool(data.get("enabled"))


def assert_enabled() -> None:
    if not is_enabled():
        print(HALT_MESSAGE, file=sys.stderr)
        raise SystemExit(0)
