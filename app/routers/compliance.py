from typing import List
from fastapi import APIRouter

from app.models.compliance import (
    ComplianceEvaluationRequest,
    ComplianceEvaluationResult,
)
from app.services import compliance

router = APIRouter(prefix="/internal/v1/compliance")


@router.post("/evaluate", response_model=ComplianceEvaluationResult)
async def evaluate(request: ComplianceEvaluationRequest):
    """Evaluate compliance rules for a wallet."""
    return await compliance.evaluate_rules(request.wallet_address, request.rules)


@router.get("/logs", response_model=List[ComplianceEvaluationResult])
async def logs(limit: int = 20):
    """Return recent compliance evaluation logs."""
    return await compliance.get_logs(limit)
