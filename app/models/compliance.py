from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel


class ComplianceEvaluationRequest(BaseModel):
    wallet_address: str
    rules: List[str]


class ComplianceEvaluationResult(BaseModel):
    wallet: str
    rules: List[str]
    results: Dict[str, bool]
    passed: bool
    flags: List[str]
    tier: str
    timestamp: datetime
