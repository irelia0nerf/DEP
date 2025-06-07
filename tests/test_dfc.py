import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import pytest  # noqa: E402
from app.services.dfc import simulate_flag_impact  # noqa: E402


@pytest.mark.asyncio
async def test_simulate_flag_impact():
    """Ensure score shift is calculated relative to current weight."""
    proposal = {"flag": "HIGH_BALANCE", "weight": 15}
    impact = await simulate_flag_impact(proposal)
    assert impact["score_shift"] == 5
