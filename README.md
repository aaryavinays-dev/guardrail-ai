# GuardRail AI

GuardRail AI is an AI governance and prompt analysis platform designed to reduce token costs, detect sensitive information, and enforce enterprise AI usage policies before prompts reach external LLM providers.

---

# Problem

Organizations are rapidly adopting AI tools such as GPT, Claude, Copilot, LLama Family and Gemini.

Many prompts contain:

* Sensitive information (PII)
* Unnecessary prompt fluff
* Repeated wording
* Email signatures
* Excessive context

This increases:

* AI spending
* Security risk
* Compliance risk
* Data leakage risk

GuardRail AI aims to detect and prevent these issues before prompts are sent to AI models.

---

# Current MVP

The current MVP accepts a prompt, analyzes its content, detects sensitive information, calculates risk scores, performs basic prompt optimization, and estimates token savings.

---

# Current Features

## Prompt Analytics

* Word count calculation
* Character count calculation
* Character count without spaces
* Uppercase transformation
* Lowercase transformation
* Reverse prompt transformation
* No-space prompt transformation

## Prompt Optimization

Removes common prompt fluff phrases:

* Best regards
* Sincerely
* Thank you
* Please kindly

Calculates:

* Estimated tokens
* Optimized tokens
* Tokens saved

## Sensitive Data Detection

### Email Detection

Example:

[test@gmail.com](mailto:test@gmail.com)

### Phone Detection

Example:

734-555-1234

### SSN Detection

Example:

123-45-6789

### Credit Card Detection

Example:

4111-1111-1111-1111

## Risk Scoring Engine

### Risk Weights

| Detection   | Score |
| ----------- | ----- |
| Email       | 20    |
| Phone       | 20    |
| SSN         | 50    |
| Credit Card | 50    |

### Risk Levels

| Score | Risk Level |
| ----- | ---------- |
| 0-20  | LOW        |
| 21-50 | MEDIUM     |
| 51-99 | HIGH       |
| 100+  | CRITICAL   |

---

# Software Engineering Improvements

Version 1.2 introduced reusable helper functions and enhanced regex detection capabilities:

* detect_email()
* detect_ssn()
* detect_phone()
* detect_credit_card()

Benefits:

* Cleaner code
* Better readability
* Easier testing
* Easier maintenance
* Improved scalability

---

# Tech Stack

* Python
* FastAPI
* Uvicorn
* Regex
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
  "risk_reasons": [
    "Email detected",
    "SSN detected"
  ]
}
```

---

# How To Run Locally

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run application:

```bash
uvicorn main:app --reload
```

Open Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Latest Progress (Version 1.2)

Completed:

* Added Email Detection
* Added SSN Detection
* Added Phone Detection
* Added Credit Card Detection
* Added support for multiple credit card formats
  - 4111-1111-1111-1111
  - 4111 1111 1111 1111
  - 4111111111111111
* Added Weighted Risk Scoring
* Added LOW / MEDIUM / HIGH / CRITICAL Risk Levels
* Refactored detection logic into reusable helper functions
* Added Prompt Optimization
* Added Token Savings Estimation
* Added GitHub Version Control

---

# Lessons Learned

## Python Fundamentals

* Functions must be called to execute
* Parameters receive data
* Arguments provide data
* return sends data back to the caller
* Python evaluates the right side of assignments first
* Regex OR operator (|)
* Regex optional operator (?)
* Built a reusable regex for multiple credit card formats

## Software Engineering

* Functions should have one responsibility
* Refactoring improves maintainability
* Helper functions improve readability
* Reusable code is better than duplicated code

---

# Roadmap


## Future Features

* API Key Detection
* Password Detection
* Bank Account Detection
* Address Detection
* Advanced PII Detection
* Configurable Risk Rules
* Prompt Quality Scoring
* Prompt Improvement Suggestions
* Request Logging
* Audit Logging
* Prompt History
* PostgreSQL Integration
* User Authentication
* OpenAI Integration
* Multi-Model Routing (GPT, Claude, Gemini)
* Analytics Dashboard
* Enterprise Policy Engine
* RAG Knowledge Base Integration
* Document Upload and Analysis
* AI Agents for Risk Investigation
* Department-Level Budget Tracking
* Cloud Deployment
* Public Demo

---

# Project Goal

The long-term goal is to build an enterprise AI governance gateway that:

* Reduces AI token waste
* Detects sensitive information
* Enforces enterprise AI policies
* Tracks AI usage and costs
* Prevents data leakage
* Routes requests to appropriate AI models
* Provides governance, compliance, and observability for enterprise AI systems
