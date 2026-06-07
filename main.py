from fastapi import FastAPI
from datetime import datetime
from detectors import (
    detect_email,       
    detect_ssn,
    detect_phone,
    detect_credit_card,
    detect_api_key,
    detect_password,
    detect_prompt_injection
)


app = FastAPI()

risk_weights = {
    "email": 20,
    "phone": 20,
    "ssn": 50,
    "credit_card": 50,
    "password": 100,
    "api_key": 100,
    "prompt_injection": 100
}


@app.get("/")
def home():
    return {"message": "GuardRail AI is running"}


def determine_action(risk_score):
    if risk_score <= 20:
        action = "ALLOW"

    elif risk_score <= 99:
        action = "WARN"

    else:
        action = "BLOCK"

    return action

def save_audit_log(prompt, risk_score, risk_level, action, risk_reasons):
    timestamp = datetime.now()

    with open("audit_log.txt", "a") as file:
        file.write("--------------------------------------------------\n")
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Prompt: {prompt}\n")
        file.write(f"Risk Score: {risk_score}\n")
        file.write(f"Risk Level: {risk_level}\n")
        file.write(f"Action: {action}\n")
        file.write(f"Risk Reasons: {risk_reasons}\n")
        file.write("--------------------------------------------------\n\n")


@app.post("/analyze")
def analyze_prompt(data: dict):

    prompt = data.get("prompt", "")

    word_count = len(prompt.split())
    character_count = len(prompt)

    uppercase_prompt = prompt.upper()
    lowercase_prompt = prompt.lower()
    reversed_prompt = prompt[::-1]
    no_space_prompt = prompt.replace(" ", "")
    character_without_spaces = len(prompt.replace(" ", ""))

    estimated_tokens = int(word_count * 1.3)

    optimized_prompt = prompt.replace("Best regards", "")
    optimized_prompt = optimized_prompt.replace("Please kindly", "")
    optimized_prompt = optimized_prompt.replace("thank you", "")
    optimized_prompt = optimized_prompt.replace("Sincerely", "")
    optimized_prompt = optimized_prompt.strip()

    optimized_tokens = int(len(optimized_prompt.split()) * 1.3)
    tokens_saved = estimated_tokens - optimized_tokens

    email_detected = detect_email(prompt)
    ssn_detected = detect_ssn(prompt)
    phone_detected = detect_phone(prompt)
    credit_card_detected = detect_credit_card(prompt)
    api_key_detected = detect_api_key(prompt)
    password_detected = detect_password(prompt)
    prompt_injection_detected = detect_prompt_injection(prompt)
    
    
    risk_reasons = []
    risk_score = 0

    if email_detected:
        risk_score += risk_weights["email"]
        risk_reasons.append("Email detected")

    if ssn_detected:
        risk_score += risk_weights["ssn"]
        risk_reasons.append("SSN detected")

    if phone_detected:
        risk_score += risk_weights["phone"]
        risk_reasons.append("Phone number detected")

    if credit_card_detected:
        risk_score += risk_weights["credit_card"]
        risk_reasons.append("Credit card detected")

    if password_detected:
        risk_score += risk_weights["password"]
        risk_reasons.append("Password detected")

    if api_key_detected:
        risk_score += risk_weights["api_key"]
        risk_reasons.append("API Key detected")

    if prompt_injection_detected:
       risk_score += risk_weights["prompt_injection"]
       risk_reasons.append("Prompt injection detected")

    

    if risk_score <= 20:
        risk_level = "LOW"

    elif risk_score <= 50:
        risk_level = "MEDIUM"

    elif risk_score <= 99:
        risk_level = "HIGH"

    else:
        risk_level = "CRITICAL"

    
    action = determine_action(risk_score)
    save_audit_log(prompt, risk_score, risk_level, action, risk_reasons)


    return {
        "prompt": prompt,
        "word_count": word_count,
        "character_count": character_count,
        "uppercase_prompt": uppercase_prompt,
        "lowercase_prompt": lowercase_prompt,
        "no_space_prompt": no_space_prompt,
        "character_without_spaces": character_without_spaces,
        "reversed_prompt": reversed_prompt,
        "optimized_prompt": optimized_prompt,
        "estimated_tokens": estimated_tokens,
        "optimized_tokens": optimized_tokens,
        "tokens_saved": tokens_saved,
        "risk_level": risk_level,
        "risk_score": risk_score,
        "action": action,
        "risk_reasons": risk_reasons
    }