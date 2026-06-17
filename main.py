from dotenv import load_dotenv
import os
from typing import Any
from redactor import redact_prompt

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from audit_repository import get_audit_summary, save_audit_log
from database import get_db

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
def analyze_prompt(request: PromptRequest, db: Session = Depends(get_db)):
    prompt = request.prompt

    word_count = len(prompt.split())
    character_count = len(prompt)
    estimated_tokens = int(word_count * 1.3)

    detections = prompt_analyzer.analyze(prompt)
    risk_score, risk_reasons = risk_scorer.calculate_score(detections)

    risk_level = risk_scorer.determine_risk_level(risk_score)
    action = risk_scorer.determine_action(risk_score)

    redacted_prompt = redact_prompt(prompt)

    save_audit_log(
    db=db,
    redacted_prompt=redacted_prompt,
    risk_score=risk_score,
    risk_level=risk_level.value,
    action=action.value,
    risk_reasons=risk_reasons,
)

    return RiskResponse(
        redacted_prompt=redacted_prompt,
        detections=detections,
        word_count=word_count,
        character_count=character_count,
        estimated_tokens=estimated_tokens,
        risk_level=risk_level.value,
        risk_score=risk_score,
        action=action.value,
        risk_reasons=risk_reasons,
    )


@app.get("/audit-summary")
def audit_summary(db: Session = Depends(get_db)):
    return get_audit_summary(db)

@app.get("/health/db")
def database_health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "ok",
            "database": "connected",
        }

    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed",
        )