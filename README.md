# GuardRail AI

GuardRail AI is an early-stage FastAPI backend project for AI governance, prompt optimization, and token cost reduction.

## Problem

Enterprises are rapidly adopting LLMs across departments, but many AI requests contain unnecessary prompt fluff, repeated text, email signatures, and non-essential wording. Since LLM providers charge based on token usage, this creates avoidable AI spending.

## Current MVP

This MVP accepts a user prompt, analyzes it, applies basic prompt-cleaning logic, and returns estimated token savings.

## Current Features

* FastAPI backend setup
* Root health-check endpoint
* `/analyze` POST endpoint
* Word count calculation
* Character count calculation
* Basic token estimation
* Email detection
* SSN detection
* Phone number detection
* Credit card detection
* Risk score calculation
- LOW / MEDIUM / HIGH risk classification
* Weighted risk scoring:
  - Email: 20
  - Phone: 20
  - SSN: 50
  - Credit Card: 50
* Prompt transformations:

  * Uppercase version
  * Lowercase version
  * Reversed prompt
  * No-space version
* Basic prompt optimization by removing simple fluff phrases
* Estimated token savings calculation

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Git
* GitHub

## API Endpoints

### GET `/`

Returns a basic health-check message.

Example response:

```json
{
  "message": "GuardRail AI is running"
}
```

---

### POST `/analyze`

Accepts a prompt and returns analysis details.

Example request:

```json
{
  "prompt": "Best regards to Mr Vinay S Aarya thank you Sincerely"
}
```

Example response:

```json
{
  "prompt": "Best regards to Mr Vinay S Aarya thank you Sincerely",
  "word_count": 10,
  "character_count": 52,
  "optimized_prompt": "to Mr Vinay S Aarya",
  "optimized_tokens": 6,
  "tokens_saved": 7,
  "estimated_tokens": 13
}
```
{
  "prompt": "My SSN is 123-45-6789 and my card is 4111-1111-1111-1111",
  "risk_level": "HIGH",
  "risk_score": 100,
  "risk_reasons": [
    "SSN detected",
    "Credit card detected"
  ]
}

## How to Run Locally

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the server:

```bash
uvicorn main:app --reload
```

Open Swagger docs:

```text
http://127.0.0.1:8000/docs
```


## Roadmap

* Improve prompt optimization logic
* Add CRITICAL risk level (100+ score)
* Support multiple credit card formats
  * 4111-1111-1111-1111
  * 4111111111111111
  * 4111 1111 1111 1111
* Add API Key detection
* Add Password detection
* Add Bank Account detection
* Add Address detection
* Refactor code into reusable functions
* Improve risk scoring engine
* Add configurable risk rules
* Add prompt category classification
* Add prompt quality scoring
* Add prompt improvement suggestions
* Add OpenAI API integration
* Add audit logging and prompt history
* Add PostgreSQL database integration
* Add user authentication and authorization
* Build React frontend dashboard
* Add analytics and reporting dashboard
* Add model routing (GPT, Claude, Gemini)
* Add enterprise policy engine
* Add document upload and analysis
* Add RAG knowledge base integration
* Add AI agents for automated risk investigation
* Deploy GuardRail AI to cloud
* Add advanced PII detection
* Add regex-based PII detection
* Add API key detection
* Add department-level budget tracking
* Add model routing logic
* Add request logging
* Add analytics dashboard
* Deploy public demo
* Add model routing logic
* Add department-level budget tracking
* Add request logging
* Add dashboard for token savings and blocked prompts

## Project Goal

The long-term goal is to build an enterprise AI governance gateway that helps organizations reduce AI token waste, enforce usage policies, and prevent sensitive data leakage before requests reach external LLM providers.
