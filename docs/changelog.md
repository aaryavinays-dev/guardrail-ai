# Changelog

## GuardRail AI — Enterprise AI Governance Gateway

This changelog documents the evolution of GuardRail AI from a foundational FastAPI prompt-analysis backend into a deployed full-stack enterprise AI governance gateway with audit logging, policy enforcement, cost tracking, model routing, evaluation coverage, and a React TypeScript governance dashboard.

---

## Current Project Summary

**Current Version:** `v5.6`  
**Current Phase:** Portfolio-Final Full-Stack Deployment  
**Current Milestone:** Deployed Enterprise AI Governance Gateway with 100-Case Evaluation Coverage  
**Backend Test Suite:** `54 passed`  
**Evaluation Harness:** `100/100 cases passed`  
**Evaluation Accuracy:** `100.0%`  
**Backend Stack:** FastAPI, PostgreSQL, SQLAlchemy, Pydantic, Pytest, OpenAI SDK  
**Frontend Stack:** React, TypeScript, Vite, CSS  
**Deployment Stack:** Vercel frontend, Render backend, Neon PostgreSQL  

### Current Capabilities

- Sensitive data detection
- Prompt injection and jailbreak detection
- Risk scoring and risk-level classification
- ALLOW / WARN / BLOCK decision engine
- Secure prompt redaction
- PostgreSQL audit logging
- API key authentication
- User and department metadata tracking
- Department-level usage analytics
- Token and cost tracking
- Blocked cost savings tracking
- Department-specific policy engine
- AI gateway endpoint
- OpenAI provider integration
- Provider failure handling
- Model routing
- React TypeScript governance dashboard
- Prompt Analyzer UI
- Gateway Demo UI
- Department Summary UI
- Audit Summary UI
- Top governance metrics dashboard
- Vercel frontend deployment
- Render backend deployment
- Neon PostgreSQL production database
- 100-case evaluation harness
- 54 passing automated backend tests
- Polished recruiter-ready README and architecture documentation

---

## Version 5.6 — Final Portfolio Polish and Expanded Evaluation Coverage

### Added

- Expanded the evaluation harness from 28 prompt cases to 100 prompt cases.
- Added category-based evaluation coverage across safe prompts, PII/sensitive data, prompt injection, cost-heavy prompts, and WARN-level ambiguous prompts.
- Added 25 safe business prompt evaluation cases.
- Added 25 PII and sensitive-data prompt evaluation cases.
- Added 20 prompt injection and jailbreak evaluation cases.
- Added 15 cost-heavy / long prompt evaluation cases.
- Added 15 ambiguous WARN-level evaluation cases.
- Updated README with polished senior recruiter-ready positioning.
- Updated README with 100/100 evaluation results.
- Updated README with final deployment architecture and environment configuration.
- Updated architecture documentation to reflect deployed Vercel + Render + Neon production setup.
- Updated architecture documentation with 100-case evaluation architecture.
- Added stronger documented limitations section to show production-awareness and engineering judgment.

### Improved

- Improved prompt injection detection coverage for broader attack wording.
- Improved detection of policy bypass attempts.
- Improved detection of system prompt extraction attempts.
- Improved detection of hidden instruction and confidential prompt requests.
- Improved detection of audit bypass attempts.
- Improved detection of compliance bypass attempts.
- Improved password detection to catch more natural-language password exposure patterns.
- Improved project documentation for recruiter, hiring manager, and technical reviewer readability.
- Improved evaluation credibility by moving from a small demo eval set to a broader synthetic regression suite.

### Validation

- Verified all 100 evaluation cases pass.
- Verified expanded prompt injection cases are blocked correctly.
- Verified password exposure cases are blocked correctly.
- Verified safe business prompts remain allowed.
- Verified cost-heavy but safe prompts remain allowed.
- Verified ambiguous sensitive-data cases return expected WARN behavior.
- Verified 54 automated backend tests continue passing.
- Verified README and architecture documentation reflect final deployed system state.

### Outcome

GuardRail AI now has stronger portfolio proof through expanded evaluation coverage, improved detector robustness, polished documentation, and clearer enterprise AI governance positioning. The project is now suitable to present as a completed full-stack AI engineering portfolio project.

---

## Version 5.5 — Live Deployment

### Added

- Deployed React + TypeScript frontend to Vercel.
- Deployed FastAPI backend to Render.
- Connected production backend to Neon PostgreSQL.
- Added live frontend, backend API, and Swagger documentation links to README.
- Added environment-based frontend configuration using `VITE_API_BASE_URL` and `VITE_API_KEY`.
- Added production CORS configuration using `FRONTEND_URL`.
- Validated production audit summary and department summary dashboards.
- Validated production prompt analysis and gateway flows.

### Verified

- Audit Summary loads production logs from Neon.
- Department Summary displays Finance and Engineering governance metrics.
- Prompt Analyzer blocks SSN prompts and redacts sensitive data.
- Gateway blocks risky prompts before model invocation.
- Gateway allows safe prompts and routes them to the selected model path.
- Cost tracking and blocked savings display correctly in the live dashboard.
- Frontend successfully communicates with deployed Render backend.
- Render backend successfully connects to Neon PostgreSQL.
- Swagger documentation is available through the deployed backend.

### Notes

- Render free-tier deployments may have a cold start delay on the first request.
- External LLM provider calls depend on valid API key, quota, billing, and provider availability.
- Safe prompts may return a controlled provider fallback if the external model provider is unavailable.

### Outcome

GuardRail AI became a live deployed full-stack application with a Vercel frontend, Render backend, and Neon PostgreSQL database.

---

## Version 5.4 — Frontend Polish and Governance Metrics

### Added

- Added top-level governance metric cards to the React dashboard.
- Added total logs, blocked prompts, warnings, critical risks, estimated cost, and blocked savings cards.
- Added frontend cost formatting using dollar values.
- Added calculated estimated cost and blocked savings from audit logs when backend totals are unavailable.
- Added cleaner detection label formatting such as `SSN`, `API Key`, and `Prompt Injection`.
- Added empty prompt validation for Prompt Analyzer.
- Added empty prompt validation for Gateway Demo.

### Improved

- Improved dashboard readability and executive-level summary visibility.
- Improved cost and savings presentation for recruiter/demo clarity.
- Improved user experience with validation messages.
- Improved risk label readability in frontend result cards.

### Validation

- Verified top metric cards update after loading audit summary.
- Verified estimated cost and blocked savings display as formatted dollar values.
- Verified empty Prompt Analyzer input shows validation error.
- Verified empty Gateway Demo input shows validation error.
- Verified existing Prompt Analyzer, Gateway Demo, Department Summary, and Audit Summary flows continue working.

### Outcome

The React dashboard presents GuardRail AI as a complete enterprise governance interface with operational metrics, cost visibility, blocked savings, prompt analysis, gateway enforcement, department analytics, and audit traceability.

---

## Version 5.3 — Audit Summary Frontend

### Added

- Added Audit Summary section to the React dashboard.
- Connected frontend to `GET /audit-summary`.
- Added audit-level metric cards for total logs, blocked count, warnings, critical risks, estimated cost, and blocked savings.
- Added recent audit logs table.
- Displayed user ID, department, action, risk score, cost, blocked savings, and redacted prompt.

### Improved

- Improved enterprise traceability by exposing audit records in the frontend.
- Improved governance visibility across recent prompt decisions.
- Added frontend loading and error states for audit summary requests.

### Validation

- Verified Audit Summary loads data from FastAPI.
- Verified recent audit logs display correctly.
- Verified cost and blocked savings appear per audit record.
- Verified top-level dashboard metrics can reuse audit summary data.

### Outcome

GuardRail AI includes frontend audit visibility, allowing users to review recent prompt decisions, risk scores, redacted prompts, costs, and blocked savings from the dashboard.

---

## Version 5.2 — Department Summary Frontend

### Added

- Added Department Summary section to the React dashboard.
- Connected frontend to `GET /department-summary`.
- Displayed department-level total requests.
- Displayed department-level blocked counts.
- Displayed department-level critical counts.
- Displayed top risk reasons by department.

### Improved

- Improved business-facing governance visibility.
- Added frontend table rendering for department analytics.
- Added loading and error states for department summary requests.

### Validation

- Verified department summary loads successfully from FastAPI.
- Verified Finance, Engineering, Marketing, and other department rows display when audit data exists.
- Verified top risk reasons display in the dashboard.

### Outcome

GuardRail AI provides department-level AI governance analytics through the frontend, helping show which business units create the most AI risk.

---

## Version 5.1 — Gateway Demo Frontend

### Added

- Added Gateway Demo section to the React dashboard.
- Connected frontend to `POST /gateway`.
- Added gateway prompt input.
- Added Run Gateway button.
- Displayed gateway action, selected model, model-called status, risk score, risk level, estimated cost, blocked savings, redacted prompt, and gateway response.

### Improved

- Improved product storytelling by demonstrating the full AI gateway flow.
- Showed safe prompt behavior and blocked prompt behavior from the frontend.
- Added frontend loading and error states for gateway requests.

### Validation

- Verified safe prompts return `ALLOW`.
- Verified safe prompts display selected model information.
- Verified provider quota/configuration failure returns controlled fallback response.
- Verified SSN prompts return `BLOCK`.
- Verified blocked prompts return `model_called = false`.
- Verified blocked prompts show redacted content and policy reasons.

### Outcome

GuardRail AI demonstrates the core gateway concept through the frontend: safe prompts can be routed toward a model, while risky prompts are blocked before model invocation.

---

## Version 5.0 — React TypeScript Dashboard and Prompt Analyzer

### Added

- Created React + TypeScript frontend using Vite.
- Added GuardRail AI dashboard layout.
- Added Prompt Analyzer form.
- Added User ID input.
- Added Department input.
- Added Prompt textarea.
- Connected frontend to `POST /analyze`.
- Added real backend response rendering.
- Displayed action, risk score, risk level, estimated tokens, estimated cost, blocked savings, redacted prompt, detections, and risk reasons.

### Improved

- Converted backend API functionality into a product-facing dashboard.
- Added controlled inputs using React state.
- Added button click handling.
- Added frontend API calls using `fetch`.
- Added loading and error states.
- Added initial responsive dashboard styling.

### Validation

- Verified React frontend runs on `http://localhost:5173`.
- Verified FastAPI backend runs on `http://127.0.0.1:8000`.
- Verified frontend successfully calls `/analyze`.
- Verified SSN prompt returns `BLOCK`.
- Verified redacted prompt displays `[REDACTED_SSN]`.
- Verified detections and risk reasons display in the frontend.

### Outcome

GuardRail AI became a full-stack application with a React TypeScript dashboard connected to the FastAPI backend.

---

## Version 4.8 — Evaluation Harness

### Added

- Added evaluation harness under `evaluation/run_eval.py`.
- Added 28 evaluation cases across safe prompts, emails, phones, SSNs, credit cards, passwords, API keys, prompt injection, and mixed-risk prompts.
- Added category-level evaluation reporting.
- Added automated comparison between expected GuardRail action and actual system action.
- Added failed-case reporting for debugging detector, scoring, or policy gaps.

### Validation

- Verified evaluation harness runs successfully.
- Verified all 28 evaluation cases passed.
- Verified evaluation report shows `100.0%` accuracy.
- Confirmed test suite passes with `54 passed`.

### Outcome

GuardRail AI gained a structured evaluation harness that validates guardrail behavior across multiple prompt-risk categories and provides category-level accuracy reporting for demo and interview credibility.

---

## Version 4.7 — Model Routing

### Added

- Added model routing logic for the `/gateway` endpoint.
- Added fast model routing for safe short prompts.
- Added strong model routing for safe longer prompts.
- Added blocked prompt routing where no model is selected or called.
- Added `selected_model` field to gateway responses.
- Added `OPENAI_FAST_MODEL` and `OPENAI_STRONG_MODEL` environment configuration.

### Validation

- Verified blocked prompts return `selected_model = null` and `model_called = false`.
- Verified safe short prompts route to the fast model.
- Verified safe long prompts route to the strong model.
- Verified provider failure handling still returns a controlled response.
- Verified audit logs continue storing gateway request outcomes.
- Confirmed test suite passes with `54 passed`.

### Outcome

GuardRail AI routes safe prompts to different AI models based on prompt complexity while blocking unsafe prompts before model invocation, improving cost-performance control for enterprise AI usage.

---

## Version 4.6 — OpenAI Gateway

### Added

- Added `/gateway` endpoint to evaluate prompts before model invocation.
- Added gateway logic to block unsafe prompts before calling an external AI model.
- Added OpenAI provider integration for safe prompts.
- Added provider failure handling so quota, billing, or configuration issues return a controlled API response instead of crashing the backend.
- Added `model_called` and `ai_response` fields to gateway responses.

### Validation

- Verified blocked Finance prompt with SSN returns `action = BLOCK`.
- Verified blocked prompt returns `model_called = false`.
- Verified blocked prompt does not call the OpenAI model.
- Verified safe prompt passes GuardRail checks.
- Verified OpenAI provider quota issue is handled gracefully with `200 OK`.
- Verified gateway logs are stored in `/audit-summary`.
- Confirmed test suite passes with `54 passed`.

### Outcome

GuardRail AI now functions as an AI gateway: unsafe prompts are blocked before reaching an external model, while safe prompts can be routed to an AI provider with graceful fallback handling.

---

## Version 4.5 — Department-Specific Policy Engine

### Added

- Added department-specific policy engine for AI governance rules.
- Added Finance policy to block SSN and credit card usage.
- Added Engineering policy to block API key exposure.
- Added HR policy to block password exposure.
- Added global policy to block prompt injection attempts.
- Integrated policy engine into `/analyze` and `/gateway`.
- Added pytest coverage for department policy rules.

### Validation

- Verified Finance prompts with SSNs are blocked by policy.
- Verified Engineering prompts with API keys are blocked by policy.
- Verified safe prompts remain allowed.
- Verified `/audit-summary` stores policy-driven action and policy reasons.
- Confirmed test suite passes with `54 passed`.

### Outcome

GuardRail AI applies department-specific governance rules, allowing different business units to follow different AI safety policies before prompts reach an external AI model.

---

## Version 4.4 — Blocked Cost Savings

### Added

- Added blocked cost savings tracking for prompts blocked by GuardRail AI.
- Added `blocked_cost_savings` column to PostgreSQL audit logs.
- Updated `/analyze` response to return blocked cost savings.
- Updated `/audit-summary` to include blocked cost savings in recent audit logs.

### Validation

- Verified blocked prompts return `blocked_cost_savings` equal to `estimated_cost`.
- Verified allowed prompts return `blocked_cost_savings` as `0.0`.
- Verified `/audit-summary` returns stored blocked cost savings values.
- Confirmed test suite passes with `51 passed`.

### Outcome

GuardRail AI estimates the AI cost prevented by blocking unsafe prompts before they reach an external model, creating a simple ROI signal for AI governance.

---

## Version 4.3 — Token and Cost Tracking

### Added

- Added estimated token tracking for each `/analyze` request.
- Added estimated cost calculation using a cost-per-token baseline.
- Added `estimated_tokens` and `estimated_cost` columns to PostgreSQL audit logs.
- Updated `/analyze` response to return estimated token and cost values.
- Updated `/audit-summary` to include estimated token and cost values in recent audit logs.

### Validation

- Verified `/analyze` returns `estimated_tokens` and `estimated_cost`.
- Verified `/audit-summary` returns stored token and cost values from PostgreSQL.
- Confirmed test suite passes with `51 passed`.

### Outcome

GuardRail AI tracks estimated AI usage and cost per prompt, creating the foundation for department-level cost analytics, blocked cost savings, and model routing.

---

## Version 4.2 — Department Usage Summary

### Added

- Added `/department-summary` endpoint to return department-level usage analytics.
- Added total request count by department.
- Added blocked prompt count by department.
- Added critical risk count by department.
- Added top risk reasons by department.
- Added pytest coverage for department summary aggregation logic.

### Validation

- Verified `/department-summary` returns `200 OK` in Swagger.
- Verified response includes department names, total requests, blocked count, critical count, and top risk reasons.
- Confirmed test suite passes with `51 passed`.

### Outcome

GuardRail AI converts raw audit logs into department-level governance analytics, helping organizations identify which business units are creating the most AI risk.

---

## Version 4.1 — Department and User Metadata

### Added

- Added `user_id` and `department` fields to the `/analyze` request body.
- Added `user_id` and `department` fields to the `/analyze` response.
- Added `user_id` and `department` columns to the PostgreSQL `audit_logs` table.
- Updated audit logging to persist user and department metadata.
- Updated `/audit-summary` to include user and department metadata in recent audit logs.
- Added pytest coverage for `PromptRequest` user metadata.

### Validation

- Verified `/analyze` accepts user and department metadata.
- Verified PostgreSQL stores user and department metadata.
- Verified `/audit-summary` returns user and department metadata.
- Confirmed test suite passes with `50 passed`.

### Outcome

GuardRail AI connects each prompt analysis to a specific user and department, enabling department-level governance analytics such as blocked prompts, critical risks, and cost savings by business unit.

---

## Version 4.0 — API Key Authentication

### Added

- Added API key authentication using FastAPI security dependencies.
- Created `auth.py` to centralize API key validation logic.
- Added `x-api-key` header validation for protected endpoints.
- Protected `/analyze` so unauthorized clients cannot create audit records.
- Protected `/audit-summary` so unauthorized clients cannot view audit activity.
- Added `GUARDRAIL_API_KEY` environment variable support.
- Added API key template value to `.env.example`.
- Added automated authentication tests using FastAPI `TestClient`.

### Validation

- Verified missing API key returns `401 Unauthorized`.
- Verified valid API key allows `/analyze` to run successfully.
- Verified protected endpoint behavior through Swagger.
- Confirmed full test suite passes with `49 passed`.

### Outcome

GuardRail AI has a protected API layer. Sensitive governance endpoints require a valid `x-api-key` header before prompt analysis or audit summary access is allowed.

---

## Version 3.x — Backend Hardening and PostgreSQL Audit Layer

### Added

- Added PostgreSQL-backed audit logging.
- Added `/health/db` endpoint.
- Added SQLAlchemy database configuration and audit log model.
- Added detector hardening for natural-language passwords and prompt injection.
- Added regression tests for detection and redaction.
- Added enums for controlled `RiskLevel` and `Action` values.
- Added dedicated `redactor.py`.
- Added expanded unit test coverage.

### Improved

- Replaced local file-based audit summary reads with PostgreSQL-backed queries.
- Improved backend persistence and traceability.
- Improved password and prompt injection detection.
- Improved modularity and separation of concerns.
- Improved audit safety by storing redacted prompts.

### Validation

- Verified PostgreSQL audit log persistence.
- Verified database health check endpoint.
- Verified sensitive prompts are redacted before storage.
- Verified detector, redactor, analyzer, scorer, and policy behavior through automated tests.

### Outcome

GuardRail AI moved from local file-based logging into a more realistic enterprise backend architecture using PostgreSQL, SQLAlchemy, modular services, and stronger automated testing.

---

## Version 2.x — Modular FastAPI Backend Foundation

### Added

- Added Pydantic request and response models.
- Added `/audit-summary` endpoint.
- Added structured JSON audit logging.
- Added modular detector, scoring, and audit logger files.
- Added environment variable configuration.
- Added object-oriented refactor for analyzer, scorer, and audit logger.
- Added exception handling and backend logging.
- Added type hints and code quality cleanup.
- Added pytest foundation for scoring and risk-level tests.

### Improved

- Moved from a single-file FastAPI app to a modular backend structure.
- Improved request validation and response consistency.
- Improved audit reporting foundation.
- Improved maintainability through separation of responsibilities.
- Improved production readiness through configuration and defensive coding.

### Outcome

GuardRail AI became a structured FastAPI backend with validated request/response models, modular detection/scoring logic, audit logging, configuration management, and initial automated tests.

---

## Version 1.x — Initial Prompt Risk Engine

### Added

- Added initial prompt analysis logic.
- Added risk scoring experiments.
- Added risk weight dictionary.
- Added early detector logic.
- Added error handling research.
- Added first manual validation flows through Swagger.

### Outcome

GuardRail AI began as a prompt risk detection prototype and established the foundation for sensitive-data detection, scoring, action decisions, and later audit logging.

---

## Final Project State

GuardRail AI is now a deployed full-stack AI governance gateway with:

- FastAPI backend
- PostgreSQL audit storage
- React TypeScript dashboard
- Vercel frontend deployment
- Render backend deployment
- Neon PostgreSQL database
- Department-aware policy enforcement
- Prompt redaction
- Token/cost tracking
- Blocked savings estimation
- AI gateway routing
- Model routing
- Provider fallback handling
- 100-case evaluation harness
- 54 automated backend tests
- Enterprise governance dashboard
- Polished README and architecture documentation

The project is complete as a portfolio-grade enterprise AI governance system. Future work should focus on provider-agnostic expansion, Docker/AWS deployment options, audit export workflows, and enterprise identity integration rather than additional MVP scope.