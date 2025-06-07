from datetime import datetime
from typing import List

from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    wallet_address: str

class AnalysisResult(BaseModel):
    wallet: str
    flags: List[str]
    score: int
    tier: str
    confidence: float

class MintRequest(BaseModel):
    wallet_address: str

class MintResult(BaseModel):
    token_id: int | str
    metadata: dict
    ipfs_uri: str | None = None
    issued_at: datetime | None = None
