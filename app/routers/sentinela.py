import asyncio
from fastapi import APIRouter

from app.models.sentinela import Event
from app.services import sentinela, scorelab_service
from infra import event_bus

router = APIRouter(prefix="/internal/v1/sentinela")

# Background task running the event monitor loop.
_monitor_task: asyncio.Task | None = None


@router.post("/start")
async def start_monitor() -> dict:
    """Start monitoring wallet activity events."""

    global _monitor_task
    if _monitor_task and not _monitor_task.done():
        return {"status": "running"}

    async def _run() -> None:
        """Process incoming events and trigger analyses."""
        events = sentinela.monitor_loop(event_bus.listen_events("wallet.activity"))
        async for payload in events:
            await scorelab_service.analyze(payload["wallet_address"])

    def _clear_task(_: asyncio.Task) -> None:
        global _monitor_task
        _monitor_task = None

    _monitor_task = asyncio.create_task(_run())
    _monitor_task.add_done_callback(_clear_task)
    await asyncio.sleep(0)
    return {"status": "started"}


@router.post("/stop")
async def stop_monitor() -> dict:
    """Stop the monitoring task if running."""

    global _monitor_task
    if _monitor_task:
        _monitor_task.cancel()
        try:
            await _monitor_task
        except asyncio.CancelledError:
            pass
        _monitor_task = None
    return {"status": "stopped"}


@router.post("/check")
def check_event(event: Event) -> dict:
    """Check whether the given event would trigger a reanalysis."""

    return {"trigger": sentinela.is_flag_trigger(event.model_dump())}
