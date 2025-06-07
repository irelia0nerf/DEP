from datetime import datetime
from typing import Any, Dict, List

# In-memory snapshot storage
_SNAPSHOTS: List[Dict[str, Any]] = []


async def snapshot_event(event: Dict[str, Any]) -> Dict[str, Any]:
    """Store an event snapshot for future audit purposes."""

    snapshot = {"event": event, "timestamp": datetime.utcnow()}
    _SNAPSHOTS.append(snapshot)
    return snapshot


def get_snapshots() -> List[Dict[str, Any]]:
    """Return all stored snapshots."""

    return list(_SNAPSHOTS)
