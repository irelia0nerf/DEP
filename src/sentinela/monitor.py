from __future__ import annotations

from typing import AsyncIterable, Dict, Any


async def monitor_events(events: AsyncIterable[Dict[str, Any]]):
    """Yield events that should trigger reanalysis."""
    async for event in events:
        if event.get("flagged"):
            yield {
                "wallet_address": event["wallet_address"],
                "context": event.get("context", {}),
            }
