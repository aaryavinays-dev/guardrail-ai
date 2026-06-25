from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException
from openai import OpenAI, OpenAIError
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from audit_logger import AuditLogger
from audit_repository import (
    get_audit_summary,
    get_department_summary,
    save_audit_log,
)
from auth import verify_api_key
from database import get_db
from models import GatewayResponse, PromptRequest, RiskResponse
from policy_engine import apply_department_policy
from prompt_analyzer import PromptAnalyzer
from redactor import redact_prompt
from risk_scorer import RiskScorer
from scoring import risk_weights


load_dotenv()


APP_NAME = os.getenv("APP_NAME", "GuardRail AI")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
AUDIT_LOG_FILE = os.getenv("AUDIT_LOG_FILE", "logs/audit_log.json")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
OPENAI_FAST_MODEL = os.getenv("OPENAI_FAST_MODEL", "gpt-4.1-mini")
OPENAI_STRONG_MODEL = os.getenv("OPENAI_STRONG_MODEL", "gpt-4.1")


def get_risk_threshold() -> int:
    try:
        return int(os.getenv("RISK_THRESHOLD", "100"))
    except ValueError:
        return 100


def select_model(estimated_tokens: int, final_action: str) -> str | None:
    if final_action == "BLOCK":
        return None

    if estimated_tokens <= 50:
        return OPENAI_FAST_MODEL

    return OPENAI_STRONG_MODEL


RISK_THRESHOLD = get_risk_threshold()


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

audit_logger = AuditLogger(AUDIT_LOG_FILE)
risk_scorer = RiskScorer(risk_weights, RISK_THRESHOLD)
prompt_analyzer = PromptAnalyzer()
openai_client = OpenAI()


@app.get("/")
def home() -> dict[str, str]:
    return {
        "message": f"{APP_NAME} is running",
        "version": APP_VERSION,
    }


@app.post(
    "/analyze",
    response_model=RiskResponse,
    dependencies=[Depends(verify_api_key)],
)
def analyze_prompt(request: PromptRequest, db: Session = Depends(get_db)):
    prompt = request.prompt

    word_count = len(prompt.split())
    character_count = len(prompt)
    estimated_tokens = int(word_count * 1.3)
    cost_per_token = 0.000002
    estimated_cost = round(estimated_tokens * cost_per_token, 6)
    blocked_cost_savings = 0.0

    detections = prompt_analyzer.analyze(prompt)
    risk_score, risk_reasons = risk_scorer.calculate_score(detections)

    risk_level = risk_scorer.determine_risk_level(risk_score)
    initial_action = risk_scorer.determine_action(risk_score)

    final_action, risk_reasons = apply_department_policy(
        department=request.department,
        detections=detections,
        current_action=initial_action.value,
        risk_reasons=risk_reasons,
    )

    if final_action == "BLOCK":
        blocked_cost_savings = estimated_cost

    redacted_prompt = redact_prompt(prompt)

    save_audit_log(
        db=db,
        redacted_prompt=redacted_prompt,
        risk_score=risk_score,
        risk_level=risk_level.value,
        action=final_action,
        risk_reasons=risk_reasons,
        user_id=request.user_id,
        department=request.department,
        estimated_tokens=estimated_tokens,
        estimated_cost=estimated_cost,
        blocked_cost_savings=blocked_cost_savings,
    )

    return RiskResponse(
        redacted_prompt=redacted_prompt,
        detections=detections,
        word_count=word_count,
        character_count=character_count,
        estimated_tokens=estimated_tokens,
        estimated_cost=estimated_cost,
        blocked_cost_savings=blocked_cost_savings,
        risk_level=risk_level.value,
        risk_score=risk_score,
        action=final_action,
        risk_reasons=risk_reasons,
        user_id=request.user_id,
        department=request.department,
    )


@app.post(
    "/gateway",
    response_model=GatewayResponse,
    dependencies=[Depends(verify_api_key)],
)
def gateway_prompt(request: PromptRequest, db: Session = Depends(get_db)):
    prompt = request.prompt

    word_count = len(prompt.split())
    character_count = len(prompt)
    estimated_tokens = int(word_count * 1.3)
    cost_per_token = 0.000002
    estimated_cost = round(estimated_tokens * cost_per_token, 6)
    blocked_cost_savings = 0.0

    detections = prompt_analyzer.analyze(prompt)
    risk_score, risk_reasons = risk_scorer.calculate_score(detections)

    risk_level = risk_scorer.determine_risk_level(risk_score)
    initial_action = risk_scorer.determine_action(risk_score)

    final_action, risk_reasons = apply_department_policy(
        department=request.department,
        detections=detections,
        current_action=initial_action.value,
        risk_reasons=risk_reasons,
    )

    selected_model = select_model(
        estimated_tokens=estimated_tokens,
        final_action=final_action,
    )

    if final_action == "BLOCK":
        blocked_cost_savings = estimated_cost

    redacted_prompt = redact_prompt(prompt)

    save_audit_log(
        db=db,
        redacted_prompt=redacted_prompt,
        risk_score=risk_score,
        risk_level=risk_level.value,
        action=final_action,
        risk_reasons=risk_reasons,
        user_id=request.user_id,
        department=request.department,
        estimated_tokens=estimated_tokens,
        estimated_cost=estimated_cost,
        blocked_cost_savings=blocked_cost_savings,
    )

    if final_action == "BLOCK":
        return GatewayResponse(
            redacted_prompt=redacted_prompt,
            detections=detections,
            risk_level=risk_level.value,
            risk_score=risk_score,
            action=final_action,
            risk_reasons=risk_reasons,
            user_id=request.user_id,
            department=request.department,
            estimated_tokens=estimated_tokens,
            estimated_cost=estimated_cost,
            blocked_cost_savings=blocked_cost_savings,
            ai_response="Prompt blocked by GuardRail AI policy. Model was not called.",
            model_called=False,
            selected_model=selected_model,
        )

    try:
        ai_result = openai_client.responses.create(
            model=selected_model,
            input=redacted_prompt,
        )

        ai_response = ai_result.output_text
        model_called = True

    except OpenAIError:
        ai_response = (
            "Model call failed due to OpenAI provider quota, billing, or configuration issue."
        )
        model_called = False

    return GatewayResponse(
        redacted_prompt=redacted_prompt,
        detections=detections,
        risk_level=risk_level.value,
        risk_score=risk_score,
        action=final_action,
        risk_reasons=risk_reasons,
        user_id=request.user_id,
        department=request.department,
        estimated_tokens=estimated_tokens,
        estimated_cost=estimated_cost,
        blocked_cost_savings=blocked_cost_savings,
        ai_response=ai_response,
        model_called=model_called,
        selected_model=selected_model,
    )


@app.get(
    "/audit-summary",
    dependencies=[Depends(verify_api_key)],
)
def audit_summary(db: Session = Depends(get_db)):
    return get_audit_summary(db)


@app.get(
    "/department-summary",
    dependencies=[Depends(verify_api_key)],
)
def department_summary(db: Session = Depends(get_db)):
    return get_department_summary(db)


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