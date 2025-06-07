from __future__ import annotations


from app.infra import event_bus
from app.services import scorelab_service


async def monitor_loop() -> None:
    """Listen for activity events and trigger reanalysis."""
    async for event in event_bus.listen_events("wallet.activity"):
        if event is None or (isinstance(event, dict) and event.get("_stop")):
            break
        wallet = event.get("wallet_address")
        if wallet:
            await scorelab_service.analyze(wallet)
