from fastapi import FastAPI
from audit_logger import save_audit_log
from models import PromptRequest, RiskResponse
from detectors import (
    detect_email,
    detect_ssn,
    detect_phone,
    detect_credit_card,
    detect_api_key,
    detect_password,
    detect_prompt_injection,
)
from scoring import risk_weights, determine_action


app = FastAPI()


@app.get("/")
def home():
    return {"message": "GuardRail AI is running"}


@app.post("/analyze", response_model=RiskResponse)
def analyze_prompt(request: PromptRequest):
    prompt = request.prompt

    word_count = len(prompt.split())
    character_count = len(prompt)

    uppercase_prompt = prompt.upper()
    lowercase_prompt = prompt.lower()
    reversed_prompt = prompt[::-1]
    no_space_prompt = prompt.replace(" ", "")
    character_without_spaces = len(no_space_prompt)

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

    return RiskResponse(
        prompt=prompt,
        word_count=word_count,
        character_count=character_count,
        uppercase_prompt=uppercase_prompt,
        lowercase_prompt=lowercase_prompt,
        no_space_prompt=no_space_prompt,
        character_without_spaces=character_without_spaces,
        reversed_prompt=reversed_prompt,
        optimized_prompt=optimized_prompt,
        estimated_tokens=estimated_tokens,
        optimized_tokens=optimized_tokens,
        tokens_saved=tokens_saved,
        risk_level=risk_level,
        risk_score=risk_score,
        action=action,
        risk_reasons=risk_reasons,
    )