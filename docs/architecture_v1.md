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
