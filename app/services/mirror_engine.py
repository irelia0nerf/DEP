"""Mirror Engine compares snapshot evolution."""

from __future__ import annotations

from typing import Dict, List

_snapshots: Dict[str, Dict] = {}


def snapshot_event(data: Dict) -> Dict:
    """Store a snapshot and return difference from previous state."""

    wallet = data["wallet"]
    previous = _snapshots.get(wallet)
    _snapshots[wallet] = {"score": data["score"], "flags": list(data["flags"])}
    if not previous:
        return {"wallet": wallet, "delta_score": 0, "added_flags": [], "removed_flags": []}
    delta_score = data["score"] - previous["score"]
    added_flags = [f for f in data["flags"] if f not in previous["flags"]]
    removed_flags = [f for f in previous["flags"] if f not in data["flags"]]
    return {
        "wallet": wallet,
        "delta_score": delta_score,
        "added_flags": added_flags,
        "removed_flags": removed_flags,
    }


def get_history(wallet: str) -> List[Dict]:
    """Retrieve stored history for a wallet."""

    if wallet in _snapshots:
        return [{"wallet": wallet, **_snapshots[wallet]}]
    return []
