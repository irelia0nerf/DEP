import asyncio
from fastapi import APIRouter

from app.models.sentinela import Event
from app.services import sentinela, scorelab_service
from infra import event_bus

router = APIRouter(prefix="/internal/v1/sentinela")
 codex/update-tests-and-fix-imports

monitor_task: asyncio.Task | None = None


 codex/remove-unused-imports-and-fix-flake8-issues
monitor_task: asyncio.Task | None = None

# Background task running the event monitor loop.
_monitor_task: asyncio.Task | None = None
 main
 main


@router.post("/start")
async def start_monitor() -> dict:
    """Start monitoring wallet activity events."""
 codex/update-tests-and-fix-imports

 codex/remove-unused-imports-and-fix-flake8-issues
 main
    global monitor_task
    if monitor_task and not monitor_task.done():


    global _monitor_task
    if _monitor_task and not _monitor_task.done():
 main
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
 codex/update-tests-and-fix-imports

 codex/remove-unused-imports-and-fix-flake8-issues
 main
    global monitor_task
    if monitor_task and not monitor_task.done():
        monitor_task.cancel()


    global _monitor_task
    if _monitor_task:
        _monitor_task.cancel()
 main
        try:
            await _monitor_task
        except asyncio.CancelledError:
            pass
        _monitor_task = None
    return {"status": "stopped"}
 codex/update-tests-and-fix-imports



 codex/remove-unused-imports-and-fix-flake8-issues





 main
 main
@router.post("/check")
def check_event(event: Event) -> dict:
    """Check whether the given event would trigger a reanalysis."""
    return {"trigger": sentinela.is_flag_trigger(event.model_dump())}
