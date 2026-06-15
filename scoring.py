risk_weights: dict[str, int] = {
    "email": 20,
    "phone": 20,
    "ssn": 50,
    "credit_card": 50,
    "password": 100,
    "api_key": 100,
    "prompt_injection": 100,
}