 codex/fix-174-workflow-errors

import sys
from pathlib import Path
 main
import types

import pytest
import httpx
from fastapi import FastAPI
from httpx import AsyncClient

 codex/fix-174-workflow-errors
# Create a minimal app for testing
from app.routers import scorelab  # noqa: E402

from app.routers.scorelab import router as scorelab_router
from app.routers.mirror_engine import router as mirror_router
from app.routers.sigilmesh import router as sigil_router
from app.routers.compliance import router as compliance_router
from app.services import compliance, sigilmesh
 main

app = FastAPI()
 codex/update-tests-and-fix-imports

app.include_router(scorelab.router)

 codex/fix-174-workflow-errors

# Ensure app import path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402
 codex/preencher-src/utils/db.py-com-lógica-de-app/utils/db.py
from app.routers.scorelab import router as scorelab_router  # noqa: E402
from app.routers.mirror_engine import router as mirror_router  # noqa: E402
from app.routers.sigilmesh import router as sigil_router  # noqa: E402
from app.routers.compliance import router as compliance_router  # noqa: E402
 6gjf82-codex/editar-src/utils/db.py-para-get_db
from app.services.compliance import compliance  # noqa: E402
from app.services import sigilmesh  # noqa: E402

from app.services import compliance, sigilmesh  # noqa: E402


async def mock_get_identity(wallet_address: str):
    return {
        "wallet": wallet_address,
        "verified": True,
        "kyc_level": 1,
        "pii": {"email": "test@example.com"},
    }


async def mock_calculate(data):
    return {"score": 50, "tier": "B"}

dummy_db = {}
 main

 main
app.include_router(scorelab_router)
app.include_router(mirror_router)
app.include_router(sigil_router)
app.include_router(compliance_router)

sys.path.append(str(Path(__file__).resolve().parents[1]))

 main

@pytest.mark.asyncio
async def test_full_analysis_flow(monkeypatch):
    """Simulate analysis to NFT minting with patched services."""

 codex/fix-174-workflow-errors
    # Step 1: patch ScoreLab dependencies

    assert hasattr(compliance, "evaluate")
    assert hasattr(sigilmesh, "mint_reputation_nft")

 main
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
 codex/fix-174-workflow-errors
    monkeypatch.setattr(
        "app.services.sherlock.analyze_wallet",
        mock_analyze_wallet,
    )

    monkeypatch.setattr("app.services.sherlock.analyze_wallet", mock_analyze_wallet)
 main
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
 codex/fix-174-workflow-errors
    assert resp.status_code == 200
    analysis = resp.json()
    assert analysis["wallet"] == "0xabc"

    # Step 2: Mirror Engine comparison

    assert analysis_resp.status_code == 200
    analysis = analysis_resp.json()
    assert analysis["wallet"] == "0xabc"

 main
    def mock_compare(current):
        return {"delta": 0, **current}

    mirror_engine = types.SimpleNamespace(compare=mock_compare)

    def mock_check(result):
        return result["score"] >= 50

 codex/fix-174-workflow-errors
    compliance = types.SimpleNamespace(check=mock_check)

    mock_compliance = types.SimpleNamespace(check=mock_check)
 main

    def mock_mint(data):
        return {"token_id": "1", "wallet": data["wallet"]}

 codex/fix-174-workflow-errors
    sigilmesh = types.SimpleNamespace(mint_reputation_nft=mock_mint)

    mock_sigilmesh = types.SimpleNamespace(mint_reputation_nft=mock_mint)
 main

    compared = mirror_engine.compare(analysis)
    assert compared["delta"] == 0
 codex/fix-174-workflow-errors
    assert compliance.check(compared)
    nft = sigilmesh.mint_reputation_nft(compared)

    assert mock_compliance.check(compared)
    nft = mock_sigilmesh.mint_reputation_nft(compared)
 main
    assert nft["wallet"] == "0xabc"