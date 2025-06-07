from pydantic import BaseModel
from typing import List


class ComplianceRequest(BaseModel):
    """Input for compliance checks."""

    wallet_address: str


class ComplianceResult(BaseModel):
    """Output of compliance verification."""

    wallet: str
    passes: bool
    issues: List[str]
