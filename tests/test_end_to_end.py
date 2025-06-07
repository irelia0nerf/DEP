import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.mark.asyncio
async def test_full_analysis_flow(monkeypatch):
    async def mock_analyze(wallet_address: str):
        return {
            "wallet": wallet_address,
            "flags": ["MOCK_FLAG"],
            "score": 75,
            "tier": "BB",
            "confidence": 0.9,
        }

    monkeypatch.setattr(
        "app.services.scorelab_service.analyze", mock_analyze
    )

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post(
            "/internal/v1/scorelab/analyze",
            json={"wallet_address": "0xabc"},
        )

    assert resp.status_code == 200
    data = resp.json()
    assert data["wallet"] == "0xabc"
    assert data["tier"] == "BB"
