import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from audit_logger import AuditLogger


def test_redact_prompt_sensitive_values():
    logger = AuditLogger("logs/test_audit_log.json")

    prompt = (
        "My SSN is 123-45-6789, email is vinay@test.com, "
        "phone is 123-456-7890, password: hello123 "
        "and key sk-abc123456789"
    )

    redacted_prompt = logger.redact_prompt(prompt)

    assert "123-45-6789" not in redacted_prompt
    assert "vinay@test.com" not in redacted_prompt
    assert "123-456-7890" not in redacted_prompt
    assert "hello123" not in redacted_prompt
    assert "sk-abc123456789" not in redacted_prompt

    assert "[REDACTED_SSN]" in redacted_prompt
    assert "[REDACTED_EMAIL]" in redacted_prompt
    assert "[REDACTED_PHONE]" in redacted_prompt
    assert "[REDACTED_PASSWORD]" in redacted_prompt
    assert "[REDACTED_API_KEY]" in redacted_prompt