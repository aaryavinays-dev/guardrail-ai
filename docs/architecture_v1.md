# GuardRail AI Architecture

## Overview

GuardRail AI is an enterprise AI governance gateway built with FastAPI, PostgreSQL, SQLAlchemy, and Python. It analyzes prompts before model invocation, detects sensitive data and prompt injection attempts, applies department-specific policies, tracks token/cost usage, estimates blocked cost savings, routes safe prompts to models, and stores structured audit logs.

---

## High-Level Flow

```text
Client / Swagger / Application
        |
        v
FastAPI API Layer
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
        +--------------------------+
        |                          |
        v                          v
BLOCK Response              Safe Prompt Flow
No Model Call               Model Routing
        |                          |
        v                          v
Audit Logging               OpenAI Provider Call
        |                          |
        +------------+-------------+
                     v
             PostgreSQL audit_logs

## CORE COMPONENETS


| Component               | File                     |Responsibility
| ------------------------------------------------------------------------------------------------------------------------------------ |
| API Layer               | `main.py`                | Defines `/analyze`, `/gateway`, `/audit-summary`, `/department-summary`, and `/health/db` |
| Request/Response Models | `models.py`              | Defines Pydantic schemas                                                                  |
| Prompt Analyzer         | `prompt_analyzer.py`     | Orchestrates all detection modules                                                        |
| Detectors               | `detectors.py`           | Detects emails, SSNs, phones, credit cards, passwords, API keys, and prompt injection     |
| Risk Scorer             | `risk_scorer.py`         | Calculates risk score, risk level, and initial action                                     |
| Scoring Config          | `scoring.py`             | Stores risk weights                                                                       |
| Policy Engine           | `policy_engine.py`       | Applies department-specific governance rules                                              |
| Redactor                | `redactor.py`            | Redacts sensitive values before response and storage                                      |
| Auth                    | `auth.py`                | Validates `x-api-key`                                                                     |
| Database Config         | `database.py`            | Manages SQLAlchemy engine/session                                                         |
| DB Model                | `db_models.py`           | Defines PostgreSQL audit log table                                                        |
| Audit Repository        | `audit_repository.py`    | Saves and queries audit records                                                           |
| Evaluation Harness      | `evaluation/run_eval.py` | Runs 28-case guardrail evaluation                                                         |

Request Lifecycle: /analyze
1. Client sends prompt, user ID, and department.
2. API key authentication runs.
3. Pydantic validates request body.
4. Prompt analyzer detects risk signals.
5. Risk scorer calculates score and risk level.
6. Department policy engine can override the initial action.
7. Redactor removes sensitive values.
8. Audit record is saved in PostgreSQL.
9. API returns risk, action, redacted prompt, cost, and policy metadata.

Request Lifecycle: /gateway
1. Client sends prompt, user ID, and department.
2. GuardRail AI analyzes prompt risk.
3. Department policy engine applies governance rules.
4. If action is BLOCK, the model is not called.
5. If action is ALLOW or WARN, a model is selected.
6. Safe prompts are routed to a selected model.
7. Provider quota or configuration failures return a controlled fallback response.
8. Audit record is stored in PostgreSQL.

Model Routing
| Condition          | Result                              |
| ------------------ | ----------------------------------- |
| `BLOCK`            | No model selected, no provider call |
| Safe short prompt  | Fast model                          |
| Safe longer prompt | Strong model                        |

Governance Controls

| Risk Type              | Behavior                     |
| ---------------------- | ---------------------------- |
| SSN in Finance         | Blocked by department policy |
| Credit card in Finance | Blocked by department policy |
| API key in Engineering | Blocked by department policy |
| Password in HR         | Blocked by department policy |
| Prompt injection       | Blocked globally             |

Audit Logging

Each audit record stores:
id
created_at
redacted_prompt
risk_score
risk_level
action
risk_reasons
prompt_redacted
user_id
department
estimated_tokens
estimated_cost
blocked_cost_savings

Evaluation Harness

The evaluation harness validates GuardRail AI across 28 prompt cases covering:

Safe prompts
Emails
Phone numbers
SSNs
Credit cards
Passwords
API keys
Prompt injection
Mixed-risk prompts

Current result:Total Cases: 28
Passed: 28
Failed: 0
Accuracy: 100.0%

Design Principles
Guardrails before model invocation
Redaction before storage
Department-aware governance
Cost visibility and blocked savings
Provider failure resilience
Testable modular backend design
Extensible provider-agnostic gateway architecture