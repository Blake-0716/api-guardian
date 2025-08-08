# API Guardian（大學專題）
目標：做一個「API 守衛亭」——登入驗證、權限管控、限流、基本安全掃描，附儀表板與 Demo。

## 里程碑（W1–W12）
- [ ] W1–W2：本機用 Docker 跑起閘道 + 假後端
- [ ] W3–W4：登入拿 Token（JWT），沒 Token 進不來
- [ ] W5–W6：權限（admin/user）
- [ ] W7–W8：限流（同一人每秒最多 10 次）
- [ ] W9–W10：自動安全掃描（CI 失敗就擋）
- [ ] W11–W12：儀表板 + 初稿報告

## 專案結構（持續更新）
api-guardian/
 ├─ docs/                # 放流程圖、設計圖
 ├─ gateway/             # 守衛亭設定（稍後加）
 ├─ services/            # 假後端/認證服務（稍後加）
 ├─ .gitignore
 └─ README.md

## 開發環境
- Docker Desktop
- Git

## 成果清單（之後會放連結）
- Demo 影片（YouTube）
- 架構圖（docs/architecture.png）
- 技術報告（PDF）
