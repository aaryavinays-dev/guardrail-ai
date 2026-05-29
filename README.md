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
- Email detection
- SSN detection
- Phone number detection
- Risk classification (HIGH / LOW)
- Risk reason reporting
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
* Add regex-based PII detection
## Roadmap

* Improve prompt optimization logic
* Add advanced PII detection
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
* Deploy public demo

## Project Goal

The long-term goal is to build an enterprise AI governance gateway that helps organizations reduce AI token waste, enforce usage policies, and prevent sensitive data leakage before requests reach external LLM providers.
