from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, text
from sqlalchemy.sql import func

from database import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    redacted_prompt = Column(Text, nullable=False)
    risk_score = Column(Integer, nullable=False)
    risk_level = Column(String(20), nullable=False)
    action = Column(String(20), nullable=False)
    risk_reasons = Column(Text, nullable=False)
    prompt_redacted = Column(Boolean, server_default=text("true"), nullable=False)
    user_id = Column(String(50), nullable=False)
    department = Column(String(100), nullable=False)