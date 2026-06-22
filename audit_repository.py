from collections import Counter

from sqlalchemy.orm import Session

from db_models import AuditLog


def save_audit_log(
    db: Session,
    redacted_prompt: str,
    risk_score: int,
    risk_level: str,
    action: str,
    risk_reasons: list[str],
    user_id: str,
    department: str,
    estimated_tokens: int,
    estimated_cost: float,
) -> AuditLog:
    audit_log = AuditLog(
        redacted_prompt=redacted_prompt,
        risk_score=risk_score,
        risk_level=risk_level,
        action=action,
        risk_reasons=", ".join(risk_reasons),
        prompt_redacted=True,
        user_id=user_id,
        department=department,
        estimated_tokens=estimated_tokens,
        estimated_cost=estimated_cost,
    )

    db.add(audit_log)
    db.commit()
    db.refresh(audit_log)

    return audit_log


def get_audit_summary(db: Session) -> dict:
    total_logs = db.query(AuditLog).count()

    critical_count = (
        db.query(AuditLog)
        .filter(AuditLog.risk_level == "CRITICAL")
        .count()
    )

    high_count = (
        db.query(AuditLog)
        .filter(AuditLog.risk_level == "HIGH")
        .count()
    )

    blocked_count = (
        db.query(AuditLog)
        .filter(AuditLog.action == "BLOCK")
        .count()
    )

    warning_count = (
        db.query(AuditLog)
        .filter(AuditLog.action == "WARN")
        .count()
    )

    recent_logs = (
        db.query(AuditLog)
        .order_by(AuditLog.created_at.desc())
        .limit(5)
        .all()
    )

    recent_log_items = []

    for log in recent_logs:
        recent_log_items.append(
            {
                "id": log.id,
                "created_at": log.created_at.isoformat(),
                "redacted_prompt": log.redacted_prompt,
                "risk_score": log.risk_score,
                "risk_level": log.risk_level,
                "action": log.action,
                "risk_reasons": log.risk_reasons,
                "prompt_redacted": log.prompt_redacted,
                "user_id": log.user_id,
                "department": log.department,
                "estimated_tokens": log.estimated_tokens,
                "estimated_cost": log.estimated_cost,
            }
        )

    return {
        "total_logs": total_logs,
        "critical_count": critical_count,
        "high_count": high_count,
        "blocked_count": blocked_count,
        "warning_count": warning_count,
        "recent_logs": recent_log_items,
    }


def get_department_summary(db: Session) -> dict:
    logs = db.query(AuditLog).all()

    department_data = {}

    for log in logs:
        department = log.department or "Unknown"

        if department not in department_data:
            department_data[department] = {
                "department": department,
                "total_requests": 0,
                "blocked_count": 0,
                "critical_count": 0,
                "risk_reasons_counter": Counter(),
            }

        department_data[department]["total_requests"] += 1

        if log.action == "BLOCK":
            department_data[department]["blocked_count"] += 1

        if log.risk_level == "CRITICAL":
            department_data[department]["critical_count"] += 1

        if log.risk_reasons:
            reasons = [reason.strip() for reason in log.risk_reasons.split(",")]
            department_data[department]["risk_reasons_counter"].update(reasons)

    departments = []

    for data in department_data.values():
        departments.append(
            {
                "department": data["department"],
                "total_requests": data["total_requests"],
                "blocked_count": data["blocked_count"],
                "critical_count": data["critical_count"],
                "top_risk_reasons": dict(
                    data["risk_reasons_counter"].most_common(5)
                ),
            }
        )

    return {"departments": departments}