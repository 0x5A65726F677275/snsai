#!/usr/bin/env python3
"""Daily automation runner — publish due posts, log results."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)


def log(msg: str) -> None:
    line = f"{datetime.now(timezone.utc).isoformat()} {msg}"
    print(line)
    with (LOG_DIR / "daily.log").open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> int:
    sys.path.insert(0, str(ROOT))
    from lib.guard import assert_enabled  # noqa: E402

    from lib.guard import is_enabled  # noqa: E402

    if not is_enabled():
        log("HALTED: automation disabled — no publish")
    assert_enabled()

    env_file = ROOT / ".env"
    if not env_file.exists():
        log("SKIP: automation/.env missing — add IG_USER_ID, IG_ACCESS_TOKEN, IMGBB_API_KEY")
        log("See automation/SETUP.ko.md step 2-3")
        return 2

    sys.path.insert(0, str(ROOT))
    from publish_due import main as publish_main  # noqa: E402

    log("START daily publish")
    code = publish_main()
    log(f"END daily publish exit={code}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
