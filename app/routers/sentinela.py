from __future__ import annotations

import asyncio
from fastapi import APIRouter

from app.infra import event_bus
from app.services import sentinela as sentinela_service

router = APIRouter(prefix="/sentinela")

_monitor_task: asyncio.Task | None = None


@router.post("/start")
async def start_monitoring():
    """Start the Sentinela monitor loop."""
    global _monitor_task
    if _monitor_task is None or _monitor_task.done():
        _monitor_task = asyncio.create_task(sentinela_service.monitor_loop())
        return {"status": "started"}
    return {"status": "running"}


@router.post("/stop")
async def stop_monitoring():
    """Stop the Sentinela monitor loop."""
    global _monitor_task
    if _monitor_task and not _monitor_task.done():
        await event_bus.publish_event("wallet.activity", {"_stop": True})
        await _monitor_task
        _monitor_task = None
        return {"status": "stopped"}
    return {"status": "not_running"}
