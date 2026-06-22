from pydantic import BaseModel, Field


class PromptRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        description="User prompt to analyze for sensitive data and prompt injection risk.",
    )
    user_id: str = Field(
        ...,
        min_length=1,
        description="Unique identifier for the user submitting the prompt.",
    )
    department: str = Field(
        ...,
        min_length=1,
        description="Department or business unit submitting the prompt.",
    )


class RiskResponse(BaseModel):
    redacted_prompt: str
    detections: dict[str, bool]
    word_count: int
    character_count: int
    risk_level: str
    risk_score: int
    action: str
    risk_reasons: list[str]
    user_id: str
    department: str 
    estimated_tokens: int
    estimated_cost: float
    blocked_cost_savings: float