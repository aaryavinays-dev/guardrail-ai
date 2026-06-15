# GuardRail AI

## Enterprise AI Governance & Prompt Security Gateway

GuardRail AI is an enterprise-focused AI governance platform designed to inspect, secure, optimize, and control prompts before they reach external AI providers such as OpenAI GPT, Claude, Gemini, Copilot, and open-source LLMs.

The platform acts as a governance layer between users and AI systems, helping organizations reduce AI costs, prevent sensitive data exposure, enforce security policies, and improve visibility into AI usage.

---

# Problem Statement

Organizations are rapidly adopting Generative AI across departments.

However, prompts often contain:

* Personally Identifiable Information (PII)
* Sensitive business information
* Passwords and credentials
* API keys and secrets
* Prompt injection attempts
* Unnecessary prompt fluff
* Repeated context and redundant text

These issues create:

* Increased AI spending
* Security vulnerabilities
* Compliance risks
* Data leakage concerns
* Poor governance and visibility

Most organizations currently send prompts directly to AI providers without any inspection or security layer.

GuardRail AI aims to solve this problem by acting as a protective gateway that analyzes, scores, and governs prompts before they reach external AI systems.

---

# Current System Capabilities

The current system accepts prompts through a FastAPI API, performs prompt analysis and risk detection, calculates security scores, applies governance decisions, and stores audit records for traceability.

---

# Current System Metrics

| Metric             | Value                       |
| ------------------ | --------------------------- |
| Current Version    | v2.1                        |
| Detection Modules  | 7                           |
| Risk Levels        | 4                           |
| Decision Actions   | 3                           |
| API Endpoints      | 2                           |
| Audit Logging      | Enabled                     |
| Architecture Style | Modular FastAPI Application |

---

# Current Architecture

```text
User Prompt
    ↓
FastAPI API Layer (main.py)
    ↓
Detection Engine (detectors.py)
    ├── Email Detection
    ├── Phone Detection
    ├── SSN Detection
    ├── Credit Card Detection
    ├── Password Detection
    ├── API Key Detection
    └── Prompt Injection Detection
    ↓
Risk Scoring Engine (scoring.py)
    ├── Risk Weight Dictionary
    ├── Risk Classification
    └── Decision Engine
    ↓
Audit Logging Engine (audit_logger.py)
    └── audit_log.txt
    ↓
API Response
```

---

# Project Structure

```text
guardrail-ai/
│
├── main.py
├── detectors.py
├── scoring.py
├── audit_logger.py
├── README.md
├── audit_log.txt
│
├── docs/
│   ├── architecture_v1.md
│   └── changelog.md
│
└── screenshots/
    ├── v1.0_mvp/
    ├── v1.1_refactor/
    ├── v1.2_credit_card/
    ├── v1.3_api_key/
    ├── v1.4_decision_engine/
    ├── v1.5_password_detection/
    ├── v1.6_prompt_injection/
    ├── v1.7_prompt_injection_v2/
    ├── v1.8_risk_weight_dictionary/
    ├── v2.0_audit_logging/
    └── v2.1_project_refactor/
```

---

# Features

## Prompt Analytics

* Word Count
* Character Count
* Character Count Without Spaces
* Uppercase Transformation
* Lowercase Transformation
* Reverse Prompt Transformation
* No-Space Prompt Transformation

---

## Prompt Optimization

GuardRail AI removes common prompt fluff, including:

* Best regards
* Sincerely
* Thank you
* Please kindly

Outputs:

* Estimated Tokens
* Optimized Tokens
* Tokens Saved

---

## Sensitive Data Detection

### Email Detection

Example:

```text
test@gmail.com
```

### Phone Detection

Example:

```text
734-555-1234
```

### SSN Detection

Example:

```text
123-45-6789
```

### Credit Card Detection

Supported Formats:

```text
4111-1111-1111-1111
4111 1111 1111 1111
4111111111111111
```

### Password Detection

Example:

```text
Password: hello123
```

### API Key Detection

Example:

```text
sk-xxxxxxxxxxxxxxxx
```

### Prompt Injection Detection

Detects patterns such as:

```text
Ignore previous instructions
Reveal system prompt
Bypass policy
Forget your rules
```

---

# Risk Scoring Engine

## Risk Weights

| Detection        | Score |
| ---------------- | ----- |
| Email            | 20    |
| Phone            | 20    |
| SSN              | 50    |
| Credit Card      | 50    |
| Password         | 100   |
| API Key          | 100   |
| Prompt Injection | 100   |

---

## Risk Levels

| Score | Risk Level |
| ----- | ---------- |
| 0-20  | LOW        |
| 21-50 | MEDIUM     |
| 51-99 | HIGH       |
| 100+  | CRITICAL   |

---

# Decision Engine

Based on calculated risk score:

| Risk Score | Action |
| ---------- | ------ |
| 0-20       | ALLOW  |
| 21-99      | WARN   |
| 100+       | BLOCK  |

The decision engine simulates enterprise governance policies before prompts are sent to external AI systems.

---

# Audit Logging System

Every analyzed prompt generates an audit record containing:

* Timestamp
* Original Prompt
* Risk Score
* Risk Level
* Action Taken
* Risk Reasons

Example:

```text
Timestamp: 2026-06-07 10:30:00

Prompt:
test@gmail.com Password: hello123

Risk Score:
120

Risk Level:
CRITICAL

Action:
BLOCK

Risk Reasons:
Password detected
```

Benefits:

* Auditability
* Traceability
* Governance Visibility
* Security Monitoring

---

## Pydantic Validation Layer

Implemented Pydantic models to validate incoming API requests and outgoing API responses.

### Added Models

- `PromptRequest`
  - Validates that incoming requests contain a `prompt` field.
  - Ensures `prompt` is treated as a string before business logic runs.

- `RiskResponse`
  - Defines the structure of the `/analyze` API response.
  - Ensures the response contains risk score, risk level, action, optimization metrics, and risk reasons.

### Why This Matters

This adds a validation layer before the GuardRail AI risk engine runs. Invalid or incomplete requests are rejected automatically by FastAPI/Pydantic, preventing bad data from entering the detection and scoring pipeline.

- Structured JSON Audit Logging
- Persistent Audit History Tracking

- Audit summary endpoint for reporting and analytics
- List comprehension-based risk score extraction
- High-risk and critical audit log filtering

### GET /audit-summary

Returns audit analytics from stored JSON audit logs.

Example response:

```json
{
  "total_logs": 2,
  "risk_scores": [50, 0],
  "risk_levels": ["MEDIUM", "LOW"],
  "high_risk_count": 1,
  "critical_count": 0,
  "high_risk_logs": []
}

### Configuration Management

- Environment variable support using python-dotenv
- Externalized application configuration
- Configurable audit log file path
- Configurable risk threshold
- Production-ready configuration pattern

# Core Engineering Concepts Demonstrated

* Modular Application Architecture
* Separation of Concerns
* Single Responsibility Principle
* Risk-Based Decision Systems
* Pattern Matching with Regular Expressions
* Audit Logging and Traceability
* REST API Design
* Secure Prompt Inspection
## Environment Variables

Create a `.env` file in the project root:

```env
APP_NAME=GuardRail AI
APP_VERSION=2.5
RISK_THRESHOLD=50
AUDIT_LOG_FILE=logs/audit_log.json

---

- Exception handling for corrupted audit logs and invalid environment configuration
- Logging for audit file failures
Implemented exception handling and logging to improve backend reliability, error recovery, and operational visibility.
# Tech Stack

## Backend

* Python
* FastAPI
* Uvicorn

## Security

* Regular Expressions (Regex)
* Prompt Injection Detection
* Risk Scoring Engine

## Development

* Git
* GitHub

---

# API Endpoints

## GET /

Health Check Endpoint

Response:

```json
{
  "message": "GuardRail AI is running"
}
```

---

## POST /analyze

Request:

```json
{
  "prompt": "My email is test@gmail.com and my SSN is 123-45-6789"
}
```

Example Response:

```json
{
  "risk_level": "HIGH",
  "risk_score": 70,
  "action": "WARN",
  "risk_reasons": [
    "Email detected",
    "SSN detected"
  ]
}
```

---

# Running Locally

Install Dependencies:

```bash
pip install fastapi uvicorn
```

Run Application:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# Version History

## v1.0

* Initial FastAPI MVP
* Prompt Analytics
* Token Estimation

## v1.1

* Refactored detection logic into reusable helper functions

## v1.2

* Credit Card Detection
* Enhanced Regex Detection

## v1.3

* API Key Detection

## v1.4

* Decision Engine
* ALLOW / WARN / BLOCK Actions

## v1.5

* Password Detection

## v1.6

* Prompt Injection Detection

## v1.7

* Enhanced Prompt Injection Detection

## v1.8

* Centralized Risk Weight Dictionary

## v2.0

* Audit Logging System
* Timestamp Tracking
* Persistent Prompt History

## v2.1

* Modular Architecture Refactor
* Added detectors.py
* Added scoring.py
* Added audit_logger.py
* Simplified main.py responsibilities
* Introduced separation of concerns

---

# Lessons Learned

Version 2.1 introduced the first major architectural refactor.

Key concepts implemented:

* Python Modules
* Cross-File Imports
* Separation of Concerns
* Refactoring Without Breaking Existing Functionality
* Backend Code Organization
* Single Responsibility Principle
* Audit Logging Architecture

---

# Future Roadmap

## Phase 2 (Current Next Milestone)

* PostgreSQL Integration
* SQLAlchemy ORM
* Structured Audit Database
* Database CRUD Operations
* Queryable Audit History

## Phase 3

* User Authentication
* Role-Based Access Control (RBAC)
* Admin Dashboard
* Analytics Dashboard

## Phase 4

* OpenAI Integration
* Claude Integration
* Gemini Integration
* Multi-Model Routing

## Phase 5

* RAG Knowledge Base
* Document Analysis
* Compliance Engine
* Enterprise Policy Management

## Phase 6

* Workflow Agents
* Human-in-the-Loop Reviews
* Cloud Deployment
* Enterprise AI Governance Platform

---

# Long-Term Vision

GuardRail AI aims to become an enterprise AI gateway that:

* Prevents sensitive data leakage
* Reduces AI token waste
* Enforces governance policies
* Tracks AI usage and costs
* Maintains audit trails
* Routes requests across multiple AI providers
* Provides security, compliance, and observability for enterprise AI systems
