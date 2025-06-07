import asyncio
from fastapi import APIRouter

from app.models.sentinela import Event
from app.services import sentinela, scorelab_service
from infra import event_bus

router = APIRouter(prefix="/internal/v1/sentinela")

monitor_task: asyncio.Task | None = None


@router.post("/start")
async def start_monitor() -> dict:
    """Start monitoring wallet activity events."""

    global monitor_task
    if monitor_task and not monitor_task.done():
        return {"status": "running"}

    async def loop() -> None:
        async for payload in event_bus.listen_events("wallet.activity"):
            await scorelab_service.analyze(payload["wallet_address"])

    monitor_task = asyncio.create_task(loop())
    await asyncio.sleep(0)
    return {"status": "started"}


@router.post("/stop")
async def stop_monitor() -> dict:
    """Stop the monitoring task if running."""

    global monitor_task
    if monitor_task and not monitor_task.done():
        monitor_task.cancel()
        try:
            await monitor_task
        except asyncio.CancelledError:
            pass
    monitor_task = None
    return {"status": "stopped"}


@router.post("/check")
def check_event(event: Event) -> dict:
    """Check whether the given event would trigger a reanalysis."""

    return {"trigger": sentinela.is_flag_trigger(event.model_dump())}
