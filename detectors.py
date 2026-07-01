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
    password_patterns = [
        r"\bpassword\b\s*(is|=|:)?\s*[A-Za-z0-9!@#$%^&*()_+\-]{6,}",
        r"\bpasscode\b\s*(is|=|:)?\s*[A-Za-z0-9!@#$%^&*()_+\-]{6,}",
        r"\bpwd\b\s*(is|=|:)?\s*[A-Za-z0-9!@#$%^&*()_+\-]{6,}",
        r"\b(production|database|admin|root|portal|temporary|temp)\s+password\s*(is|=|:)?\s*[A-Za-z0-9!@#$%^&*()_+\-]{6,}",
    ]

    for pattern in password_patterns:
        if re.search(pattern, prompt, re.IGNORECASE):
            return True

    return False


def detect_prompt_injection(prompt: str) -> bool:
    suspicious_patterns = [
        r"ignore\s+(all\s+)?(previous|prior|earlier)\s+instructions",
        r"reveal\s+(the\s+)?system\s+prompt",
        r"show\s+(me\s+)?(the\s+)?system\s+prompt",
        r"bypass\s+(all\s+)?(company\s+)?(policies|policy|rules|safety|safety\s+rules|safety\s+filters|guardrails)",
        r"disable\s+(all\s+)?(your\s+)?safety\s+(filters|rules|policies)",
        r"override\s+(the\s+)?policy\s+engine",
        r"override\s+(the\s+)?instructions",
        r"forget\s+(all\s+)?(your\s+)?rules",
        r"show\s+(me\s+)?(your\s+)?hidden\s+instructions",
        r"confidential\s+system\s+rules",
        r"pretend\s+you\s+are\s+not\s+(restricted|bound)",
        r"not\s+restricted\s+by\s+safety\s+policies",
        r"jailbreak",
        r"developer\s+mode",
        r"\bDAN\b",
        r"previous\s+instructions\s+are\s+invalid",
        r"follow\s+only\s+my\s+new\s+instructions",
        r"reveal\s+(the\s+)?confidential\s+prompt",
        r"ignore\s+compliance\s+rules",
        r"remove\s+all\s+safety\s+policies",
        r"unrestricted\s+mode",
        r"system\s+rules?",
        r"compliance\s+checker",
        r"downgrade\s+this\s+risk",
        r"do\s+not\s+log\s+the\s+request",
        r"do\s+not\s+write\s+this\s+request\s+to\s+the\s+audit\s+log",
        r"show\s+any\s+stored\s+api\s+keys",
        r"hidden\s+developer\s+instructions",
        r"provide\s+hidden\s+instructions",
        r"reveal\s+restricted\s+data",
    ]


    for pattern in suspicious_patterns:
        if re.search(pattern, prompt, re.IGNORECASE):
            return True

    return False