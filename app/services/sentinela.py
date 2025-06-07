"""Sentinela monitoring service."""

import asyncio
from contextlib import suppress
from typing import Optional

from infra.event_bus import listen_events, publish_event
from app.services import scorelab_service


monitor_task: Optional[asyncio.Task] = None


async def monitor_loop() -> None:
    """Listen for wallet activity events and trigger reanalysis."""
    async for event in listen_events("wallet.activity"):
        wallet = event.get("wallet")
        if wallet:
            await scorelab_service.analyze(wallet)
            await publish_event("score.reanalyzed", {"wallet": wallet})


async def start_monitoring() -> None:
    global monitor_task
    if monitor_task is None or monitor_task.done():
        monitor_task = asyncio.create_task(monitor_loop())


async def stop_monitoring() -> None:
    global monitor_task
    if monitor_task is not None:
        monitor_task.cancel()
        with suppress(asyncio.CancelledError):
            await monitor_task
        monitor_task = None
