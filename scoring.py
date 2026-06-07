risk_weights = {
    "email": 20,
    "phone": 20,
    "ssn": 50,
    "credit_card": 50,
    "password": 100,
    "api_key": 100,
    "prompt_injection": 100
}

def determine_action(risk_score):
    if risk_score <= 20:
        action = "ALLOW"

    elif risk_score <= 99:
        action = "WARN"

    else:
        action = "BLOCK"

    return action