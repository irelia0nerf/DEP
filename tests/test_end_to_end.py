import sys
from pathlib import Path
import types

import pytest
import httpx
from httpx import AsyncClient

# Ensure app import path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402


@pytest.mark.asyncio
async def test_full_analysis_flow(monkeypatch):
    """Simulate analysis to NFT minting with patched services."""

    # Step 1: patch ScoreLab dependencies
    async def mock_analyze_wallet(addr: str):
        return ["MIXER_USAGE", "HIGH_BALANCE"]

    async def mock_get_identity(addr: str):
        return {"wallet": addr, "verified": True}

    def mock_calculate(flags):
        return 95, "AAA", 0.99

    class DummyColl:
        async def insert_one(self, data):
            self.saved = data

    class DummyDB:
        def __init__(self):
            self.analysis = DummyColl()

    dummy_db = DummyDB()
    monkeypatch.setattr(
        "app.services.sherlock.analyze_wallet",
        mock_analyze_wallet,
    )
    monkeypatch.setattr(
        "src.sherlock.analyzer.analyze_wallet",
        mock_analyze_wallet,
    )
    monkeypatch.setattr(
        "src.scorelab_core.core.analyze_wallet",
        mock_analyze_wallet,
    )
    monkeypatch.setattr("app.services.kyc.get_identity", mock_get_identity)
    monkeypatch.setattr("app.services.score_engine.calculate", mock_calculate)
    monkeypatch.setattr("app.utils.db.get_db", lambda: dummy_db)
    monkeypatch.setattr("app.services.scorelab_service.get_db", lambda: dummy_db)
    monkeypatch.setattr("src.scorelab_core.core.get_db", lambda: dummy_db)

    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post(
            "/internal/v1/scorelab/analyze",
            json={"wallet_address": "0x" + "a" * 40},
        )
    assert resp.status_code == 200
    analysis = resp.json()
    assert analysis["wallet"] == "0x" + "a" * 40

    # Step 2: Mirror Engine comparison
    def mock_compare(current):
        return {"delta": 0, **current}

    mirror_engine = types.SimpleNamespace(compare=mock_compare)

    # Step 3: Compliance check
    def mock_check(result):
        return result["score"] >= 50

    compliance = types.SimpleNamespace(check=mock_check)

    # Step 4: SigilMesh minting
    def mock_mint(data):
        return {"token_id": "1", "wallet": data["wallet"]}

    sigilmesh = types.SimpleNamespace(mint_reputation_nft=mock_mint)

    # Execute mocked pipeline
    compared = mirror_engine.compare(analysis)
    assert compared["delta"] == 0
    assert compliance.check(compared)
    nft = sigilmesh.mint_reputation_nft(compared)
    assert nft["wallet"] == "0x" + "a" * 40
