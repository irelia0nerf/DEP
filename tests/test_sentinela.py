import pytest

from src.sentinela import monitor_events


@pytest.mark.asyncio
async def test_monitor_events():
    async def gen():
        for e in [
            {"wallet_address": "0x1", "flagged": True, "context": {"x": 1}},
            {"wallet_address": "0x2", "flagged": False},
        ]:
            yield e
    events = []
    async for ev in monitor_events(gen()):
        events.append(ev)
    assert events == [{"wallet_address": "0x1", "context": {"x": 1}}]
