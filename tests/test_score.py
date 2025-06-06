import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import pytest  # noqa: E402
from httpx import AsyncClient, ASGITransport  # noqa: E402


@pytest.mark.asyncio
async def test_score_endpoint():
    from main import app  # noqa: E402

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/score/",
            json={"wallet_address": "0xabc", "tx_volume": 1200, "age_days": 365},
        )
    assert response.status_code == 200
    payload = response.json()
    assert "score" in payload
    assert "tier" in payload
    assert 0 <= payload["score"] <= 1000