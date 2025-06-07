import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import pytest  # noqa: E402
from app.services import dfc  # noqa: E402


def test_simulate_flag_impact():
    proposal = {"data": {"flag": True}}
    impact = simulate_flag_impact(proposal)
    assert impact["score_shift"] == 1
