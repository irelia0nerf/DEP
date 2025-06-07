from datetime import datetime
from typing import Any, Dict, List

from app.utils import db as db_utils


def get_db():
    return db_utils.get_db()


async def snapshot_event(data: Dict[str, Any]) -> Dict[str, Any]:
    """Save a snapshot of the analysis result in MongoDB."""
    db = get_db()
    snapshot = data.copy()
    snapshot["timestamp"] = datetime.utcnow()
    collection = getattr(db, "snapshots", None)
    if collection is not None:
        await collection.insert_one(snapshot)
    return snapshot

    snapshot = {"event": event, "timestamp": datetime.utcnow()}
    _SNAPSHOTS.append(snapshot)
    return snapshot

async def compare_snapshots(wallet: str) -> Dict[str, Any]:
    """Return the diff between the last two snapshots for a wallet."""
    db = get_db()
    collection = getattr(db, "snapshots", None)
    if collection is None:
        return {}
    cursor = collection.find({"wallet": wallet}).sort("timestamp", -1)
    docs: List[Dict[str, Any]] = await cursor.to_list(length=2)
    if len(docs) < 2:
        return {}

    wallet = data["wallet"]
    previous = _snapshots.get(wallet)
    _snapshots[wallet] = {
        "score": data["score"],
        "flags": list(data["flags"]),
    }
    if not previous:
        return {"wallet": wallet, "delta_score": 0, "added_flags": [],
                "removed_flags": []}
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
