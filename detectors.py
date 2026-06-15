import re


def detect_email(prompt: str) -> bool:
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    return bool(re.search(email_pattern, prompt))


def detect_ssn(prompt: str) -> bool:
    ssn_pattern = r"\b\d{3}-\d{2}-\d{4}\b"
    return bool(re.search(ssn_pattern, prompt))


def detect_phone(prompt: str) -> bool:
    phone_pattern = r"\b(?:\+1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    return bool(re.search(phone_pattern, prompt))


def detect_credit_card(prompt: str) -> bool:
    credit_card_pattern = r"\b(?:\d{4}[- ]?){3}\d{4}\b"
    return bool(re.search(credit_card_pattern, prompt))


def detect_api_key(prompt: str) -> bool:
    api_key_pattern = r"\bsk-[A-Za-z0-9_-]{10,}\b"
    return bool(re.search(api_key_pattern, prompt))


def detect_password(prompt: str) -> bool:
    password_pattern = r"\b(password|pwd|passcode)\s*[:=]\s*\S+"
    return bool(re.search(password_pattern, prompt, re.IGNORECASE))


def detect_prompt_injection(prompt: str) -> bool:
    suspicious_patterns = [
        r"ignore previous instructions",
        r"reveal system prompt",
        r"bypass policy",
        r"forget your rules",
        r"disable safety",
        r"override instructions",
        r"act as unrestricted",
    ]

    for pattern in suspicious_patterns:
        if re.search(pattern, prompt, re.IGNORECASE):
            return True

    return False