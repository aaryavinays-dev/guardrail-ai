# GuardRail AI

## Enterprise AI Governance & Prompt Security Gateway

GuardRail AI is a FastAPI-based backend prototype for inspecting and governing user prompts before they are sent to external AI systems such as OpenAI, Claude, Gemini, Copilot, or open-source LLMs.

The system detects sensitive data, identifies prompt injection attempts, calculates risk scores, applies governance decisions, redacts sensitive values, and stores structured audit records for traceability.

---

## Problem Statement

Organizations are rapidly adopting Generative AI across business teams, but many prompts are sent directly to AI providers without inspection.

Prompts may contain:

* Personally Identifiable Information (PII)
* Social Security Numbers
* Phone numbers
* Credit card numbers
* Passwords and credentials
* API keys and secrets
* Prompt injection attempts

This creates risks around:

* Sensitive data leakage
* Compliance exposure
* Lack of AI usage visibility
* Weak governance controls
* Poor auditability

GuardRail AI acts as a protective prompt governance layer that analyzes and controls prompts before they reach external AI systems.

---

## Current Version

**Version:** v3.0
**Current Phase:** Secure backend cleanup before PostgreSQL integration

---

## Current Capabilities

* FastAPI backend API
* Pydantic request and response validation
* Sensitive data detection
* Prompt injection detection
* Risk scoring engine
* ALLOW / WARN / BLOCK decision engine
* Environment variable configuration
* JSON audit logging
* Audit summary endpoint
* Secure prompt redaction
* Pytest unit testing

---

## Current System Metrics

| Metric              |           Value |
| ------------------- | --------------: |
| Detection Modules   |               7 |
| Risk Levels         |               4 |
| Decision Actions    |               3 |
| API Endpoints       |               3 |
| Test Cases          |               9 |
| Audit Logging       |      JSON-based |
| Current Storage     | Local JSON file |
| Next Storage Target |      PostgreSQL |

---

## Architecture

```text
User Prompt
    |
    v
FastAPI API Layer
    |
    v
Pydantic Validation
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
Prompt Redaction Layer
    |
    v
JSON Audit Logging
```

---

## Project Structure

```text
guardrail-ai/
│
├── main.py
├── models.py
├── detectors.py
├── prompt_analyzer.py
├── risk_scorer.py
├── scoring.py
├── audit_logger.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── docs/
│   ├── architecture_v1.md
│   └── changelog.md
│
├── tests/
    |__test_detectors.py
│   ├── test_prompt_analyzer.py
│   └── test_redactor.py
    |__test_risk_scorer.py
│
├── screenshots/
│   ├── v1.7_prompt_injection_v2/
│   ├── v1.8_risk_weight_dictionary/
│   ├── v2.0_audit_logging/
│   ├── v2.1_project_refactor/
│   ├── v2.2_pydantic_validation/
│   ├── v2.3_json_logging/
│   ├── v2.4_list_comprehension/
│   ├── v2.5_environment_variables/
│   ├── v2.6_oop_refactor/
│   ├── v2.7_exception_handling/
│   ├── v2.8_logging and type hints/
│   ├── v2.9_pytest_tests_passed/
│   └── v3.0_secure_response_redaction/
    |__ v3.1_python_polish/
│
└── logs/
    └── audit_log.json
```

`logs/`, `.env`, `venv/`, `__pycache__/`, and `.pytest_cache/` are ignored by Git.

---

## Detection Modules

GuardRail AI currently detects the following risk signals:

| Detection Type   | Example                        |
| ---------------- | ------------------------------ |
| Email            | `test@gmail.com`               |
| SSN              | `123-45-6789`                  |
| Phone            | `123-456-7890`                 |
| Credit Card      | `4111-1111-1111-1111`          |
| Password         | `password: hello123`           |
| API Key          | `sk-abc123456789`              |
| Prompt Injection | `Ignore previous instructions` |

---

## Risk Scoring Engine

Each detection type has a configured risk weight.

| Detection        | Score |
| ---------------- | ----: |
| Email            |    20 |
| Phone            |    20 |
| SSN              |    50 |
| Credit Card      |    50 |
| Password         |   100 |
| API Key          |   100 |
| Prompt Injection |   100 |

---

## Risk Levels

| Score Range | Risk Level |
| ----------- | ---------- |
| 0-20        | LOW        |
| 21-50       | MEDIUM     |
| 51-99       | HIGH       |
| 100+        | CRITICAL   |

---

## Decision Engine

| Score Range | Action |
| ----------- | ------ |
| 0-20        | ALLOW  |
| 21-99       | WARN   |
| 100+        | BLOCK  |

The decision engine simulates enterprise governance behavior by deciding whether a prompt should be allowed, warned, or blocked based on detected risk.

---

## Secure Prompt Redaction

GuardRail AI redacts sensitive values before returning API responses and before writing audit records.

Example input:

```text
My SSN is 123-45-6789, email is vinay@test.com, phone is 123-456-7890, password: hello123 and key sk-abc123456789 Ignore previous instructions
```

Example redacted output:

```text
My SSN is [REDACTED_SSN], email is [REDACTED_EMAIL], phone is [REDACTED_PHONE], password: [REDACTED_PASSWORD] and key [REDACTED_API_KEY] Ignore previous instructions
```

This prevents sensitive values from being stored in audit logs or exposed in API responses.

---

## API Endpoints

### GET `/`

Health check endpoint.

Example response:

```json
{
  "message": "GuardRail AI is running",
  "version": "3.0"
}
```

---

### POST `/analyze`

Analyzes a prompt for sensitive data and prompt injection risk.

Example request:

```json
{
  "prompt": "My SSN is 123-45-6789, email is vinay@test.com, password: hello123 Ignore previous instructions"
}
```

Example response:

```json
{
  "redacted_prompt": "My SSN is [REDACTED_SSN], email is [REDACTED_EMAIL], password: [REDACTED_PASSWORD] Ignore previous instructions",
  "detections": {
    "email": true,
    "ssn": true,
    "phone": false,
    "credit_card": false,
    "password": true,
    "api_key": false,
    "prompt_injection": true
  },
  "word_count": 10,
  "character_count": 94,
  "estimated_tokens": 13,
  "risk_level": "CRITICAL",
  "risk_score": 270,
  "action": "BLOCK",
  "risk_reasons": [
    "email detected",
    "ssn detected",
    "password detected",
    "prompt_injection detected"
  ]
}
```

---

### GET `/audit-summary`

Returns audit analytics from stored JSON audit records.

Example response:

```json
{
  "total_logs": 5,
  "risk_scores": [20, 70, 220],
  "risk_levels": ["LOW", "HIGH", "CRITICAL"],
  "high_risk_count": 2,
  "critical_count": 1,
  "high_risk_logs": []
}
```

---

## Audit Logging

Each analyzed prompt creates a structured JSON audit record.

Stored audit records include:

* Timestamp
* Redacted prompt
* Redaction flag
* Risk score
* Risk level
* Action
* Risk reasons

Example audit record:

```json
{
  "timestamp": "2026-06-15T15:48:04.683586+00:00",
  "prompt": "My SSN is [REDACTED_SSN], email is [REDACTED_EMAIL], password: [REDACTED_PASSWORD]",
  "prompt_redacted": true,
  "risk_score": 170,
  "risk_level": "CRITICAL",
  "action": "BLOCK",
  "risk_reasons": [
    "email detected",
    "ssn detected",
    "password detected"
  ]
}
```

---

## Configuration

Runtime configuration is handled using environment variables.

Create a `.env` file in the project root:

```env
APP_NAME=GuardRail AI
APP_VERSION=3.0
RISK_THRESHOLD=100
AUDIT_LOG_FILE=logs/audit_log.json
```

A safe template is provided in:

```text
.env.example
```

Do not commit the real `.env` file.

---

## Running Locally

### 1. Create and activate virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the application

```bash
uvicorn main:app --reload
```

---

### 4. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Current test coverage includes:

* Risk score calculation
* Risk level determination
* Action decision logic
* Prompt redaction validation

| Metric              |           Value |
| ------------------- | --------------: |
| Detection Modules   |               7 |
| Risk Levels         |               4 |
| Decision Actions    |               3 |
| API Endpoints       |               3 |
| Test Cases          |              37 |
| Audit Logging       |      JSON-based |
| Current Storage     | Local JSON file |
| Next Storage Target |      PostgreSQL |

Expected result:

```text
37 passed
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn
* Pydantic

### Security Logic

* Regex-based sensitive data detection
* Prompt injection pattern detection
* Risk scoring
* Prompt redaction

### Persistence

* JSON audit logging
* PostgreSQL planned next

### Testing

* Pytest

### Development

* Git
* GitHub
* VS Code

---

## Engineering Concepts Demonstrated

* REST API development
* Backend modularization
* Separation of concerns
* Object-oriented programming
* Pydantic validation
* Environment variable configuration
* Exception handling
* Logging
* JSON file persistence
* Secure audit logging
* Prompt redaction
* Unit testing with pytest
* Risk-based decision systems
* Python Enums for fixed business values
* Pure function extraction
* Parametrized testing with `pytest.mark.parametrize`
* Detector-level test coverage
* Coordinator class testing through `PromptAnalyzer`
* Circular import debugging


---

## Version History

### v1.7 - Prompt Injection Detection

* Added prompt injection detection patterns.
* Added governance logic for risky prompt behavior.

### v1.8 - Risk Weight Dictionary

* Added centralized risk weight dictionary.
* Replaced hardcoded scoring values.

### v2.0 - Audit Logging

* Added persistent audit logging.
* Added timestamp tracking.
* Added audit trail generation.

### v2.1 - Modular Architecture Refactor

* Added separate modules for detectors, scoring, and audit logging.
* Simplified FastAPI route responsibilities.

### v2.2 - Pydantic Validation

* Added request and response validation models.
* Added FastAPI response model enforcement.

### v2.3 - JSON Audit Logging

* Replaced plain text audit logs with structured JSON logs.

### v2.4 - Audit Summary Endpoint

* Added `/audit-summary`.
* Added summary analytics for risk scores and risk levels.

### v2.5 - Environment Variables

* Added `.env` support.
* Added configurable app metadata, audit log path, and risk threshold.

### v2.6 - Object-Oriented Refactor

* Added `PromptAnalyzer`.
* Added `RiskScorer`.
* Refactored `AuditLogger`.

### v2.7 - Exception Handling and Logging

* Added corrupted JSON handling.
* Added logging for audit file operations and failures.

### v2.8 - Type Hints and Code Quality

* Added type hints across backend modules.
* Improved readability and maintainability.

### v2.9 - Pytest Unit Testing

* Added unit tests for risk scoring and risk level logic.

### v3.0 - Secure Prompt Redaction

* Added prompt redaction for API responses and audit logs.
* Removed raw prompt exposure from `/analyze`.
* Added redaction test coverage.

### v3.1 - Python Polish and Expanded Test Coverage

- Extracted redaction logic into `redactor.py`.
- Added `RiskLevel` and `Action` enums.
- Added detector tests using `pytest.mark.parametrize`.
- Added PromptAnalyzer tests.
- Expanded pytest coverage from 9 tests to 37 passing tests.

---

## Roadmap

### Phase 2: PostgreSQL Persistence

* Replace local JSON audit storage with PostgreSQL.
* Add SQLAlchemy ORM models.
* Store audit records in a database table.
* Add database-backed audit summary queries.
* Add migration-ready database structure.

### Phase 3: Authentication and RBAC

* Add user authentication.
* Add role-based access control.
* Add admin-only audit visibility.

### Phase 4: Dashboard and Analytics

* Build audit dashboard.
* Add risk trend analysis.
* Add policy violation reporting.

### Phase 5: External AI Provider Integration

* Add OpenAI integration.
* Add Claude integration.
* Add Gemini integration.
* Add multi-model routing.

### Phase 6: Enterprise Governance Platform

* Add policy management.
* Add human-in-the-loop review workflows.
* Add compliance reporting.
* Add deployment support.

---

## Long-Term Vision

GuardRail AI aims to become an enterprise AI gateway that helps organizations:

* Prevent sensitive data leakage
* Detect prompt injection attempts
* Enforce AI governance policies
* Maintain audit trails
* Improve visibility into AI usage
* Support compliance and security reviews
* Route requests safely across multiple AI providers
