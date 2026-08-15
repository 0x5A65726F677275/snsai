# Automation HALTED — 2026-08-15

User request: stop all automation from this moment.

| Switch | Value |
|--------|--------|
| `automation/config.json` → `enabled` | **false** |
| `config/account-profile.json` → `automation.enabled` | **false** |
| Instagram daily YAML cron | removed |
| YouTube daily YAML cron | removed |
| Publish / enqueue scripts | exit 0 immediately |
| Cursor agent rules | do not auto-research / generate / publish |

Resume later: set both `enabled` flags to `true`, restore cron in the YAML drafts, and re-save Cursor Automation only if you want cloud runs again.

Windows PC (if the old task was registered):

```powershell
Unregister-ScheduledTask -TaskName "SNS-AI-Instagram-Publish" -Confirm:$false
```

Or run `automation/unregister_scheduled_task.ps1`.
