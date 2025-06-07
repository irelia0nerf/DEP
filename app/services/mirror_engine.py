from datetime import datetime
from typing import Any, Dict, List

# In-memory snapshot storage
_SNAPSHOTS: List[Dict[str, Any]] = []


async def snapshot_event(event: Dict[str, Any]) -> Dict[str, Any]:
    """Store an event snapshot for future audit purposes."""

    snapshot = {"event": event, "timestamp": datetime.utcnow()}
    _SNAPSHOTS.append(snapshot)
    return snapshot


    wallet = data["wallet"]
    previous = _snapshots.get(wallet)
    _snapshots[wallet] = {
        "score": data["score"],
        "flags": list(data["flags"]),
    }
    if not previous:
        return {
            "wallet": wallet,
            "delta_score": 0,
            "added_flags": [],
            "removed_flags": [],
        }
    delta_score = data["score"] - previous["score"]
    added_flags = [f for f in data["flags"] if f not in previous["flags"]]
    removed_flags = [f for f in previous["flags"] if f not in data["flags"]]
    return {
        "wallet": wallet,
        "delta_score": delta_score,
        "added_flags": added_flags,
        "removed_flags": removed_flags,
    }

    return list(_SNAPSHOTS)
