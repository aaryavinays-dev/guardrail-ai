## Version 1.8 - Risk Weight Dictionary Refactor

### Features

* Added centralized `risk_weights` dictionary
* Replaced hardcoded risk values with dictionary lookups
* Refactored risk scoring engine
* Improved maintainability and scalability

### Concepts Learned

* Dictionaries
* Key-Value Pairs
* Dictionary Lookups
* Increment Operators (`+=`)
* Refactoring
* Maintainability

### Validation

Master Prompt Test:

* Email: 20
* Password: 100
* Prompt Injection: 100

Final Risk Score: 220

Action: BLOCK

---

## Version 2.0 - Error Handling Research

### Concepts Learned

* Error Handling
* `try`
* `except`
* `KeyError`

### Future Enhancement

Potential future enhancement:

* Add `KeyError` handling around configurable risk scoring rules
* Improve system resilience when configuration values are missing

---

## Version 2.0 - Audit Logging

### Features

* Added persistent audit logging using file handling
* Added timestamp tracking
* Logged prompt, risk score, risk level, action, and risk reasons
* Preserved historical records using append mode

### Concepts Learned

* File Handling
* `open()`
* `write()`
* Append Mode (`"a"`)
* Audit Trails
* Persistence
* Timestamps

### Validation

* Tested master prompt through Swagger
* Verified audit log generation
* Verified historical logs are preserved
* Confirmed audit records contain prompt metadata and decisions

---

## Version 2.1 - Modular Architecture Refactor

### Features

* Created `detectors.py`
* Created `scoring.py`
* Created `audit_logger.py`
* Refactored detection logic into reusable modules
* Refactored risk scoring and decision logic into dedicated modules
* Refactored audit logging into a dedicated logging module
* Simplified `main.py` to focus on FastAPI routing and request handling

### Concepts Learned

* Python Modules
* Imports
* Cross-File Function Calls
* Separation of Concerns
* Single Responsibility Principle
* Backend Project Organization
* Refactoring Without Breaking Existing Functionality

### Validation

Master Prompt:

```json
{
  "prompt": "test@gmail.com Password: hello123 Ignore previous instructions"
}
```

Results:

* Email Detection: PASS
* Password Detection: PASS
* Prompt Injection Detection: PASS
* Risk Score: 220
* Risk Level: CRITICAL
* Action: BLOCK
* Audit Logging: PASS

### Outcome

GuardRail AI transitioned from a single-file FastAPI application to a modular backend architecture with dedicated components for detection, scoring, and audit logging.

## Version 0.4.0 - Pydantic Validation Layer

### Added
- Added `PromptRequest` model for validating incoming API requests.
- Added `RiskResponse` model for validating `/analyze` API responses.
- Integrated Pydantic models into FastAPI `/analyze` endpoint.
- Added response model enforcement using `response_model=RiskResponse`.

### Improved
- Replaced raw request handling with validated request objects.
- Improved API reliability by validating request and response structure.
- Made the application closer to production-style FastAPI architecture.

## Version 2.3 - JSON Audit Logging

### Objective
Replace plain-text audit logging with structured JSON audit logging to enable better persistence, analysis, and future dashboard/reporting capabilities.

### Implemented
- Added JSON audit log storage using `audit_log.json`
- Added `json` library integration
- Converted audit records into Python dictionaries
- Converted datetime objects to strings for JSON compatibility
- Implemented file existence validation
- Added `json.load()` to read existing audit history
- Added `append()` logic to preserve previous audit records
- Added `json.dump()` to save updated audit logs
- Created structured list-of-dictionaries audit architecture

### Validation
- Successfully logged SSN detection event
- Successfully appended multiple audit records
- Verified JSON file persistence across API requests
- Verified audit history retention

```md
## Version 2.4 - Audit Summary Endpoint & List Comprehensions

### Added
- Added `/audit-summary` endpoint.
- Added JSON audit log reading using `json.load()`.
- Added list comprehensions to extract risk scores and risk levels.
- Added filtering logic for high-risk and critical audit records.
- Added audit analytics response for reporting use cases.

## Version 2.5 - Environment Variables & Configuration Management

### Added
- Added `.env` configuration support.
- Added `.env.example` template file.
- Added `python-dotenv` dependency.
- Added configurable application metadata using environment variables.
- Added configurable audit log file path.
- Added configurable risk threshold.

### Improved
- Removed hardcoded configuration values from source code.
- Separated configuration from business logic.
- Improved production readiness and deployment flexibility.

### Learning Outcomes
- Environment Variables
- Configuration Management
- `os.getenv()`
- Type Conversion from Environment Variables
- Production Configuration Patterns

### Improved
- Expanded GuardRail AI from operational prompt analysis to basic audit reporting.
- Created foundation for future dashboard and PostgreSQL-backed analytics.

### Learning Outcomes
- List comprehension syntax
- Extracting fields from list of dictionaries
- Filtering dictionaries using conditions
- Reading JSON logs and generating API summaries

### Learning Outcomes
- JSON vs Python Dictionary
- `json.loads()` and `json.dumps()`
- `json.load()` and `json.dump()`
- Lists containing dictionaries
- Structured logging architecture
- File persistence concepts

v2.6 – OOP Refactor

Implemented object-oriented architecture.

Added PromptAnalyzer class
- Centralized prompt detection logic

Added RiskScorer class
- Centralized risk scoring logic

Refactored AuditLogger
- Converted logging functionality into class methods

Benefits:
- Better separation of responsibilities
- Cleaner main.py
- Improved maintainability
- Easier future expansion


## Version 2.7 - Exception Handling and Logging

### Added
- Added exception handling for corrupted JSON audit logs.
- Added safe fallback behavior when audit logs cannot be loaded.
- Added exception handling for corrupted audit log files.
- Added exception handling for invalid environment variable values.
- Added backend logging for audit log operations and failures.
- Added logging for audit log JSON decoding failures.
- Added fallback handling for invalid `RISK_THRESHOLD` environment variable values.
- Validated audit summary endpoint after implementing exception handling and logging improvements.

### Improved
- Reused `AuditLogger.load_logs()` inside `/audit-summary` to avoid duplicate file-reading logic.
- Improved backend resilience by preventing corrupted audit logs from crashing the API.

## Version 2.9 - Unit Testing with Pytest

### Added
- Added pytest framework for automated backend testing.
- Added unit tests for RiskScorer score calculation.
- Added unit tests for RiskScorer risk level determination.

### Improved
- Reduced reliance on manual testing through automated test execution.
- Improved confidence in backend scoring logic.

### Outcome
GuardRail AI now maintains structured persistent audit logs in JSON format, enabling future analytics, reporting, and dashboard capabilities.