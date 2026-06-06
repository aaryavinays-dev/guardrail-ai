## Version 1.8 - Risk Weight Dictionary Refactor

Features:
- Added centralized risk_weights dictionary
- Replaced hardcoded risk values with dictionary lookups
- Refactored risk scoring engine
- Improved maintainability and scalability

Concepts Learned:
- Dictionaries
- Key Value Pairs
- Dictionary Lookup
- += Operator
- Refactoring
- Maintainability

Validation:
Master Prompt Test

Email: 20
Password: 100
Prompt Injection: 100

Final Risk Score: 220
Action: BLOCK


## Version 2.0 robustness enhancement 
Concept Learned:
Error Handling
try
except
KeyError

Future Enhancement:
Add KeyError handling to risk scoring engine

## Version 2.0 - Audit Logging

Features:
- Added local audit logging using file handling
- Saved prompt, risk score, risk level, action, risk reasons, and timestamp
- Used append mode to preserve historical audit records

Concepts Learned:
- File Handling
- open()
- write()
- append mode
- audit trails
- timestamps
- persistence

Validation:
- Tested master prompt with email, password, and prompt injection
- Confirmed audit_log.txt stores the full request history