from datetime import datetime
from typing import List

from pydantic import BaseModel


class SnapshotRequest(BaseModel):
    wallet: str
    flags: List[str]
    score: int
    tier: str
    confidence: float
    timestamp: datetime


class SnapshotResult(SnapshotRequest):
    snapshot_id: str
