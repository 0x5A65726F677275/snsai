# Cursor Automation 설정 — @art_of_vector27

**PC 꺼도 됩니다.** Cloud Agent가 매일 자동 실행합니다.

---

## 1단계 — Agents Window 열기

Cursor → **Agents Window** (일반 채팅 ❌)

---

## 2단계 — 아래 메시지 복사해서 붙여넣기

```
Create a Cursor Automation from automation/cursor-automation-draft.yaml in my sns_ai workspace.

Requirements:
- Trigger: every day 8:00 AM Eastern (cron 0 8 * * *)
- Enable Cloud Agent (runs without my PC on)
- MCP tools: higgsfield, composio
- Instagram: @art_of_vector27 (Composio already connected, ig_user_id 27772957595695936)
- English only, 1:1 image carousels, no video
- Never use @snsai
```

---

## 3단계 — Approve → Save

Draft table 나오면 **Approve** → **Automations editor**에서 **Save**

---

## 4단계 — Cloud Agent 켜기

[Cursor Dashboard → Cloud Agents](https://cursor.com/dashboard?tab=cloud-agents) → **Enable**

---

## 5단계 — MCP 연결 확인

[Cursor Settings → MCP](https://cursor.com/settings) 에서:
- ✅ **higgsfield** — connected
- ✅ **composio** — connected (Instagram `@art_of_vector27`)

---

## 6단계 — Windows 예약 작업 끄기 (중복 방지)

PowerShell:
```powershell
Unregister-ScheduledTask -TaskName "SNS-AI-Instagram-Publish" -Confirm:$false
```
→ Cursor Automation만 사용 (Windows 작업은 Composio 못 씀)

---

## 7단계 — 테스트 (내일 기다리지 않기)

Agents Window:
```
Run the art of vector daily Instagram pipeline now as a test.
Fresh trend research → 1:1 carousel → publish to @art_of_vector27 via Composio.
```

---

## 매일 자동 흐름

```
08:00 AM (Cloud)  트렌드 조사 (실시간 web search)
                    ↓
                  콘텐츠 + 캡션 작성 (English)
                    ↓
                  Higgsfield 1:1 이미지 생성
                    ↓
                  Composio → @art_of_vector27 게시
                    ↓
                  automation/logs/daily.log 기록
```

**PC:** 꺼도 됨 ✅

---

## 로그 / 큐 확인

| 파일 | 내용 |
|------|------|
| `automation/logs/daily.log` | 게시 성공/실패 |
| `automation/queue/posts.json` | 게시 기록 |
| `reports/YYYY-MM-DD-trend-report.md` | 매일 트렌드 |

---

## 문제 해결

| 문제 | 해결 |
|------|------|
| Automation editor 안 열림 | **Agents Window**에서 실행 (일반 채팅 X) |
| MCP missing | cursor.com/settings → MCP 연결 |
| 게시 실패 | 이미지 public URL 필요 — Higgsfield CDN URL 사용 |
| @snsai 나옴 | draft yaml 업데이트됨 — 다시 import |

---

## 초안 파일

`automation/cursor-automation-draft.yaml`
