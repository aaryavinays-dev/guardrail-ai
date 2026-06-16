from sqlalchemy.orm import Session

from db_models import AuditLog


def save_audit_log(
    db: Session,
    redacted_prompt: str,
    risk_score: int,
    risk_level: str,
    action: str,
    risk_reasons: list[str],
) -> AuditLog:
    audit_log = AuditLog(
        redacted_prompt=redacted_prompt,
        risk_score=risk_score,
        risk_level=risk_level,
        action=action,
        risk_reasons=", ".join(risk_reasons),
        prompt_redacted=True,
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