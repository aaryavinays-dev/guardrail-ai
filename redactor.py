import re


def redact_prompt(prompt: str) -> str:
    redacted_prompt = prompt

    redacted_prompt = re.sub(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        "[REDACTED_EMAIL]",
        redacted_prompt,
    )

    redacted_prompt = re.sub(
        r"\b\d{3}-\d{2}-\d{4}\b",
        "[REDACTED_SSN]",
        redacted_prompt,
    )

    redacted_prompt = re.sub(
        r"\b(?:\d{4}[- ]?){3}\d{4}\b",
        "[REDACTED_CREDIT_CARD]",
        redacted_prompt,
    )

    redacted_prompt = re.sub(
        r"\b(?:\+1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b",
        "[REDACTED_PHONE]",
        redacted_prompt,
    )

    redacted_prompt = re.sub(
        r"\bsk-[A-Za-z0-9_-]{10,}\b",
        "[REDACTED_API_KEY]",
        redacted_prompt,
    )

    redacted_prompt = re.sub(
        r"\b((?:production|database|admin|root)\s+password)\s+(is|as)\s+\S+",
        r"\1 \2 [REDACTED_PASSWORD]",
        redacted_prompt,
        flags=re.IGNORECASE,
    )

    redacted_prompt = re.sub(
        r"\b((?:production|database|admin|root)\s+password)\s+(?!(?:is|as)\b)\S+",
        r"\1 [REDACTED_PASSWORD]",
        redacted_prompt,
        flags=re.IGNORECASE,
    )

    redacted_prompt = re.sub(
        r"\b(password|pwd|passcode)\s*[:=]\s*\S+",
        r"\1: [REDACTED_PASSWORD]",
        redacted_prompt,
        flags=re.IGNORECASE,
    )

    redacted_prompt = re.sub(
        r"\b(password|pwd|passcode)\s+(is|as)\s+\S+",
        r"\1 \2 [REDACTED_PASSWORD]",
        redacted_prompt,
        flags=re.IGNORECASE,
    )

    return redacted_prompt