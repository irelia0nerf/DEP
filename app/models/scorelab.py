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


class MintRequest(BaseModel):
    wallet_address: str


class MintResult(BaseModel):
    wallet: str
    score: int
    tier: str
    flags: List[str]
    cid: str
    did: str
