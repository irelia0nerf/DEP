from typing import List
from pydantic import BaseModel


class ComplianceRequest(BaseModel):
    wallet_address: str


class ComplianceResult(BaseModel):
    wallet: str
    kyc_verified: bool
    kyt_flags: List[str]
    status: str
    ts: str
