import sys
from pathlib import Path

import pytest
import httpx
from httpx import AsyncClient

sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402


@pytest.mark.asyncio
async def test_mint_nft(monkeypatch):
    async def mock_get_analysis(wallet_address: str):
        return {
            "wallet": wallet_address,
            "flags": ["MOCK"],
            "score": 99,
            "tier": "AAA",
            "confidence": 0.9,
        }

    async def mock_mint(analysis: dict):
        return {
            "wallet": analysis["wallet"],
            "score": analysis["score"],
            "tier": analysis["tier"],
            "flags": analysis["flags"],
            "cid": "cid123",
            "did": "did:example:123456",
        }

    monkeypatch.setattr("app.services.scorelab_service.get_analysis", mock_get_analysis)
    monkeypatch.setattr("app.services.sigilmesh.mint_reputation_nft", mock_mint)

    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        url = "/internal/v1/sigilmesh/mint"
        response = await ac.post(url, json={"wallet_address": "0xabc"})

    assert response.status_code == 200
    data = response.json()
    assert data["wallet"] == "0xabc"
    assert data["cid"] == "cid123"
    assert data["did"].startswith("did:example:")
