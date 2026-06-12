from dotenv import load_dotenv
import os
import json

from fastapi import FastAPI

from audit_logger import AuditLogger
from risk_scorer import RiskScorer
from prompt_analyzer import PromptAnalyzer
from models import PromptRequest, RiskResponse
from scoring import risk_weights, determine_action


load_dotenv()

APP_NAME = os.getenv("APP_NAME", "GuardRail AI")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
RISK_THRESHOLD = int(os.getenv("RISK_THRESHOLD", 50))
AUDIT_LOG_FILE = os.getenv("AUDIT_LOG_FILE", "logs/audit_log.json")


app = FastAPI()

audit_logger = AuditLogger(AUDIT_LOG_FILE)
risk_scorer = RiskScorer(risk_weights, RISK_THRESHOLD)
prompt_analyzer = PromptAnalyzer()


@app.get("/")
def home():
    return {
        "message": f"{APP_NAME} is running",
        "version": APP_VERSION
    }


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

    detections = prompt_analyzer.analyze(prompt)
    risk_score, risk_reasons = risk_scorer.calculate_score(detections)

    if risk_score <= 20:
        risk_level = "LOW"
    elif risk_score <= 50:
        risk_level = "MEDIUM"
    elif risk_score <= 99:
        risk_level = "HIGH"
    else:
        risk_level = "CRITICAL"

    action = determine_action(risk_score)

    audit_logger.save(prompt, risk_score, risk_level, action, risk_reasons)

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


@app.get("/audit-summary")
def audit_summary():
    audit_log_file = os.getenv("AUDIT_LOG_FILE", "logs/audit_log.json")

    if not os.path.exists(audit_log_file):
        return {"message": "No audit logs found"}

    with open(audit_log_file, "r") as file:
        audit_logs = json.load(file)

    risk_scores = [
        log["risk_score"]
        for log in audit_logs
    ]

    high_risk_logs = [
        log
        for log in audit_logs
        if log["risk_score"] >= 50
    ]

    critical_logs = [
        log
        for log in audit_logs
        if log["risk_level"] == "CRITICAL"
    ]

    risk_levels = [
        log["risk_level"]
        for log in audit_logs
    ]

    return {
        "total_logs": len(audit_logs),
        "risk_scores": risk_scores,
        "risk_levels": risk_levels,
        "high_risk_count": len(high_risk_logs),
        "critical_count": len(critical_logs),
        "high_risk_logs": high_risk_logs
    }