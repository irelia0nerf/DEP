import sys
from pathlib import Path
import pytest
import httpx
from httpx import AsyncClient

sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402
from app.routers.scorelab import router as scorelab_router  # noqa: E402
from app.routers.mirror_engine import router as mirror_router  # noqa: E402
from app.routers.sigilmesh import router as sigil_router  # noqa: E402
from app.routers.compliance import router as compliance_router  # noqa: E402

app.include_router(scorelab_router)
app.include_router(mirror_router)
app.include_router(sigil_router)
app.include_router(compliance_router)


@pytest.mark.asyncio
async def test_analysis_to_nft(monkeypatch):
    async def mock_analyze(wallet_address: str):
        return {
            "wallet": wallet_address,
            "flags": ["MOCK_FLAG"],
            "score": 90,
            "tier": "AAA",
            "confidence": 0.99,
            "timestamp": "2025-01-01T00:00:00Z",
        }

    async def mock_snapshot_analysis(data):
        return {**data, "snapshot_id": "snap1"}

    async def mock_mint_snapshot(snapshot):
        return {
            "nft_id": "nft1",
            "snapshot_id": snapshot["snapshot_id"],
            "wallet": snapshot["wallet"],
        }

    async def mock_check_compliance(data):
        return {"wallet": data["wallet"], "compliant": True}

    monkeypatch.setattr(
        "app.services.scorelab_service.analyze",
        mock_analyze,
    )
    monkeypatch.setattr(
        "app.services.mirror_engine.snapshot_analysis",
        mock_snapshot_analysis,
    )
    monkeypatch.setattr(
        "app.services.sigilmesh.mint_snapshot",
        mock_mint_snapshot,
    )
    monkeypatch.setattr(
        "app.services.compliance.check_compliance",
        mock_check_compliance,
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
        analysis_resp = await ac.post(
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

        snapshot_resp = await ac.post(
            "/internal/v1/mirror/snapshot",
            json=analysis_data,
        )
        assert snapshot_resp.status_code == 200
        snapshot_data = snapshot_resp.json()
        assert snapshot_data["snapshot_id"] == "snap1"

    # Execute mocked pipeline
    compared = mirror_engine.compare(analysis)
    assert compared["delta"] == 0
    assert compliance.check(compared)
    nft = sigilmesh.mint_reputation_nft(compared)
    assert nft["wallet"] == "0x" + "a" * 40
