# Current Architecture

## Backend File Responsibilities

```text
main.py
├── receives API requests through FastAPI
├── sends user prompts to PromptAnalyzer
├── applies risk scoring logic from scoring.py
├── applies decision logic: ALLOW / WARN / BLOCK
└── writes audit records using audit_logger.py
```

```text
prompt_analyzer.py
└── coordinates detection logic from detectors.py
```

```text
detectors.py
├── Email Detection
├── SSN Detection
├── Phone Detection
├── Credit Card Detection
├── Password Detection
├── API Key Detection
└── Prompt Injection Detection
```

```text
scoring.py
└── calculates the risk score based on detected sensitive data and prompt risk signals
```

```text
audit_logger.py
└── stores JSON-formatted audit records in the configured audit log file
```
redactor.py
└── redacts sensitive values before API response and audit persistence

enums.py
└── defines controlled values for RiskLevel and Action

---

## Request Processing Flow

```text
User Prompt
    |
    v
FastAPI API
    |
    v
Prompt Analyzer
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
    |
    +--> ALLOW
    +--> WARN
    +--> BLOCK
    |
    v
Audit Logging System
```

---

## Audit Logging Flow

```text
Client Request
    |
    v
Prompt Analysis
    |
    v
Risk Detection Results
    |
    v
Risk Score and Decision
    |
    v
Audit Record Dictionary
    |
    v
Write JSON-formatted record to audit log file
```

---

## Configuration Layer

The application uses environment variables for runtime configuration.

Examples:

```text
APP_NAME
APP_VERSION
RISK_THRESHOLD
AUDIT_LOG_FILE
```

Environment variables are loaded using `python-dotenv` and accessed using `os.getenv()`.

This allows the application to change runtime behavior without hardcoding values directly inside the source code.

## PostgreSQL Integration Architecture

GuardRail AI now uses PostgreSQL as the persistent audit storage layer.

Current architecture:

```text
Client / Swagger UI
        ↓
FastAPI Endpoint: /analyze
        ↓
PromptAnalyzer
        ↓
RiskScorer
        ↓
Redactor
        ↓
Audit Repository
        ↓
SQLAlchemy Session
        ↓
PostgreSQL audit_logs table
```

Database-related files:

```text
database.py
- Loads DATABASE_URL from .env
- Creates SQLAlchemy engine
- Creates SessionLocal
- Provides get_db() dependency for FastAPI

db_models.py
- Defines the AuditLog SQLAlchemy model
- Maps the Python class to the PostgreSQL audit_logs table

audit_repository.py
- Saves analyzed prompt results into PostgreSQL
- Generates audit summary data from PostgreSQL
```

Security note:

Only redacted prompts are stored in PostgreSQL. Raw sensitive values such as emails, SSNs, passwords, phone numbers, credit cards, and API keys should not be persisted in the audit table.

