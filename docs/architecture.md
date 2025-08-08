# Architecture (v0)
User --> [API Gateway (守衛亭)] --> Backend Service
             | 認證/授權 (先用 API-Key，之後換 JWT)
             | 限流 (Rate limit)
             v
           日誌/監控（之後接儀表板）
