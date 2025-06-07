from typing import Any, AsyncGenerator, AsyncIterator, Dict

THRESHOLD_GAS = 50000


def is_flag_trigger(event: Dict[str, Any]) -> bool:
    """Return ``True`` if the event should trigger a reanalysis."""

    return event.get("gas", 0) > THRESHOLD_GAS or event.get("anomaly", False)


async def monitor_loop(
    events: AsyncIterator[Dict[str, Any]],
) -> AsyncGenerator[Dict[str, Any], None]:
    """Yield events that pass the trigger rules."""

    async for event in events:
        if is_flag_trigger(event):
            yield {"wallet_address": event.get("wallet"), "context": event}
