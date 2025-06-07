from __future__ import annotations

from uuid import uuid4


def register_proposal(flag_data: dict, user_id: str) -> dict:
    """Create and return a new flag change proposal."""
    proposal = {
        "id": str(uuid4()),
        "data": flag_data,
        "user_id": user_id,
        "status": "PENDING",
    }
    return proposal


def simulate_flag_impact(proposal: dict) -> dict:
    """Simulate impact of a flag change on scoring."""
    score_shift = len(proposal.get("data", {})) * 1
    return {"score_shift": score_shift}
