# YouTube Daily Publish — Composio

**Channel:** [AOV @vector-ope](https://www.youtube.com/@vector-ope)  
**Connection:** Composio YouTube `youtube_aid-starve` — ACTIVE  
**Automation draft:** `automation/cursor-automation-youtube.yaml`

## One-time Studio fixes

1. Channel name: `AOV — Art of Vector` (keep handle `@vector-ope`)
2. Replace the leftover "hacker information" description with the bio in `strategy/youtube-faceless-growth.md`
3. Phone-verify the channel at https://www.youtube.com/verify (custom thumbnails 403 until this is done — today's Short used the auto frame)
4. On **both existing videos**, set **Not made for kids** — they are currently marked kids
5. Create playlist: `0-Comp Daily`

## Daily run — HALTED 2026-08-15

Do not save or enable `cursor-automation-youtube.yaml`. Cron is removed. Publish scripts exit immediately while `automation/config.json` `enabled` is false. See `automation/DISABLED.md`.

## Do not

- Pass a raw video URL as `videoFile` (needs Composio `s3key`)
- Publish another "0 competition niches 2026" list
- Leave Made for kids checked
- Mix Korean on-screen text
