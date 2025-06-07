from fastapi import APIRouter
from pydantic import BaseModel

from app.services import dfc


class ProposalRequest(BaseModel):
    flag: str
    weight: int
    user_id: str


router = APIRouter(prefix="/internal/v1/dfc")


@router.post("/proposals")
async def propose_flag_change(request: ProposalRequest):
    """Register a new flag proposal and simulate its impact."""

    proposal = await dfc.register_proposal(
        {"flag": request.flag, "weight": request.weight}, request.user_id
    )
    impact = await dfc.simulate_flag_impact(proposal)
    if impact["score_shift"] > 5:
        proposal["status"] = "APPROVED_FOR_STAGING"
    proposal["impact"] = impact
    return proposal
