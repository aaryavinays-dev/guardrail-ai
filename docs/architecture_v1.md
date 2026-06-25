# GuardRail AI Architecture

## Overview

GuardRail AI is an enterprise AI governance gateway built with FastAPI, PostgreSQL, SQLAlchemy, Python, React, TypeScript, and Vite.

The system analyzes prompts before AI model invocation, detects sensitive data and prompt injection attempts, applies department-specific governance policies, redacts sensitive values, tracks token and cost usage, estimates blocked cost savings, routes safe prompts through an AI gateway, and stores structured audit logs for enterprise visibility.

The project is designed to demonstrate backend engineering, AI platform thinking, full-stack product implementation, auditability, policy enforcement, and cost-aware AI governance.

---

## High-Level Architecture

```text
React + TypeScript Dashboard
        |
        v
FastAPI API Layer
        |
        v
API Key Authentication
        |
        v
Pydantic Request Validation
        |
        v
Prompt Analyzer
        |
        v
Sensitive Data + Prompt Injection Detectors
        |
        v
Risk Scoring Engine
        |
        v
Department Policy Engine
        |
        v
Final Action: ALLOW / WARN / BLOCK
        |
        +-----------------------------+
        |                             |
        v                             v
BLOCK Response                 Safe Prompt Flow
No Model Call                  Model Routing
        |                             |
        v                             v
Audit Logging                  OpenAI Provider Call
        |                             |
        +-------------+---------------+
                      v
              PostgreSQL audit_logs
```

---

## Core Components

| Component               | File / Folder            | Responsibility                                                                                               |
| ----------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Frontend Dashboard      | `frontend/`              | React + TypeScript dashboard for prompt analysis, gateway testing, department analytics, and audit summaries |
| API Layer               | `main.py`                | Defines `/analyze`, `/gateway`, `/audit-summary`, `/department-summary`, and `/health/db`                    |
| Request/Response Models | `models.py`              | Defines Pydantic schemas for request validation and structured responses                                     |
| Prompt Analyzer         | `prompt_analyzer.py`     | Orchestrates detection, scoring, redaction, and action decision flow                                         |
| Detectors               | `detectors.py`           | Detects emails, SSNs, phone numbers, credit cards, passwords, API keys, and prompt injection attempts        |
| Risk Scorer             | `risk_scorer.py`         | Calculates risk score, risk level, and initial action                                                        |
| Scoring Config          | `scoring.py`             | Stores risk weights for detected signals                                                                     |
| Policy Engine           | `policy_engine.py`       | Applies department-specific governance rules and action overrides                                            |
| Redactor                | `redactor.py`            | Redacts sensitive values before response and storage                                                         |
| Auth                    | `auth.py`                | Validates requests using the `x-api-key` header                                                              |
| Database Config         | `database.py`            | Manages SQLAlchemy engine and database sessions                                                              |
| DB Model                | `db_models.py`           | Defines the PostgreSQL audit log table                                                                       |
| Audit Repository        | `audit_repository.py`    | Saves and queries audit records                                                                              |
| Evaluation Harness      | `evaluation/run_eval.py` | Runs the 28-case guardrail evaluation suite                                                                  |
| Tests                   | `tests/`                 | Contains automated tests for backend behavior                                                                |

---

## Frontend Dashboard

GuardRail AI includes a React + TypeScript dashboard built with Vite. The frontend is intentionally designed as an internal governance dashboard rather than a consumer SaaS interface.

The dashboard provides:

* Prompt Analyzer connected to `POST /analyze`
* Gateway Demo connected to `POST /gateway`
* Department Summary connected to `GET /department-summary`
* Audit Summary connected to `GET /audit-summary`
* Top governance metrics for total logs, blocked prompts, warnings, critical risks, estimated cost, and blocked savings
* Loading states, error states, redacted prompt display, cost formatting, and detection labels

The frontend demonstrates how enterprise teams could analyze prompts, enforce AI usage policies, monitor risk by department, and review audit logs before or after model invocation.

---

## Request Lifecycle: `/analyze`

1. Client sends a prompt, user ID, and department.
2. API key authentication validates the request.
3. Pydantic validates the request body.
4. Prompt analyzer runs sensitive data and prompt injection detectors.
5. Risk scorer calculates risk score, risk level, and initial action.
6. Department policy engine applies governance rules and may override the action.
7. Redactor removes sensitive values from the prompt.
8. Token usage, estimated cost, and blocked savings are calculated.
9. Audit record is saved in PostgreSQL.
10. API returns action, risk score, risk level, detections, redacted prompt, risk reasons, and cost metadata.

---

## Request Lifecycle: `/gateway`

1. Client sends a prompt, user ID, and department.
2. GuardRail AI analyzes prompt risk using the same governance pipeline.
3. Department policy engine applies department-specific and global rules.
4. If the final action is `BLOCK`, the model is not called.
5. If the final action is `ALLOW` or `WARN`, a model is selected.
6. Safe prompts are routed to the selected model.
7. Provider quota, billing, or configuration failures return a controlled fallback response.
8. Audit record is saved in PostgreSQL.

This endpoint demonstrates the main product concept: risky prompts are stopped before model invocation, while safe prompts can continue through the gateway.

---

## Model Routing

| Condition          | Result                                 |
| ------------------ | -------------------------------------- |
| `BLOCK`            | No model selected and no provider call |
| Safe short prompt  | Routed to a faster/lower-cost model    |
| Safe longer prompt | Routed to a stronger model             |
| Provider failure   | Controlled fallback response returned  |

---

## Governance Controls

| Risk Type              | Behavior                                                    |
| ---------------------- | ----------------------------------------------------------- |
| SSN in Finance         | Blocked by department policy                                |
| Credit card in Finance | Blocked by department policy                                |
| API key in Engineering | Blocked by department policy                                |
| Password in HR         | Blocked by department policy                                |
| Prompt injection       | Blocked globally                                            |
| Safe prompt            | Allowed or warned depending on risk score and policy result |

---

## Audit Logging

Each audit record stores:

* `id`
* `created_at`
* `redacted_prompt`
* `risk_score`
* `risk_level`
* `action`
* `risk_reasons`
* `prompt_redacted`
* `user_id`
* `department`
* `estimated_tokens`
* `estimated_cost`
* `blocked_cost_savings`

Audit data powers the department summary, audit summary, top governance metrics, cost visibility, and blocked savings dashboard.

---

## API Endpoints

| Endpoint              | Method | Purpose                                                           |
| --------------------- | ------ | ----------------------------------------------------------------- |
| `/analyze`            | `POST` | Analyze a prompt and return risk/action metadata                  |
| `/gateway`            | `POST` | Analyze prompt risk and route safe prompts through the AI gateway |
| `/audit-summary`      | `GET`  | Return audit-level governance metrics and recent logs             |
| `/department-summary` | `GET`  | Return department-level usage and risk analytics                  |
| `/health/db`          | `GET`  | Check database connectivity                                       |

---

## Evaluation Harness

The evaluation harness validates GuardRail AI across 28 prompt cases covering:

* Safe prompts
* Emails
* Phone numbers
* SSNs
* Credit cards
* Passwords
* API keys
* Prompt injection
* Mixed-risk prompts

Current evaluation result:

```text
Total Cases: 28
Passed: 28
Failed: 0
Accuracy: 100.0%
```

---

## Testing

The backend includes automated tests for core governance behavior, policy enforcement, scoring, redaction, and API behavior.

Current test status:

```text
54 passing tests
```

---

## Design Principles

GuardRail AI follows these design principles:

* Guardrails before model invocation
* Redaction before storage
* Department-aware policy enforcement
* API key protected backend endpoints
* Structured audit logging
* Token and cost visibility
* Blocked cost savings estimation
* Provider failure resilience
* Modular backend design
* Testable evaluation harness
* Frontend dashboard for enterprise governance visibility
* Extensible provider-agnostic gateway architecture

---

## Current Project Status

| Area                | Status       |
| ------------------- | ------------ |
| Backend API         | Complete     |
| Prompt analysis     | Complete     |
| Policy engine       | Complete     |
| Redaction           | Complete     |
| Audit logging       | Complete     |
| Token/cost tracking | Complete     |
| Gateway routing     | Complete     |
| Evaluation harness  | Complete     |
| Automated tests     | Complete     |
| React dashboard     | Complete     |
| Frontend polish     | Complete     |
| Deployment          | Planned next |
