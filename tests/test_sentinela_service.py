import pytest

from app.services import sentinela


def test_is_flag_trigger():
    assert sentinela.is_flag_trigger({"gas": 60000}) is True
    assert sentinela.is_flag_trigger({"gas": 10}) is False


@pytest.mark.asyncio
async def test_monitor_loop():
    async def gen():
        for g in [10, 60000]:
            yield {"wallet": "0x1", "gas": g}

    results = []
    async for evt in sentinela.monitor_loop(gen()):
        results.append(evt)
    assert len(results) == 1
    assert results[0]["wallet_address"] == "0x1"
