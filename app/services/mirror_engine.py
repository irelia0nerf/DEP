from __future__ import annotations

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

    latest, previous = docs[0], docs[1]
    flags_latest = set(latest.get("flags", []))
    flags_previous = set(previous.get("flags", []))
    return {
        "latest": latest,
        "previous": previous,
        "score_change": latest.get("score", 0) - previous.get("score", 0),
        "flags_added": list(flags_latest - flags_previous),
        "flags_removed": list(flags_previous - flags_latest),
    }