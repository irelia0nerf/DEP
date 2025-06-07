from pydantic import BaseModel
from typing import List


class Snapshot(BaseModel):
    """Snapshot of a wallet reputation state."""

    wallet: str
    score: int
    flags: List[str]


class SnapshotDiff(BaseModel):
    """Difference between two snapshots."""

    wallet: str
    delta_score: int
    added_flags: List[str]
    removed_flags: List[str]
