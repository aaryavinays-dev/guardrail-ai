from pydantic import BaseModel
from typing import List


class PromptRequest(BaseModel):
    prompt: str


class RiskResponse(BaseModel):
    prompt: str
    word_count: int
    character_count: int
    uppercase_prompt: str
    lowercase_prompt: str
    no_space_prompt: str
    character_without_spaces: int
    reversed_prompt: str
    optimized_prompt: str
    estimated_tokens: int
    optimized_tokens: int
    tokens_saved: int
    risk_level: str
    risk_score: int
    action: str
    risk_reasons: List[str]