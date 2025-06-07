import asyncio

from src.services.engine import bayes_px, calculate_score
from src.models import WalletData


def test_bayes_px_bounds():
    assert bayes_px(0.5, 0.5, 0.0) == 0.0
    assert 0.0 <= bayes_px(0.8, 0.4, 0.6) <= 1.0


def test_calculate_score():
    data = WalletData(wallet_address="0xabc", tx_volume=1200, age_days=365)
    result = asyncio.run(calculate_score(data))
    assert "score" in result and "tier" in result and "probability" in result
