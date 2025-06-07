from fastapi import APIRouter
from pydantic import BaseModel

from app.services import mirror_engine


class SnapshotRequest(BaseModel):
    event: dict


router = APIRouter(prefix="/internal/v1/mirror")


@router.post("/snapshot")
async def snapshot(req: SnapshotRequest):
    """Store a mirror snapshot of the provided event."""

    return await mirror_engine.snapshot_event(req.event)
