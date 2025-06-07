import sys
from pathlib import Path

import pytest
import httpx
from httpx import AsyncClient

sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402
from app.routers.sigilmesh import router as sigil_router  # noqa: E402

app.include_router(sigil_router)


@pytest.mark.asyncio
async def test_mint_endpoint(monkeypatch):
    sample_analysis = {
        "wallet": "0xabc",
        "flags": ["MOCK_FLAG"],
        "score": 95,
        "tier": "AAA",
        "confidence": 0.99,
        "timestamp": "2025-01-01T00:00:00Z",
    }
    sample_nft = {"token_id": 1, "metadata": sample_analysis}

    async def mock_get_latest(wallet_address: str):
        return sample_analysis

    async def mock_mint(analysis):
        return sample_nft

    monkeypatch.setattr("app.services.sigilmesh.get_latest_analysis", mock_get_latest)
    monkeypatch.setattr("app.services.sigilmesh.mint_reputation_nft", mock_mint)

    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/internal/v1/sigilmesh/mint",
            json={"wallet_address": "0xabc"},
        )
    assert response.status_code == 200
    data = response.json()
    assert data["token_id"] == 1
    assert set(data["metadata"].keys()) >= {
        "wallet",
        "score",
        "tier",
        "flags",
        "timestamp",
    }


@pytest.mark.asyncio
async def test_mint_reputation_nft_structure():
    from app.services import sigilmesh
    analysis = {
        "wallet": "0xabc",
        "flags": ["A"],
        "score": 80,
        "tier": "AAA",
        "confidence": 0.9,
        "timestamp": sigilmesh.datetime.utcnow(),
    }
    nft = await sigilmesh.mint_reputation_nft(analysis)
    assert "token_id" in nft
    meta = nft["metadata"]
    assert meta["wallet"] == "0xabc"
    assert meta["score"] == 80
    assert meta["tier"] == "AAA"
    assert meta["flags"] == ["A"]
    assert "timestamp" in meta
