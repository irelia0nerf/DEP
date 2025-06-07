import sys
from pathlib import Path

import pytest
import httpx
from httpx import AsyncClient

sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402
from app.routers.scorelab import router as scorelab_router  # noqa: E402

app.include_router(scorelab_router)


@pytest.mark.asyncio
async def test_scorelab_analyze(monkeypatch):
    async def mock_analyze(wallet_address: str):
        return {
            "wallet": wallet_address,
            "flags": ["MOCK_FLAG"],
            "score": 90,
            "tier": "AAA",
            "confidence": 0.99,
            "timestamp": "2025-01-01T00:00:00Z",
        }

    monkeypatch.setattr("app.services.scorelab_service.analyze", mock_analyze)
    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/internal/v1/scorelab/analyze",
            json={"wallet_address": "0x123"},
        )
    assert response.status_code == 200
    data = response.json()
    assert data["wallet"] == "0x123"
    assert data["tier"] == "AAA"


def test_aggregate_flags_verified():
    from app.services.scorelab_service import aggregate_flags

    result = aggregate_flags([
        "MIXER_USAGE",
        "HIGH_BALANCE",
        "MIXER_USAGE",
    ], {"verified": True})

    expected = ["HIGH_BALANCE", "MIXER_USAGE", "KYC_VERIFIED"]
    assert result == expected


def test_aggregate_flags_unverified():
    from app.services.scorelab_service import aggregate_flags

    result = aggregate_flags([
        "HIGH_BALANCE",
        "MIXER_USAGE",
        "HIGH_BALANCE",
    ], {"verified": False})

    expected = ["HIGH_BALANCE", "MIXER_USAGE"]
    assert result == expected


def test_aggregate_flags_empty_identity():
    from app.services.scorelab_service import aggregate_flags

    result = aggregate_flags(["MIXER_USAGE", "MIXER_USAGE"], {})

    assert result == ["MIXER_USAGE"]
