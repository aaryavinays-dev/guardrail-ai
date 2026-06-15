from dotenv import load_dotenv
import os
from typing import Any

from fastapi import FastAPI

from audit_logger import AuditLogger
from risk_scorer import RiskScorer
from prompt_analyzer import PromptAnalyzer
from models import PromptRequest, RiskResponse
from scoring import risk_weights


load_dotenv()


APP_NAME = os.getenv("APP_NAME", "GuardRail AI")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
AUDIT_LOG_FILE = os.getenv("AUDIT_LOG_FILE", "logs/audit_log.json")


def get_risk_threshold() -> int:
    try:
        return int(os.getenv("RISK_THRESHOLD", "100"))
    except ValueError:
        return 100


RISK_THRESHOLD = get_risk_threshold()


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)

audit_logger = AuditLogger(AUDIT_LOG_FILE)
risk_scorer = RiskScorer(risk_weights, RISK_THRESHOLD)
prompt_analyzer = PromptAnalyzer()


@app.get("/")
def home() -> dict[str, str]:
    return {
        "message": f"{APP_NAME} is running",
        "version": APP_VERSION,
    }


@app.post("/analyze", response_model=RiskResponse)
def analyze_prompt(request: PromptRequest) -> RiskResponse:
    prompt = request.prompt

    word_count = len(prompt.split())
    character_count = len(prompt)
    estimated_tokens = int(word_count * 1.3)

    detections = prompt_analyzer.analyze(prompt)
    risk_score, risk_reasons = risk_scorer.calculate_score(detections)

    risk_level = risk_scorer.determine_risk_level(risk_score)
    action = risk_scorer.determine_action(risk_score)

    redacted_prompt = audit_logger.redact_prompt(prompt)

    audit_logger.save(prompt, risk_score, risk_level, action, risk_reasons)

    return RiskResponse(
        redacted_prompt=redacted_prompt,
        detections=detections,
        word_count=word_count,
        character_count=character_count,
        estimated_tokens=estimated_tokens,
        risk_level=risk_level,
        risk_score=risk_score,
        action=action,
        risk_reasons=risk_reasons,
    )


@app.get("/audit-summary")
def audit_summary() -> dict[str, Any]:
    audit_logs = audit_logger.load_logs()

    risk_scores = [
        log.get("risk_score", 0)
        for log in audit_logs
    ]

    risk_levels = [
        log.get("risk_level", "UNKNOWN")
        for log in audit_logs
    ]

    high_risk_logs = [
        log
        for log in audit_logs
        if log.get("risk_score", 0) >= 50
    ]

    critical_logs = [
        log
        for log in audit_logs
        if log.get("risk_level") == "CRITICAL"
    ]

    return {
        "total_logs": len(audit_logs),
        "risk_scores": risk_scores,
        "risk_levels": risk_levels,
        "high_risk_count": len(high_risk_logs),
        "critical_count": len(critical_logs),
        "high_risk_logs": high_risk_logs,
    }