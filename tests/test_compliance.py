import sys
from pathlib import Path
import pytest
import httpx
from httpx import AsyncClient

sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402
from app.routers.compliance import router as compliance_router  # noqa: E402

app.include_router(compliance_router)


class FakeCursor:
    def __init__(self, data):
        self.data = data

    def sort(self, *args, **kwargs):
        return self

    def limit(self, _):
        return self

    async def to_list(self, length):
        return self.data[:length]


class FakeCollection:
    def __init__(self):
        self.data = []

    async def insert_one(self, doc):
        self.data.append(doc)

    def find(self):
        return FakeCursor(self.data)


class FakeDB:
    def __init__(self):
        self.compliance_logs = FakeCollection()


def setup_fakes(monkeypatch):
    fake_db = FakeDB()
    monkeypatch.setattr("app.services.compliance.get_db", lambda: fake_db)
    return fake_db


@pytest.mark.asyncio
async def test_compliance_evaluation(monkeypatch):
    async def mock_analyze(wallet_address: str):
        return {
            "wallet": wallet_address,
            "flags": ["KYC_VERIFIED", "HIGH_BALANCE"],
            "score": 90,
            "tier": "AAA",
            "confidence": 0.99,
            "timestamp": "2025-01-01T00:00:00Z",
        }

    monkeypatch.setattr("app.services.scorelab_service.analyze", mock_analyze)
    setup_fakes(monkeypatch)

    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/internal/v1/compliance/evaluate",
            json={
                "wallet_address": "0xabc",
                "rules": ["kyc_verified", "no_mixer", "tier_bb_or_higher"],
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["passed"] is True
        assert all(data["results"].values())

        response = await ac.get("/internal/v1/compliance/logs")
        assert response.status_code == 200
        logs = response.json()
        assert len(logs) == 1
        assert logs[0]["wallet"] == "0xabc"
