import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from src.services.engine import bayes_px, calculate_score  # noqa: E402
from src.models import WalletData  # noqa: E402


def test_bayes_px_bounds():
    assert bayes_px(0.5, 0.5, 0.0) == 0.0
    assert 0.0 <= bayes_px(0.8, 0.4, 0.6) <= 1.0


def test_calculate_score():
    data = WalletData(wallet_address="0xabc", tx_volume=1200, age_days=365)
    result = calculate_score(data)
    assert "score" in result and "tier" in result and "probability" in result
