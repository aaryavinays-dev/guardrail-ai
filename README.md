# GuardRail AI

## Enterprise AI Governance & Prompt Security Gateway

GuardRail AI is an enterprise-focused AI governance platform designed to inspect, secure, optimize, and control prompts before they reach external AI providers such as OpenAI GPT, Claude, Gemini, Copilot, and open-source LLMs.

The goal is to help organizations reduce AI costs, prevent sensitive data exposure, enforce governance policies, and improve AI usage visibility through centralized prompt inspection and risk analysis.

---

# Problem Statement

Organizations are rapidly adopting Generative AI across departments.

However, prompts frequently contain:

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
* Poor AI governance

Most organizations currently send prompts directly to AI providers without any inspection layer.

GuardRail AI aims to solve this problem by acting as a protective gateway between users and AI systems.

---

# Current MVP

The current MVP accepts prompts through a FastAPI endpoint, analyzes content, detects sensitive information, calculates risk scores, determines actions, and maintains audit logs for future review.

---

# Current Architecture

User Prompt

↓

FastAPI API

↓

Detection Engine

* Email Detection
* Phone Detection
* SSN Detection
* Credit Card Detection
* Password Detection
* API Key Detection
* Prompt Injection Detection

↓

Risk Scoring Engine

↓

Risk Classification Engine

* LOW
* MEDIUM
* HIGH
* CRITICAL

↓

Decision Engine

* ALLOW
* WARN
* BLOCK

↓

Audit Logging System

* audit_log.txt

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

GuardRail AI removes common prompt fluff including:

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

[test@gmail.com](mailto:test@gmail.com)

---

### Phone Number Detection

Example:

734-555-1234

---

### SSN Detection

Example:

123-45-6789

---

### Credit Card Detection

Supported Formats:

* 4111-1111-1111-1111
* 4111 1111 1111 1111
* 4111111111111111

---

### Password Detection

Detects password-related information inside prompts.

Example:

Password: hello123

---

### API Key Detection

Detects exposed API keys.

Example:

sk-xxxxxxxxxxxxxxxx

---

### Prompt Injection Detection

Detects common prompt injection attempts including:

* Ignore previous instructions
* Reveal system prompt
* Bypass policy
* Forget your rules

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

Based on the calculated risk score:

| Risk Score | Action |
| ---------- | ------ |
| 0-20       | ALLOW  |
| 21-99      | WARN   |
| 100+       | BLOCK  |

This decision engine simulates enterprise policy enforcement before requests reach external AI systems.

---

# Audit Logging System

Version 2.0 introduces persistent audit logging.

Every analyzed prompt stores:

* Timestamp
* Original Prompt
* Risk Score
* Risk Level
* Action Taken
* Risk Reasons

Example Log Entry:

Timestamp:
2026-06-07 10:30:00

Prompt:
[test@gmail.com](mailto:test@gmail.com) Password: hello123

Risk Score:
120

Risk Level:
CRITICAL

Action:
BLOCK

Risk Reasons:
Password detected

---

This provides:

* Auditability
* Traceability
* Governance visibility
* Security monitoring

---

# Tech Stack

## Backend

* Python
* FastAPI
* Uvicorn

## Security

* Regex Pattern Detection
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

# How To Run Locally

Install Dependencies

```bash
pip install fastapi uvicorn
```

Run Application

```bash
uvicorn main:app --reload
```

Open Swagger UI

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

---

# Concepts Implemented

## Python

* Functions
* Dictionaries
* Sets
* Lists
* Loops
* Conditional Logic
* Error Handling
* File Handling
* Regex

## Backend Engineering

* REST APIs
* FastAPI
* API Endpoints
* Request Processing
* Risk Scoring Systems
* Audit Logging

## Security Engineering

* PII Detection
* Sensitive Data Identification
* Prompt Injection Detection
* Policy Enforcement
* AI Governance Concepts

---

# Future Roadmap

## Phase 2

* PostgreSQL Integration
* SQLAlchemy ORM
* Structured Audit Database
* Configurable Risk Policies

## Phase 3

* User Authentication
* Role Based Access Control
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
