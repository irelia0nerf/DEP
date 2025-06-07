from datetime import datetime
from app.utils.db import get_db


async def save_snapshot(snapshot: dict, db=None) -> None:
    """Persist an analysis snapshot to MongoDB."""
    database = db or get_db()
    if "timestamp" not in snapshot:
        snapshot["timestamp"] = datetime.utcnow()
    await database.snapshots.insert_one(snapshot)


async def compare_snapshot(wallet: str, current: dict, db=None) -> dict:
    """Compare the current snapshot with the last saved one.

    Parameters
    ----------
    wallet:
        Wallet address of the snapshot.
    current:
        Snapshot data produced by the analysis.

    Returns
    -------
    dict
        Dictionary describing score change and flag differences.
    """

    database = db or get_db()
    previous = await database.snapshots.find_one(
        {"wallet": wallet}, sort=[("timestamp", -1)]
    )
    if not previous:
        return {
            "score_change": 0,
            "added_flags": list(current.get("flags", [])),
            "removed_flags": []
        }
    added_flags = sorted(
        set(current.get("flags", [])) - set(previous.get("flags", []))
    )
    removed_flags = sorted(
        set(previous.get("flags", [])) - set(current.get("flags", []))
    )
    score_change = current.get("score", 0) - previous.get("score", 0)
    return {
        "score_change": score_change,
        "added_flags": added_flags,
        "removed_flags": removed_flags,
    }
