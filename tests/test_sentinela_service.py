import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import pytest  # noqa: E402
from app.services import sentinela  # noqa: E402


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
