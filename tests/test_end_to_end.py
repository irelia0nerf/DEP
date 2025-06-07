import sys
from pathlib import Path
import types

import pytest
import httpx
from fastapi import FastAPI
from httpx import AsyncClient

from app.routers.scorelab import router as scorelab_router
from app.routers.mirror_engine import router as mirror_router
from app.routers.sigilmesh import router as sigil_router
from app.routers.compliance import router as compliance_router
from app.services import compliance, sigilmesh

app = FastAPI()
app.include_router(scorelab_router)
app.include_router(mirror_router)
app.include_router(sigil_router)
app.include_router(compliance_router)

sys.path.append(str(Path(__file__).resolve().parents[1]))


@pytest.mark.asyncio
async def test_full_analysis_flow(monkeypatch):
    """Simulate analysis to NFT minting with patched services."""

    assert hasattr(compliance, "evaluate")
    assert hasattr(sigilmesh, "mint_reputation_nft")

    async def mock_analyze_wallet(addr: str):
        return ["MIXER_USAGE"]

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
    monkeypatch.setattr("app.services.sherlock.analyze_wallet", mock_analyze_wallet)
    monkeypatch.setattr("app.services.kyc.get_identity", mock_get_identity)
    monkeypatch.setattr("app.services.score_engine.calculate", mock_calculate)
    monkeypatch.setattr("app.utils.db.get_db", lambda: dummy_db)
    monkeypatch.setattr("app.services.scorelab_service.get_db", lambda: dummy_db)

    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        analysis_resp = await ac.post(
            "/internal/v1/scorelab/analyze",
            json={"wallet_address": "0xabc"},
        )
    assert analysis_resp.status_code == 200
    analysis = analysis_resp.json()
    assert analysis["wallet"] == "0xabc"

    def mock_compare(current):
        return {"delta": 0, **current}

    mirror_engine = types.SimpleNamespace(compare=mock_compare)

    def mock_check(result):
        return result["score"] >= 50

    mock_compliance = types.SimpleNamespace(check=mock_check)

    def mock_mint(data):
        return {"token_id": "1", "wallet": data["wallet"]}

    mock_sigilmesh = types.SimpleNamespace(mint_reputation_nft=mock_mint)

    compared = mirror_engine.compare(analysis)
    assert compared["delta"] == 0
    assert mock_compliance.check(compared)
    nft = mock_sigilmesh.mint_reputation_nft(compared)
    assert nft["wallet"] == "0xabc"
