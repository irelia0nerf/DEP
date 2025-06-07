import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import pytest  # noqa: E402
from app.services import mirror_engine  # noqa: E402


@pytest.mark.asyncio
async def test_snapshot_event():
    event = {"foo": "bar"}
    snapshot = await mirror_engine.snapshot_event(event)
    assert snapshot["event"] == event
    assert "timestamp" in snapshot
