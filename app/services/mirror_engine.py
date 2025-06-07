from datetime import datetime
from typing import Any, Dict, List

from app.utils import db as db_utils

_db_cache = None


def get_db():
    return db_utils.get_db()


def _ensure_db():
    """Return a cached database handle."""
    global _db_cache
    if _db_cache is None:
        _db_cache = get_db()
    return _db_cache


async def snapshot_event(data: Dict[str, Any]) -> Dict[str, Any]:
    """Save a snapshot of the analysis result in MongoDB."""
    db = _ensure_db()
    snapshot = {"event": data, "timestamp": datetime.utcnow()}
    collection = getattr(db, "snapshots", None)
    if collection is not None:
        await collection.insert_one(snapshot)
    return snapshot


async def compare_snapshots(wallet: str) -> Dict[str, Any]:
    """Return the diff between the last two snapshots for a wallet."""
    db = _ensure_db()
    collection = getattr(db, "snapshots", None)
    if collection is None:
        return {}

    cursor = collection.find({}).sort("timestamp", -1)
    all_docs: List[Dict[str, Any]] = await cursor.to_list(length=None)
    docs = [d for d in all_docs if d.get("event", {}).get("wallet") == wallet][:2]
    if len(docs) < 2:
        return {}

    latest_event = docs[0]["event"]
    previous_event = docs[1]["event"]

    flags_latest = set(latest_event.get("flags", []))
    flags_previous = set(previous_event.get("flags", []))

    return {
        "latest": docs[0],
        "previous": docs[1],
        "score_change": latest_event.get("score", 0) - previous_event.get("score", 0),
        "flags_added": list(flags_latest - flags_previous),
        "flags_removed": list(flags_previous - flags_latest),
    }
