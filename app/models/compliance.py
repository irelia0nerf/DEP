from pydantic import BaseModel


class ComplianceRequest(BaseModel):
    wallet: str
    tier: str


class ComplianceResult(BaseModel):
    wallet: str
    compliant: bool
