import re

def detect_email(prompt):
    email_detected = re.search(r"\S+@\S+\.\S+", prompt)
    return email_detected


def detect_ssn(prompt):
    ssn_detected = re.search(r"\d{3}-\d{2}-\d{4}", prompt)
    return ssn_detected


def detect_phone(prompt):
    phone_detected = re.search(r"\d{3}-\d{3}-\d{4}", prompt)
    return phone_detected


def detect_credit_card(prompt):
    credit_card_detected = re.search(r"\d{4}(-| )?\d{4}(-| )?\d{4}(-| )?\d{4}", prompt)
    return credit_card_detected

def detect_api_key(prompt):
    api_key_detected = re.search(r"sk-", prompt)
    return api_key_detected

def detect_password(prompt):
    password_detected = re.search(r"password", prompt, re.IGNORECASE)
    return password_detected

def detect_prompt_injection(prompt):
    suspicious_patterns = [
        "Ignore previous instructions",
        "Reveal system prompt",
        "Bypass policy",
        "Forget your rules"
    ]
    for pattern in suspicious_patterns:
        if re.search(pattern, prompt, re.IGNORECASE):
            return True
        
    return False