"""Dynamic Flag Council service logic."""

from __future__ import annotations

import uuid
from typing import Dict, List

_proposals: Dict[str, Dict] = {}


def register_proposal(flag_data: Dict, user_id: str) -> Dict:
    """Register a flag change proposal.

    Args:
        flag_data: Information about the new flag.
        user_id: Identifier of the proposing user.

    Returns:
        Proposal record with generated ID and status.
    """

    proposal_id = str(uuid.uuid4())
    proposal = {
        "proposal_id": proposal_id,
        "flag": flag_data.get("flag"),
        "description": flag_data.get("description", ""),
        "user_id": user_id,
        "status": "PENDING",
    }
    _proposals[proposal_id] = proposal
    return proposal


def simulate_flag_impact(proposal: Dict) -> Dict[str, float]:
    """Simulate impact of a proposal on scoring logic."""

    # Simplistic impact: flags with certain keywords have higher score impact
    flag = proposal.get("flag", "")
    score_shift = 10.0 if "mixer" in flag.lower() else 2.0
    return {"score_shift": score_shift}


def list_proposals() -> List[Dict]:
    """Return all stored proposals."""

    return list(_proposals.values())
