# GuardRail AI Frontend

## Overview

This folder contains the React + TypeScript frontend for GuardRail AI.

The frontend is built with Vite and serves as an internal enterprise AI governance dashboard. It connects to the FastAPI backend and allows users to analyze prompts, test the AI gateway flow, view department-level governance analytics, and review audit-level traceability.

The goal of this frontend is not to be a consumer SaaS landing page. It is designed as a practical internal dashboard that demonstrates how enterprise teams could monitor and govern AI prompt usage before model invocation.

---

## Frontend Features

### Prompt Analyzer

Connected to:

```text
POST /analyze
```

The Prompt Analyzer allows a user to submit:

* User ID
* Department
* Prompt text

It displays:

* Final action: `ALLOW`, `WARN`, or `BLOCK`
* Risk score
* Risk level
* Estimated tokens
* Estimated cost
* Blocked cost savings
* Redacted prompt
* Detected risk flags
* Risk reasons

---

### Gateway Demo

Connected to:

```text
POST /gateway
```

The Gateway Demo shows the core GuardRail AI product flow:

* Safe prompts can continue toward model invocation.
* Risky prompts are blocked before reaching the model.

It displays:

* Final action
* Selected model
* Whether the model was called
* Risk score
* Risk level
* Estimated cost
* Blocked cost savings
* Redacted prompt
* Gateway or provider response
* Risk reasons

---

### Department Summary

Connected to:

```text
GET /department-summary
```

The Department Summary section displays department-level governance analytics:

* Department name
* Total requests
* Blocked prompts
* Critical risk count
* Top risk reasons

This helps show which departments are creating the most AI risk.

---

### Audit Summary

Connected to:

```text
GET /audit-summary
```

The Audit Summary section displays audit-level traceability:

* Total logs
* Blocked count
* Warning count
* Critical count
* Estimated cost
* Blocked cost savings
* Recent audit logs
* User ID
* Department
* Action
* Risk score
* Redacted prompt

---

### Top Governance Metrics

The dashboard includes top-level metrics for:

* Total logs
* Blocked prompts
* Warnings
* Critical risks
* Estimated cost
* Blocked cost savings

These metrics help communicate the business value of GuardRail AI as a governance and cost-visibility layer.

---

## Tech Stack

* React
* TypeScript
* Vite
* CSS
* Fetch API
* FastAPI backend integration

---

## Local Setup

From the project root:

```bash
cd frontend
npm install
npm run dev
```

The frontend runs at:

```text
http://localhost:5173
```

The FastAPI backend should also be running at:

```text
http://127.0.0.1:8000
```

---

## Backend Requirements

The frontend expects the backend to expose these endpoints:

| Endpoint              | Method | Purpose                                      |
| --------------------- | ------ | -------------------------------------------- |
| `/analyze`            | `POST` | Analyze prompt risk                          |
| `/gateway`            | `POST` | Route safe prompts and block risky prompts   |
| `/department-summary` | `GET`  | Return department-level governance analytics |
| `/audit-summary`      | `GET`  | Return audit metrics and recent logs         |

All requests use the API key header:

```text
x-api-key: guardrail-local-dev-key
```

---

## Frontend Development Notes

The frontend uses React state to manage:

* Prompt Analyzer form inputs
* Gateway Demo input
* Backend response data
* Loading states
* Error states
* Department summary data
* Audit summary data

The dashboard uses controlled inputs, button click handlers, `fetch` API calls, conditional rendering, and table rendering to display backend data.

---

## Project Purpose

This frontend exists to make the GuardRail AI backend understandable and demo-ready.

It shows how an enterprise team could:

* Analyze prompts before model invocation
* Block risky prompts
* Redact sensitive data
* Track AI usage by department
* Review audit logs
* Estimate AI usage cost
* Estimate blocked cost savings
* Demonstrate governance controls through a usable dashboard

---

## Status

| Feature                    | Status       |
| -------------------------- | ------------ |
| Prompt Analyzer            | Complete     |
| Gateway Demo               | Complete     |
| Department Summary         | Complete     |
| Audit Summary              | Complete     |
| Top Governance Metrics     | Complete     |
| Loading/Error States       | Complete     |
| Cost Formatting            | Complete     |
| Detection Label Formatting | Complete     |
| Deployment                 | Planned next |
