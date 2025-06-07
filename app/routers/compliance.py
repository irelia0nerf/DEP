from fastapi import APIRouter
from app.models.compliance import ComplianceRequest, ComplianceResult
from app.services import compliance


router = APIRouter(prefix="/internal/v1")


@router.post("/compliance/check", response_model=ComplianceResult)
async def check(request: ComplianceRequest):
    return await compliance.check_compliance(request.dict())
