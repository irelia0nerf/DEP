from pydantic import BaseModel
from typing import Optional


class FlagProposal(BaseModel):
    """Data required to propose a new reputation flag."""

    flag: str
    description: str
    user_id: str


class FlagProposalOut(FlagProposal):
    """Response model for a submitted proposal."""

    proposal_id: str
    status: str
    score_shift: Optional[float] = None
