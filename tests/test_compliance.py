import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from app.services import compliance  # noqa: E402


def test_evaluate_pass():
    result = compliance.evaluate("0x1", {"verified": True}, ["A"])
    assert result["status"] == "REVIEW"


def test_evaluate_fail():
    result = compliance.evaluate("0x1", {"verified": False}, ["A", "B", "C", "D"])
    assert result["status"] == "FAIL"
