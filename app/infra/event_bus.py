import asyncio
from typing import Any, AsyncGenerator, Dict

_queues: Dict[str, asyncio.Queue] = {}


def _get_queue(topic: str) -> asyncio.Queue:
    if topic not in _queues:
        _queues[topic] = asyncio.Queue()
    return _queues[topic]


async def publish_event(topic: str, payload: Any) -> None:
    queue = _get_queue(topic)
    await queue.put(payload)


async def listen_events(topic: str) -> AsyncGenerator[Any, None]:
    queue = _get_queue(topic)
    while True:
        payload = await queue.get()
        yield payload
