# Cursor Automation — Full Auto Setup (Option B)

**Goal:** Every day 8 AM — generate content + images. 9 AM — publish to Instagram. **PC off OK** (cloud agent).

---

## ⚠️ This session cannot open the Automations editor

The Automations editor handoff is only available in the **Agents Window**.

### Do this now (5 minutes)

1. Open **Cursor → Agents Window** (not regular chat)
2. Paste this message:

```
Create a Cursor Automation from automation/cursor-automation-draft.yaml in my sns_ai workspace.

- Trigger: daily 8:00 AM (cron 0 8 * * *)
- MCP tools: higgsfield, composio
- Enable Cloud Agent so it runs without my PC on
- Instagram account @art_of_vector27 is connected via Composio
```

3. When the draft table appears → click **Approve**
4. When asked → **Open Automations editor** and save

---

## Prerequisites checklist

| Step | Status | Action |
|------|--------|--------|
| Higgsfield MCP authenticated | Check Cursor Settings → MCP | Connect if needed |
| Composio MCP authenticated | ✅ Already connected | Instagram `@art_of_vector27` active |
| Cloud Agent enabled | Cursor Dashboard → Cloud Agents | Turn ON |
| GitHub repo (recommended for cloud) | ✅ `0x5A65726F677275/snsai` | Pushed to `main` |

---

## GitHub repo (recommended for cloud agent)

Cloud agents work best with a Git repo. One-time setup:

Repo: **https://github.com/0x5A65726F677275/snsai** (`main` branch)

The automation draft already points at `0x5A65726F677275/snsai` / `main`.

---

## What runs automatically after setup

```
08:00 AM (Cloud)  Cursor Automation starts
                    ↓
                  Trend research (web)
                    ↓
                  Write report + carousel content (English)
                    ↓
                  Higgsfield generate_image (1:1 slides)
                    ↓
                  Enqueue automation/queue/posts.json
                    ↓
                  Composio → Instagram publish

09:00 AM (Local)  Windows task SNS-AI-Instagram-Publish (backup if cloud publish skipped)
```

You can disable the Windows 9 AM task once cloud publish works reliably:

```powershell
Unregister-ScheduledTask -TaskName "SNS-AI-Instagram-Publish" -Confirm:$false
```

---

## Test before waiting until tomorrow

In Agents Window, say:

```
Run the SNS AI daily pipeline now as a test — generate today's carousel and publish to @art_of_vector27
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Automation not in editor | Use Agents Window, not chat |
| MCP blocked in automation | Connect higgsfield + composio in cursor.com dashboard |
| Publish fails | Images need public HTTPS URLs — agent uploads via Composio |
| PC-off but nothing runs | Enable Cloud Agent + GitHub repo |

---

## Files

- `automation/cursor-automation-draft.yaml` — automation prefill
- `automation/queue/posts.json` — publish queue
- `automation/STATUS.md` — current status
