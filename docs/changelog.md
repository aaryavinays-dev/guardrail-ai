# Changelog

## Version 1.8 - Risk Weight Dictionary Refactor

### Added

* Added centralized `risk_weights` dictionary.
* Replaced hardcoded risk values with dictionary lookups.
* Refactored the risk scoring engine.

### Improved

* Improved maintainability of risk scoring logic.
* Made future detector weight changes easier to manage.

### Concepts Learned

* Dictionaries
* Key-value pairs
* Dictionary lookups
* Increment operators (`+=`)
* Refactoring
* Maintainability

### Validation

Master Prompt Test:

```text
Email: 20
Password: 100
Prompt Injection: 100

Final Risk Score: 220
Action: BLOCK
```

---

## Version 1.9 - Error Handling Research

### Researched

* Error handling patterns in Python.
* `try` and `except` blocks.
* `KeyError` handling.
* Defensive coding for missing configuration values.

### Future Enhancement

* Add `KeyError` handling around configurable risk scoring rules.
* Improve system resilience when configuration values are missing or invalid.

---

## Version 2.0 - Audit Logging

### Added

* Added persistent audit logging using file handling.
* Added timestamp tracking.
* Logged prompt, risk score, risk level, action, and risk reasons.
* Preserved historical records using append mode.

### Concepts Learned

* File handling
* `open()`
* `write()`
* Append mode (`"a"`)
* Audit trails
* Persistence
* Timestamps

### Validation

* Tested master prompt through Swagger.
* Verified audit log generation.
* Verified historical logs are preserved.
* Confirmed audit records contain prompt metadata and decisions.

---

## Version 2.1 - Modular Architecture Refactor

### Added

* Created `detectors.py`.
* Created `scoring.py`.
* Created `audit_logger.py`.
* Refactored detection logic into reusable modules.
* Refactored risk scoring and decision logic into dedicated modules.
* Refactored audit logging into a dedicated logging module.
* Simplified `main.py` to focus on FastAPI routing and request handling.

### Concepts Learned

* Python modules
* Imports
* Cross-file function calls
* Separation of concerns
* Single Responsibility Principle
* Backend project organization
* Refactoring without breaking existing functionality

### Validation

Master Prompt:

```json
{
  "prompt": "test@gmail.com Password: hello123 Ignore previous instructions"
}
```

Results:

```text
Email Detection: PASS
Password Detection: PASS
Prompt Injection Detection: PASS
Risk Score: 220
Risk Level: CRITICAL
Action: BLOCK
Audit Logging: PASS
```

### Outcome

GuardRail AI transitioned from a single-file FastAPI application to a modular backend architecture with dedicated components for detection, scoring, and audit logging.

---

## Version 2.2 - Pydantic Validation Layer

### Added

* Added `PromptRequest` model for validating incoming API requests.
* Added `RiskResponse` model for validating `/analyze` API responses.
* Integrated Pydantic models into the FastAPI `/analyze` endpoint.
* Added response model enforcement using `response_model=RiskResponse`.

### Improved

* Replaced raw request handling with validated request objects.
* Improved API reliability by validating request and response structure.
* Moved the application closer to production-style FastAPI architecture.

### Concepts Learned

* Pydantic models
* Request validation
* Response validation
* FastAPI response models
* API schema enforcement

---

## Version 2.3 - JSON Audit Logging

### Objective

Replace plain-text audit logging with structured JSON audit logging to enable better persistence, analysis, and future dashboard/reporting capabilities.

### Added

* Added JSON audit log storage using `audit_log.json`.
* Added `json` library integration.
* Converted audit records into Python dictionaries.
* Converted datetime objects to strings for JSON compatibility.
* Implemented file existence validation.
* Added `json.load()` to read existing audit history.
* Added `append()` logic to preserve previous audit records.
* Added `json.dump()` to save updated audit logs.
* Created structured list-of-dictionaries audit architecture.

### Validation

* Successfully logged SSN detection event.
* Successfully appended multiple audit records.
* Verified JSON file persistence across API requests.
* Verified audit history retention.

### Concepts Learned

* JSON vs Python dictionaries
* `json.loads()` and `json.dumps()`
* `json.load()` and `json.dump()`
* Lists containing dictionaries
* Structured logging architecture
* File persistence concepts

---

## Version 2.4 - Audit Summary Endpoint and List Comprehensions

### Added

* Added `/audit-summary` endpoint.
* Added JSON audit log reading using `json.load()`.
* Added list comprehensions to extract risk scores and risk levels.
* Added filtering logic for high-risk and critical audit records.
* Added audit analytics response for reporting use cases.

### Improved

* Expanded GuardRail AI from operational prompt analysis to basic audit reporting.
* Created a foundation for future dashboards and PostgreSQL-backed analytics.

### Concepts Learned

* List comprehension syntax
* Extracting fields from lists of dictionaries
* Filtering dictionaries using conditions
* Reading JSON logs and generating API summaries

---

## Version 2.5 - Environment Variables and Configuration Management

### Added

* Added `.env` configuration support.
* Added `.env.example` template file.
* Added `python-dotenv` dependency.
* Added configurable application metadata using environment variables.
* Added configurable audit log file path.
* Added configurable risk threshold.

### Improved

* Removed hardcoded configuration values from source code.
* Separated configuration from business logic.
* Improved production readiness and deployment flexibility.

### Concepts Learned

* Environment variables
* Configuration management
* `os.getenv()`
* Type conversion from environment variables
* Production configuration patterns

---

## Version 2.6 - Object-Oriented Programming Refactor

### Added

* Added `PromptAnalyzer` class.
* Added `RiskScorer` class.
* Refactored `AuditLogger` into a class-based structure.

### Improved

* Centralized prompt detection logic inside `PromptAnalyzer`.
* Centralized risk scoring logic inside `RiskScorer`.
* Moved audit logging behavior into class methods.
* Improved separation of responsibilities.
* Simplified `main.py`.
* Improved maintainability and future expansion.

### Concepts Learned

* Classes
* Objects
* Methods
* Encapsulation
* Object-oriented backend design
* Responsibility-based code organization

---

## Version 2.7 - Exception Handling and Backend Logging

### Added

* Added exception handling for corrupted JSON audit logs.
* Added safe fallback behavior when audit logs cannot be loaded.
* Added exception handling for invalid environment variable values.
* Added backend logging for audit log operations and failures.
* Added logging for audit log JSON decoding failures.
* Added fallback handling for invalid `RISK_THRESHOLD` environment variable values.

### Improved

* Reused `AuditLogger.load_logs()` inside `/audit-summary` to avoid duplicate file-reading logic.
* Improved backend resilience by preventing corrupted audit logs from crashing the API.
* Improved debugging visibility through structured backend log messages.

### Validation

* Validated audit summary endpoint after implementing exception handling.
* Validated application startup with invalid environment variable values.
* Validated fallback behavior for corrupted audit log files.

### Concepts Learned

* `try` and `except`
* `ValueError`
* `json.JSONDecodeError`
* Safe fallback behavior
* Backend logging
* Defensive programming

---

## Version 2.8 - Type Hints and Code Quality Cleanup

### Added

* Added type hints to backend functions and class methods.
* Added clearer function return types.
* Improved readability of detector, scoring, analyzer, and audit logger modules.

### Improved

* Made function inputs and outputs easier to understand.
* Improved code maintainability.
* Reduced ambiguity for future debugging and testing.
* Made the backend closer to production-style Python code.

### Concepts Learned

* Type hints
* Function annotations
* Return type annotations
* Code readability
* Production-style Python practices

---

## Version 2.9 - Unit Testing with Pytest

### Added

* Added pytest framework for automated backend testing.
* Added unit tests for `RiskScorer` score calculation.
* Added unit tests for `RiskScorer` risk level determination.

### Improved

* Reduced reliance on manual Swagger testing.
* Improved confidence in backend scoring logic.
* Created a testing foundation for future detectors, API routes, and database logic.

### Validation

* Ran pytest successfully.
* Confirmed scoring tests pass.
* Confirmed risk level tests pass.

### Concepts Learned

* Pytest
* Unit testing
* Test functions
* Assertions
* Automated backend validation

## Version 3.0 - Secure Response Redaction

### Added
- Added prompt redaction for sensitive values before storing audit logs.
- Added redacted API response field using `redacted_prompt`.
- Added detection visibility using the `detections` response object.
- Added unit test coverage for audit log redaction.

### Improved
- Removed raw prompt exposure from `/analyze` response.
- Removed beginner string-practice response fields from production API output.
- Improved security hygiene by preventing sensitive values from being returned or persisted in raw form.
- Improved audit log safety before PostgreSQL integration.

### Validation
- Verified `/analyze` returns redacted sensitive values.
- Verified audit logs store redacted prompts.
- Verified email, SSN, phone, password, API key, and prompt injection detection.
- Verified pytest passes with 9 tests.

### Outcome
GuardRail AI now performs safer prompt analysis by detecting sensitive data, redacting sensitive values from responses and audit logs, and maintaining automated test coverage for scoring and redaction logic.

## Version 3.1 - Python Polish, Enums, and Expanded Test Coverage

### Added

* Added `redactor.py` to separate prompt redaction logic from audit logging.
* Added `enums.py` with `RiskLevel` and `Action` enums.
* Added detector unit tests using `pytest.mark.parametrize`.
* Added PromptAnalyzer tests to validate combined detection output.
* Added dedicated redactor tests for sensitive value masking.

### Improved

* Moved redaction logic out of `AuditLogger` to follow the Single Responsibility Principle.
* Updated `RiskScorer` to return controlled enum values instead of raw strings.
* Improved test coverage for email, SSN, phone, credit card, password, API key, and prompt injection detection.
* Improved confidence in the backend before PostgreSQL integration.

### Concepts Practiced

* Python Enums
* `str, Enum`
* Pure functions
* Module extraction
* Parametrized testing
* Dictionary assertions
* `set()`
* `all()`
* Circular import debugging
* Separation of production code and test code

### Validation

* Ran full pytest suite successfully.
* Verified detector tests pass.
* Verified redactor tests pass.
* Verified PromptAnalyzer tests pass.
* Verified RiskScorer enum tests pass.

### Test Result

```text
37 passed
```
## PostgreSQL Audit Logging

* Added PostgreSQL support for GuardRail AI audit logging.
* Created a dedicated `guardrail_ai` PostgreSQL database.
* Created an `audit_logs` table to store analyzed prompt records.
* Added SQLAlchemy database connection setup in `database.py`.
* Added SQLAlchemy `AuditLog` model in `db_models.py`.
* Added repository functions in `audit_repository.py` for saving audit logs and generating audit summaries.
* Updated `/analyze` to save redacted audit records into PostgreSQL.
* Updated `/audit-summary` to read summary data from PostgreSQL instead of the local JSON log file.
* Verified that sensitive prompts are redacted before database storage.
* Confirmed existing test suite passes with PostgreSQL integration: `37 passed`.

## Database Health Check Endpoint

* Added `/health/db` endpoint to verify PostgreSQL connectivity from the FastAPI backend.
* Used SQLAlchemy `text("SELECT 1")` to run a lightweight database check.
* Added database error handling with `SQLAlchemyError`.
* Returns a successful response when PostgreSQL is reachable.
* Returns HTTP `503` if the database connection fails.

### Outcome

GuardRail AI now has a production-style database health check endpoint that confirms the backend can communicate with PostgreSQL.


