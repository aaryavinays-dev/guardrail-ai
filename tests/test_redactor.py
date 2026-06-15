import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from redactor import redact_prompt


def test_redact_prompt_sensitive_values():
    prompt = (
        "My SSN is 123-45-6789, email is vinay@test.com, "
        "phone is 123-456-7890, password: hello123 "
        "and key sk-abc123456789"
    )

    redacted = redact_prompt(prompt)

    assert "123-45-6789" not in redacted
    assert "vinay@test.com" not in redacted
    assert "123-456-7890" not in redacted
    assert "hello123" not in redacted
    assert "sk-abc123456789" not in redacted

    assert "[REDACTED_SSN]" in redacted
    assert "[REDACTED_EMAIL]" in redacted
    assert "[REDACTED_PHONE]" in redacted
    assert "[REDACTED_PASSWORD]" in redacted
    assert "[REDACTED_API_KEY]" in redacted