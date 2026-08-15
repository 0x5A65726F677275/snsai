# Grow a Faceless YouTube Channel — 0-Comp AI Video Every Day

**Channel:** AOV ([@vector-ope](https://www.youtube.com/@vector-ope))  
**Channel ID:** `UCzkwbcy4d8HlHzImkreOQQQ`  
**Publish:** Composio YouTube (ACTIVE)  
**Generate:** Higgsfield `seedance_2_5` Shorts + `faceless-channel-video` for search  
**Language:** English only  
**Locked:** 2026-08-15

This is a **YouTube-only** growth system. Instagram stays separate.

---

## Channel audit (live, 2026-08-15)

| Field | Value | Action |
|-------|-------|--------|
| Subscribers | 0 | First 30 public Shorts decide the niche |
| Views | 0–1 | No baseline — do not invent metrics |
| Uploads | 2 motion tests | Reposition as operator / 0-comp series |
| `AOV CHARGER` | private, **made for kids** | Uncheck kids in Studio — kids mode kills comments + ads |
| `A architect...` | public, **made for kids**, 1 view | Same — flip kids off |
| Channel description | leftover "hacker information" copy | Replace with English operator bio (below) |
| Custom URL | `@vector-ope` | Keep; add "Art of Vector" in the channel name |

**Paste this channel description (English):**

> Daily faceless AI videos for creators. I find weak-supply YouTube keywords, generate the video with AI, and upload through Composio the same morning. Human POV. Invisible AI. No filming.

---

## The growth math (new faceless channel)

YouTube gives a new channel **two doors**:

| Door | Surface | What wins | Cadence |
|------|---------|-----------|---------|
| **Browse** | Shorts shelf | Hook in 1s, 80%+ viewed, daily | 1 Short / day (required) |
| **Search** | Results page | Weak supply + better packaging | 1 search video / day when credits allow |

0-competition is a **search** game. Shorts is how strangers find you before you have authority.

**Rule:** never publish another "20 niches with 0 competition" list. That query is 🧊 SATURATED (Steffen Miro posted a new one 2026-08-14). Teach the **filter**, then prove it with a keyword nobody packaged.

North star: **subs per 1,000 views**. Secondary: Shorts % viewed, search CTR, average view duration.

---

## What "0 competition" means (live test)

Empty niches have no demand. **Weak supply** is the target.

Live Composio scan, 2026-08-15:

| Keyword | Supply | Verdict |
|---------|--------|---------|
| how to grow a faceless youtube channel with AI 2026 | 550K results, big gurus | 🧊 SATURATED — do not rank this |
| 0 competition youtube keywords / niches 2026 | listicle wall (Steffen Miro, vidIQ clones) | 🧊 SATURATED |
| how to upload YouTube Shorts with Composio MCP | MCP explainers only — **no daily upload tutorial** | 🔥 NOW — 0-comp lane |
| Cursor agent posts YouTube Shorts every day | n8n / ChatGPT adjacent, no Cursor+Composio loop | 🔥 NOW |

**Today's locked keyword:** `how to upload YouTube Shorts with Composio MCP`  
**Title:** `I Connected Composio to YouTube and Post a Faceless AI Short Every Day`

---

## Daily operator loop (YouTube only)

Run at **08:00 America/New_York** via Cursor Automation + Composio.

1. **Search 3 long-tails** with `YOUTUBE_SEARCH_YOU_TUBE` (maxResults 10, order relevance, en, US).
2. **Score** each with the 5-filter (must pass 4/5) — see `strategy/youtube-0-competition-system.md`.
3. **Lock one keyword** that is NOT a niche-list video.
4. **Generate** a 12–20s 9:16 faceless Short (`seedance_2_5`, English VO + on-screen text).
5. **Generate** a 16:9 thumbnail (`nano_banana_pro`, English headline 3–5 words).
6. **Stage** the MP4 into Composio S3 (`upload_local_file` / workbench).
7. **Upload** with `YOUTUBE_MULTIPART_UPLOAD_VIDEO`:
   - `privacyStatus`: `public` (user asked for daily growth posts)
   - `categoryId`: `28` (Science & Technology)
   - title + description + tags from the content package
8. **Thumbnail** with `YOUTUBE_UPDATE_THUMBNAIL` (channel must be phone-verified).
9. **In YouTube Studio:** uncheck Made for kids. The upload API used here does not expose that flag — existing AOV videos are wrongly marked kids.
10. **Log** video ID, keyword score, and later CTR / % viewed into `automation/youtube/queue.json`.

Never pass a raw HTTPS URL as `videoFile`. Composio needs `{name, mimetype, s3key}`.

---

## 30-day growth plan (0 → first 1,000 subs)

### Days 1–7 — Prove the loop
- 1 public Short / day in the Composio / operator / weak-supply lane
- Same visual system every day (dark / violet / cyan, giant number or filter card)
- Pin comment: "Tomorrow's keyword is scored at 8am ET"
- Do not change niche mid-week

### Days 8–14 — Add search
- Keep daily Shorts
- Add one 8–12 min faceless explainer on the week's best 0-comp keyword
- Playlist: "0-Comp Daily"

### Days 15–30 — Double down
- Kill any lane with CTR < 4% after 1,000 impressions
- Repeat winning title patterns
- End screens: Short → search video in the same lane

Success at day 30: 1,000+ subs **or** one Short with 10K+ views and >2 subs / 1K views. If neither, the packaging is wrong — not the tool stack.

---

## Made-for-kids warning

Both current AOV uploads are `selfDeclaredMadeForKids: true`. That:

- disables most comments
- blocks the browse features you need
- tanks RPM later

Fix in YouTube Studio → each video → Details → "No, it's not made for kids."  
New daily uploads: set the same immediately after Composio publish.

---

## Composio tools used

| Step | Tool |
|------|------|
| Keyword research | `YOUTUBE_SEARCH_YOU_TUBE` |
| Channel health | `YOUTUBE_GET_CHANNEL_STATISTICS` (`mine: true`) |
| Inventory | `YOUTUBE_LIST_CHANNEL_VIDEOS` (`mine: true`) |
| Enrich | `YOUTUBE_GET_VIDEO_DETAILS_BATCH` |
| Upload | `YOUTUBE_MULTIPART_UPLOAD_VIDEO` |
| Fallback upload | `YOUTUBE_UPLOAD_VIDEO` |
| Thumbnail | `YOUTUBE_UPDATE_THUMBNAIL` |
| Metadata fix | `YOUTUBE_UPDATE_VIDEO` |

Connection alias: `youtube_aid-starve` (ACTIVE as of 2026-08-15).
