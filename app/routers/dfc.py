"""Routers for Dynamic Flag Council operations."""

from fastapi import APIRouter
from app.models.dfc import FlagProposal, FlagProposalOut
from app.services import dfc

router = APIRouter(prefix="/internal/v1")


@router.post("/dfc/proposals", response_model=FlagProposalOut)
async def propose_flag(proposal: FlagProposal) -> FlagProposalOut:
    """Submit a flag change proposal and simulate its impact."""

    record = dfc.register_proposal(proposal.dict(), proposal.user_id)
    impact = dfc.simulate_flag_impact(record)
    record.update(impact)
    if impact["score_shift"] > 5:
        record["status"] = "APPROVED_FOR_STAGING"
    return FlagProposalOut(**record)
