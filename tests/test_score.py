import pytest
from httpx import AsyncClient

from main import app
from app.services.engine import calculate_px


@pytest.mark.asyncio
async def test_calculate_score_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
            "wallet_address": "0xabc",
            "tx_volume": 1200,
            "age_days": 10,
        }
        response = await ac.post("/score/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "px" in data and 0 <= data["px"] <= 1


def test_calculate_px_function():
    flags = {"new_wallet": True, "high_volume": True}
    weights = {"new_wallet": -0.15, "high_volume": 0.10}
    px = calculate_px(flags, weights)
    assert 0 <= px <= 1
