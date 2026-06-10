Current Architecture

main.py
├── imports detection logic from detectors.py
├── imports scoring logic from scoring.py
└── imports audit logging from audit_logger.py

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

Audit Logging Flow

Client Request
      ↓
Prompt Analysis
      ↓
Risk Detection
      ↓
Audit Record Dictionary
      ↓
Append To Audit Log List
      ↓
JSON File Persistence

### Configuration Layer

The application uses environment variables for runtime configuration.

Examples:

- APP_NAME
- APP_VERSION
- RISK_THRESHOLD
- AUDIT_LOG_FILE

Environment variables are loaded using `python-dotenv` and accessed via `os.getenv()`.