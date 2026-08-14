# SNS AI — Instagram 자동 게시 설정

## 한 줄 요약

| 방식 | PC 켜둬야? | 난이도 |
|------|------------|--------|
| **A. Windows 예약 작업** | ✅ 게시 시각에 ON | 중 |
| **B. Cursor Automation (클라우드)** | ❌ 불필요 | 쉬움 |
| **C. 수동 큐 + 원클릭** | 게시할 때만 | 가장 쉬움 |

---

## A. Windows 예약 작업 (로컬 자동)

### 1. Instagram Business 계정 준비

1. Instagram → **프로페셔널 계정** (Business 또는 Creator)
2. Facebook **페이지** 연결
3. [Meta Developer](https://developers.facebook.com/apps/) → 앱 생성
4. 권한: `instagram_basic`, `instagram_content_publish`, `pages_read_engagement`
5. **장기 Access Token** 발급 → `IG_USER_ID`, `IG_ACCESS_TOKEN` 확보

### 2. 이미지 공개 URL (필수)

Instagram API는 **공개 HTTPS URL**만 받습니다.

**방법 1 — ImgBB (무료, 추천)**

1. https://api.imgbb.com/ 가입
2. API key 복사 → `automation/.env`에 `IMGBB_API_KEY=`

**방법 2 — 자체 CDN**

`PUBLIC_MEDIA_BASE_URL=https://your-cdn.com/sns_ai/` 설정

### 3. 환경 설정

```powershell
cd "c:\Users\Dae Jin Kim\OneDrive\Pictures\sns_ai\automation"
copy .env.example .env
# .env 편집: IG_USER_ID, IG_ACCESS_TOKEN, IMGBB_API_KEY

pip install -r requirements.txt
```

### 4. 예약 작업 등록 (매일 오전 9시)

```powershell
powershell -ExecutionPolicy Bypass -File register_scheduled_task.ps1 -PublishTime "09:00"
```

### 5. 테스트

```powershell
python publish_due.py
```

**⚠️ PC는 매일 9시에 켜져 있어야 합니다.** (절전 모드면 `StartWhenAvailable`로 깨면 후 실행)

---

## B. Cursor Automation (PC 없이 — 추천) ✅ 선택됨

**상세 가이드:** `automation/CURSOR-AUTOMATION-SETUP.md`  
**초안 파일:** `automation/cursor-automation-draft.yaml`

### Agents Window에서 (5분)

1. **Cursor → Agents Window** 열기 (일반 채팅 아님)
2. 아래 메시지 붙여넣기:

```
Create a Cursor Automation from automation/cursor-automation-draft.yaml in my sns_ai workspace.

- Trigger: daily 8:00 AM (cron 0 8 * * *)
- MCP tools: higgsfield, composio
- Enable Cloud Agent so it runs without my PC on
- Instagram account @art_of_vector27 is connected via Composio
```

3. Draft table → **Approve** → **Automations editor**에서 저장

### 테스트 (내일 기다리지 않기)

Agents Window에서:
```
Run the SNS AI daily pipeline now as a test — generate today's carousel and publish to @art_of_vector27
```

---

## C. 게시 큐 (지금 바로 사용)

게시 대기열: `automation/queue/posts.json`

```powershell
# 새 포스트 추가
python enqueue_post.py --content-file queue/2026-08-14-launch.json --publish-at "2026-08-15T09:00:00-04:00"

# 예약 시간 되면 자동 게시
python publish_due.py
```

---

## 매일 자동 흐름 (목표)

```
08:00  트렌드 조사 + 이미지 생성 (Cursor Automation 또는 수동 "오늘 뭐 올릴까?")
       ↓
       queue/posts.json 에 enqueue
09:00  publish_due.py → Instagram API 게시
       ↓
       performance-log.json 업데이트 (수동 또는 다음 Automation)
```

---

## TikTok은?

Higgsfield MCP에 **TikTok 자동 게시** 있음 (`tiktok_connect` → `tiktok_prepare_publish` → `tiktok_publish`).  
Instagram은 Meta API 또는 위 스크립트 사용.

---

## 문제 해결

| 오류 | 해결 |
|------|------|
| `IG_USER_ID` missing | `.env` 파일 생성 |
| ImgBB failed | API key 확인 |
| Container ERROR | 이미지 1:1, 1080px+, JPG/PNG |
| PC 꺼져서 안 올라감 | Cursor Automation(클라우드)으로 전환 |

---

## 다음 단계

1. `automation/.env` 설정 (Meta + ImgBB)
2. `python publish_due.py` 테스트
3. `register_scheduled_task.ps1` 실행
4. (선택) Cursor Automation 생성 — PC 없이 매일
