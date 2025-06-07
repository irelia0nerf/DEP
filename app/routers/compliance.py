from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app.services import compliance


class ComplianceRequest(BaseModel):
    wallet_address: str
    verified: bool
    flags: List[str]


router = APIRouter(prefix="/internal/v1/compliance")


@router.post("/evaluate")
def evaluate(req: ComplianceRequest):
    """Return a compliance evaluation for the wallet."""

    kyc_info = {"verified": req.verified}
    return compliance.evaluate(req.wallet_address, kyc_info, req.flags)
