# GuardRail AI Screenshot Index

## Purpose

This document organizes the screenshots used as proof for GuardRail AI backend features, API behavior, PostgreSQL persistence, testing, and evaluation.

Screenshots are useful for:

* GitHub documentation
* Demo video recording
* Recruiter review
* Interview explanation
* Portfolio proof of work

---

## Screenshot Folder Structure

```text
screenshots/
│
├── api_security/
├── blocked_cost_savings/
├── department_metadata/
├── department_summary/
├── evaluation_harness/
├── model_routing/
├── openai_gateway/
├── policy_engine/
├── postgresql_audit_logging/
├── token_cost_tracking/
│
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
├── v2.1_project_refactor/
├── v2.2_pydantic_validation/
├── v2.3_json_logging/
├── v2.4_list_comprehension/
├── v2.5_environment_variables/
├── v2.6_oop_refactor/
├── v2.7_exception_handling/
├── v2.8_logging_and_type_hints/
├── v3.0_secure_response_redaction/
└── v3.1_python_polish/
```

---

## API Security

Folder:

```text
screenshots/api_security/
```

Purpose:

Shows that protected endpoints require a valid API key before users can analyze prompts or view audit data.

Recommended proof points:

| Screenshot                        | Purpose                              |
| --------------------------------- | ------------------------------------ |
| Missing API key returns 401       | Shows endpoint protection            |
| Invalid API key returns 401       | Shows unauthorized request rejection |
| Valid API key succeeds            | Shows authenticated request behavior |
| Pytest passing after API security | Shows regression coverage            |

---

## PostgreSQL Audit Logging

Folder:

```text
screenshots/postgresql_audit_logging/
```

Purpose:

Shows that GuardRail AI stores prompt analysis decisions in PostgreSQL instead of relying only on local files.

Recommended proof points:

| Screenshot                                  | Purpose                       |
| ------------------------------------------- | ----------------------------- |
| PostgreSQL `audit_logs` table               | Shows database persistence    |
| `/analyze` saves audit record               | Shows API-to-database flow    |
| `/audit-summary` reads from PostgreSQL      | Shows reporting from database |
| `/health/db` success response               | Shows database connectivity   |
| Pytest passing after PostgreSQL integration | Shows regression confidence   |

---

## Department Metadata

Folder:

```text
screenshots/department_metadata/
```

Purpose:

Shows that every prompt analysis can be connected to a specific user and department.

Recommended proof points:

| Screenshot                                         | Purpose                            |
| -------------------------------------------------- | ---------------------------------- |
| `/analyze` request with `user_id` and `department` | Shows metadata capture             |
| PostgreSQL audit row with user and department      | Shows metadata persistence         |
| `/audit-summary` with user and department          | Shows metadata returned in reports |
| Pytest passing after metadata                      | Shows validation coverage          |

---

## Department Summary

Folder:

```text
screenshots/department_summary/
```

Purpose:

Shows department-level governance analytics generated from audit logs.

Recommended proof points:

| Screenshot                              | Purpose                             |
| --------------------------------------- | ----------------------------------- |
| `/department-summary` Swagger response  | Shows department analytics endpoint |
| Finance blocked prompt summary          | Shows business-unit governance      |
| Top risk reasons by department          | Shows risk reporting                |
| Pytest passing after department summary | Shows aggregation test coverage     |

---

## Token and Cost Tracking

Folder:

```text
screenshots/token_cost_tracking/
```

Purpose:

Shows estimated token and cost visibility for each prompt request.

Recommended proof points:

| Screenshot                                  | Purpose              |
| ------------------------------------------- | -------------------- |
| `/analyze` response with `estimated_tokens` | Shows token tracking |
| `/analyze` response with `estimated_cost`   | Shows cost tracking  |
| PostgreSQL row with token and cost fields   | Shows persistence    |
| `/audit-summary` showing cost fields        | Shows reporting      |

---

## Blocked Cost Savings

Folder:

```text
screenshots/blocked_cost_savings/
```

Purpose:

Shows estimated AI cost prevented when unsafe prompts are blocked.

Recommended proof points:

| Screenshot                                       | Purpose                     |
| ------------------------------------------------ | --------------------------- |
| Blocked prompt with `blocked_cost_savings > 0`   | Shows avoided AI cost       |
| Allowed prompt with `blocked_cost_savings = 0.0` | Shows correct calculation   |
| `/audit-summary` with blocked savings            | Shows stored ROI signal     |
| Pytest passing after blocked cost savings        | Shows regression confidence |

---

## Policy Engine

Folder:

```text
screenshots/policy_engine/
```

Purpose:

Shows department-specific AI governance rules.

Recommended proof points:

| Screenshot                         | Purpose                    |
| ---------------------------------- | -------------------------- |
| Finance + SSN blocked              | Shows Finance policy       |
| Finance + credit card blocked      | Shows Finance policy       |
| Engineering + API key blocked      | Shows Engineering policy   |
| HR + password blocked              | Shows HR policy            |
| Prompt injection globally blocked  | Shows global governance    |
| Pytest passing after policy engine | Shows policy test coverage |

---

## OpenAI Gateway

Folder:

```text
screenshots/openai_gateway/
```

Purpose:

Shows that GuardRail AI can act as a gateway before external model invocation.

Recommended proof points:

| Screenshot                           | Purpose                                       |
| ------------------------------------ | --------------------------------------------- |
| Blocked prompt through `/gateway`    | Shows unsafe prompt blocked before model call |
| Safe prompt through `/gateway`       | Shows allowed gateway flow                    |
| Provider fallback response           | Shows quota/billing/config failure handling   |
| `/audit-summary` after gateway calls | Shows gateway audit logging                   |

---

## Model Routing

Folder:

```text
screenshots/model_routing/
```

Purpose:

Shows cost-performance routing behavior for safe prompts.

Recommended proof points:

| Screenshot                                  | Purpose                    |
| ------------------------------------------- | -------------------------- |
| Blocked prompt with `selected_model = null` | Shows no model selected    |
| Safe short prompt routes to fast model      | Shows fast model routing   |
| Safe long prompt routes to strong model     | Shows strong model routing |
| Pytest passing after model routing          | Shows no regression        |

---

## Evaluation Harness

Folder:

```text
screenshots/evaluation_harness/
```

Purpose:

Shows that GuardRail AI behavior is validated through repeatable evaluation cases.

Recommended proof points:

| Screenshot                            | Purpose                      |
| ------------------------------------- | ---------------------------- |
| Evaluation report with 28/28 passed   | Shows guardrail validation   |
| Category summary with 100% pass rates | Shows coverage by risk type  |
| Pytest result with 54 passed          | Shows backend test stability |

Important files:

```text
01_eval_report_28_cases_100_accuracy.png
02_pytest_54_passed_after_eval_v2.png
```

---

## Legacy / Build Progress Screenshots

Folders:

```text
screenshots/v1.0_mvp/
screenshots/v1.1_refactor/
screenshots/v1.2_credit_card/
screenshots/v1.3_api_key/
screenshots/v1.4_decision_engine/
screenshots/v1.5_password_detection/
screenshots/v1.6_prompt_injection/
screenshots/v1.7_prompt_injection_v2/
screenshots/v1.8_risk_weight_dictionary/
screenshots/v2.0_audit_logging/
screenshots/v2.1_project_refactor/
screenshots/v2.2_pydantic_validation/
screenshots/v2.3_json_logging/
screenshots/v2.4_list_comprehension/
screenshots/v2.5_environment_variables/
screenshots/v2.6_oop_refactor/
screenshots/v2.7_exception_handling/
screenshots/v2.8_logging_and_type_hints/
screenshots/v3.0_secure_response_redaction/
screenshots/v3.1_python_polish/
```

Purpose:

These folders show the project evolution from MVP detection logic to a more complete enterprise AI governance gateway.

They are useful for documenting learning progress and feature history, but the final README should mainly highlight the latest production-style backend features.

---

## Recommended Demo Screenshot Flow

Use this order when recording the project demo:

```text
1. Swagger UI homepage
2. API key authorization
3. /analyze Finance SSN blocked
4. /department-summary analytics
5. /gateway prompt injection blocked
6. /gateway safe short prompt routes to fast model
7. /gateway safe long prompt routes to strong model
8. /audit-summary audit logs
9. evaluation/run_eval.py 28/28 passing
10. python -m pytest 54 passed
```

---

## Recommended GitHub Proof Points

The final GitHub README should emphasize:

* PostgreSQL audit logging
* API key authentication
* Department metadata tracking
* Department-level analytics
* Token and cost tracking
* Blocked cost savings
* Policy-driven blocking
* AI gateway behavior
* Model routing
* Evaluation harness with 28 passing cases
* Pytest suite with 54 passing tests

---

## Final Validation State

```text
Backend Phase 1: Complete
Evaluation Harness: 28/28 passing
Pytest: 54 passed
Primary Database: PostgreSQL
API Framework: FastAPI
Gateway Behavior: Blocks unsafe prompts before model invocation
```
