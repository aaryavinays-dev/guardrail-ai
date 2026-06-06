Current Architecture

User Prompt
      |
      v
FastAPI API
      |
      v
Detection Engine
      |
      +--> Email Detection
      +--> SSN Detection
      +--> Phone Detection
      +--> Credit Card Detection
      +--> Password Detection
      +--> API Key Detection
      +--> Prompt Injection Detection
      |
      v
Risk Scoring Engine
      |
      v
Decision Engine
(ALLOW / WARN / BLOCK)
      |
      v
Audit Logging System
(audit_log.txt)