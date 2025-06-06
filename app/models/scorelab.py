from datetime import datetime
from pydantic import BaseModel
from typing import List


class AnalysisRequest(BaseModel):
    wallet_address: str


class AnalysisResult(BaseModel):
    wallet: str
    flags: List[str]
    score: int
    tier: str
    confidence: float
    timestamp: datetime
