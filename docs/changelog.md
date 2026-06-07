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
