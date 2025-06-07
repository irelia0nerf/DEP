import asyncio
from collections import defaultdict
from typing import Any, AsyncIterator, Dict, List

_subscribers: Dict[str, List[asyncio.Queue]] = defaultdict(list)


async def publish_event(event_type: str, payload: Dict[str, Any]) -> None:
    """Publish an event to all listeners."""
    for queue in list(_subscribers.get(event_type, [])):
        await queue.put(payload)


async def listen_events(event_type: str) -> AsyncIterator[Dict[str, Any]]:
    """Yield events of a specific type as they are published."""
    queue: asyncio.Queue = asyncio.Queue()
    _subscribers[event_type].append(queue)
    try:
        while True:
            payload = await queue.get()
            yield payload
    finally:
        _subscribers[event_type].remove(queue)
