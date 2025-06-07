from fastapi import APIRouter
from app.models.mirror import SnapshotRequest, SnapshotResult
from app.services import mirror_engine


router = APIRouter(prefix="/internal/v1")


@router.post("/mirror/snapshot", response_model=SnapshotResult)
async def snapshot(request: SnapshotRequest):
    return await mirror_engine.snapshot_analysis(request.dict())
