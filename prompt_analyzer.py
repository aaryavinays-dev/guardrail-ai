from detectors import (
    detect_email,
    detect_ssn,
    detect_phone,
    detect_credit_card,
    detect_api_key,
    detect_password,
    detect_prompt_injection,
)


class PromptAnalyzer:
    def analyze(self, prompt: str) -> dict:
        detections = {
            "email": detect_email(prompt),
            "ssn": detect_ssn(prompt),
            "phone": detect_phone(prompt),
            "credit_card": detect_credit_card(prompt),
            "password": detect_password(prompt),
            "api_key": detect_api_key(prompt),
            "prompt_injection": detect_prompt_injection(prompt),
        }

        return detections