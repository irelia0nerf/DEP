import httpx
import pytest
from httpx import AsyncClient

from main import app
from app.routers.scorelab import router as scorelab_router
from app.routers.sigilmesh import router as sigil_router
from app.services import sherlock, kyc, score_engine

app.include_router(scorelab_router)
app.include_router(sigil_router)


@pytest.mark.asyncio
async def test_full_analysis_flow(monkeypatch):
    async def mock_analyze_wallet(addr: str):
        return ["MOCK_FLAG"]

    async def mock_get_identity(addr: str):
        return {"verified": True}

    def mock_calculate(flags):
        return 80, "AAA", 0.95

    class DummyColl:
        def __init__(self):
            self.saved = None

        async def insert_one(self, data):
            self.saved = data

        async def find_one(self, query, projection=None):
            return self.saved

    class DummyDB:
        def __init__(self):
            self.analysis = DummyColl()

    dummy_db = DummyDB()
    monkeypatch.setattr(sherlock, "analyze_wallet", mock_analyze_wallet)
    monkeypatch.setattr(kyc, "get_identity", mock_get_identity)
    monkeypatch.setattr(score_engine, "calculate", mock_calculate)
    monkeypatch.setattr("app.services.scorelab_service.get_db", lambda: dummy_db)
    monkeypatch.setattr("app.utils.db.get_db", lambda: dummy_db)

    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        analysis_resp = await ac.post(
            "/internal/v1/scorelab/analyze",
            json={"wallet_address": "0xabc"},
        )
        assert analysis_resp.status_code == 200
        mint_resp = await ac.post(
            "/internal/v1/sigilmesh/mint",
            json={"wallet_address": "0xabc"},
        )
        assert mint_resp.status_code == 200
        assert "token_id" in mint_resp.json()
