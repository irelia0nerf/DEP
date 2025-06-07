from datetime import datetime
from typing import Any, Dict, List
from uuid import uuid4

from app.services import score_engine

# In-memory store of proposals for demo purposes
_PROPOSALS: List[Dict[str, Any]] = []


async def register_proposal(flag_data: Dict[str, Any], user_id: str) -> Dict[str, Any]:
    """Register a flag proposal and return its stored representation."""

    proposal = {
        "id": uuid4().hex,
        "flag": flag_data.get("flag"),
        "weight": int(flag_data.get("weight", 0)),
        "user_id": user_id,
        "status": "PENDING",
        "created_at": datetime.utcnow(),
    }
    _PROPOSALS.append(proposal)
    return proposal


async def simulate_flag_impact(proposal: Dict[str, Any]) -> Dict[str, int]:
    """Return the expected score shift if the proposal is approved."""

    weights = score_engine.load_weights()
    current = weights.get(proposal["flag"], 0)
    score_shift = proposal.get("weight", 0) - current
    return {"score_shift": score_shift}
