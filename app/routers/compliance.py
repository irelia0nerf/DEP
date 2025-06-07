"""Endpoints for Compliance Orchestrator."""

from fastapi import APIRouter
from app.models.compliance import ComplianceRequest, ComplianceResult
from app.services import compliance

router = APIRouter(prefix="/internal/v1")


@router.post("/compliance/check", response_model=ComplianceResult)
async def check(req: ComplianceRequest) -> ComplianceResult:
    """Run compliance verification for a wallet."""

    result = await compliance.check_compliance(req.wallet_address)
    return ComplianceResult(**result)
