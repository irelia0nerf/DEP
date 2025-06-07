import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import pytest  # noqa: E402
from app.services import dfc  # noqa: E402


@pytest.mark.asyncio
async def test_register_and_simulate():
    proposal = await dfc.register_proposal({"flag": "TEST", "weight": 10}, "u1")
    assert proposal["flag"] == "TEST"
    impact = await dfc.simulate_flag_impact(proposal)
    assert "score_shift" in impact
