"""Endpoints for Mirror Engine."""

from fastapi import APIRouter
from app.models.mirror import Snapshot, SnapshotDiff
from app.services import mirror_engine

router = APIRouter(prefix="/internal/v1")


@router.post("/mirror/snapshot", response_model=SnapshotDiff)
async def snapshot(data: Snapshot) -> SnapshotDiff:
    """Store a snapshot and get difference from previous one."""

    diff = mirror_engine.snapshot_event(data.dict())
    return SnapshotDiff(**diff)
