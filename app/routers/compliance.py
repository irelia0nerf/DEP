from typing import List
from fastapi import APIRouter

from app.models.compliance import ComplianceRequest, ComplianceResult
from app.services import compliance

router = APIRouter(prefix="/internal/v1/compliance")


@router.post("/evaluate", response_model=ComplianceResult)
async def evaluate(req: ComplianceRequest):
    return await compliance.evaluate(req.wallet_address)


@router.get("/logs", response_model=List[ComplianceResult])
async def logs(limit: int = 10):
    return await compliance.get_logs(limit)
