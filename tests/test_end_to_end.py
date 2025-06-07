 codex/implement-kyc-logic-and-adjust-tests

import sys
from pathlib import Path
 codex/preencher-src/utils/db.py-com-lógica-de-app/utils/db.py
import types

 main
import types

 main
import pytest
import httpx
from fastapi import FastAPI
from httpx import AsyncClient
import types

 codex/implement-kyc-logic-and-adjust-tests
# Create a minimal app for testing
from app.routers import scorelab  # noqa: E402

app = FastAPI()
app.include_router(scorelab.router)

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

app.include_router(scorelab_router)
app.include_router(mirror_router)
app.include_router(sigil_router)
app.include_router(compliance_router)

 main
 main


@pytest.mark.asyncio
async def test_full_analysis_flow(monkeypatch):
    """Simulate analysis to NFT minting with patched services."""
 codex/implement-kyc-logic-and-adjust-tests

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



    wallet = "0x" + "a" * 40

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

 main
    class DummyDB:
        def __init__(self):
            self.analysis = DummyColl()

    dummy_db = DummyDB()
    monkeypatch.setattr(
 codex/implement-kyc-logic-and-adjust-tests
        "app.services.sherlock.analyze_wallet",

        "src.sherlock.analyzer.analyze_wallet",
        mock_analyze,
    )
    monkeypatch.setattr(
        "app.services.sherlock.analyze_wallet",
        mock_analyze_wallet,
    )
    monkeypatch.setattr(
        "src.scorelab_core.core.analyze_wallet",
 codex/preencher-src/utils/db.py-com-lógica-de-app/utils/db.py
        mock_analyze,

 main
        mock_analyze_wallet,
 main
    )
    monkeypatch.setattr("app.services.kyc.get_identity", mock_get_identity)
    monkeypatch.setattr("app.services.score_engine.calculate", mock_calculate)
    monkeypatch.setattr("app.utils.db.get_db", lambda: dummy_db)
    monkeypatch.setattr("app.services.scorelab_service.get_db", lambda: dummy_db)

    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post(
            "/internal/v1/scorelab/analyze",
 codex/implement-kyc-logic-and-adjust-tests
            json={"wallet_address": "0xabc"},
        )
 codex/preencher-src/utils/db.py-com-lógica-de-app/utils/db.py

 codex/implement-kyc-logic-and-adjust-tests
    assert resp.status_code == 200
    analysis = resp.json()
    assert analysis["wallet"] == "0xabc"


            json={"wallet_address": wallet},
        )
 codex/remover-duplicação-e-definir-o-modelo-event
    assert resp.status_code == 200
    analysis = resp.json()
    assert analysis["wallet"] == wallet

 main
 main
    assert analysis_resp.status_code == 200
    analysis = analysis_resp.json()
    assert analysis["wallet"] == "0x" + "a" * 40
 main

    # Step 2: Mirror Engine comparison
    def mock_compare(current):
        return {"delta": 0, **current}

    mirror_engine = types.SimpleNamespace(compare=mock_compare)

    # Step 3: Compliance check
    def mock_check(result):
        return result["score"] >= 50

 codex/preencher-src/utils/db.py-com-lógica-de-app/utils/db.py
        snapshot_resp = await ac.post(
            "/internal/v1/mirror/snapshot",
            json=analysis,
        )
        assert snapshot_resp.status_code == 200
        snapshot_data = snapshot_resp.json()
        assert snapshot_data["snapshot_id"] == "snap1"

    compliance = types.SimpleNamespace(check=mock_check)

    # Step 4: SigilMesh minting
    def mock_mint(data):
        return {"token_id": "1", "wallet": data["wallet"]}

    sigilmesh = types.SimpleNamespace(mint_reputation_nft=mock_mint)
 main

    # Execute mocked pipeline
    compared = mirror_engine.compare(analysis)
    assert compared["delta"] == 0
    assert compliance.check(compared)
    nft = sigilmesh.mint_reputation_nft(compared)
 codex/implement-kyc-logic-and-adjust-tests
    assert nft["wallet"] == "0xabc"

    assert nft["wallet"] == wallet
 main