import sys
from pathlib import Path
import httpx
import pytest
from httpx import AsyncClient

sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402


class FakeCursor:
    def __init__(self, docs):
        self.docs = docs

    def sort(self, *args, **kwargs):
        return self

    def limit(self, *_args, **_kwargs):
        return self

    async def to_list(self, length=None):
        return self.docs[:length]


class FakeCollection:
    def __init__(self):
        self.docs = []

    async def insert_one(self, doc):
        self.docs.append(doc)

    def find(self, *args, **kwargs):
        return FakeCursor(self.docs)


class FakeDB:
    def __init__(self):
        self.compliance_logs = FakeCollection()


@pytest.mark.asyncio
async def test_compliance_evaluate_and_logs(monkeypatch):
    async def mock_identity(addr):
        return {"wallet": addr, "verified": True}

    async def mock_analyze(addr):
        return []

    db = FakeDB()
    monkeypatch.setattr("app.services.kyc.get_identity", mock_identity)
    monkeypatch.setattr("app.services.sherlock.analyze_wallet", mock_analyze)
    monkeypatch.setattr("app.services.compliance.get_db", lambda: db)

    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post(
            "/internal/v1/compliance/evaluate",
            json={"wallet_address": "0xabc"},
        )
    assert resp.status_code == 200
    result = resp.json()
    assert result["status"] == "pass"
    assert result["kyc_verified"] is True
    assert result["kyt_flags"] == []

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        logs_resp = await ac.get("/internal/v1/compliance/logs?limit=1")
    assert logs_resp.status_code == 200
    logs = logs_resp.json()
    assert len(logs) == 1
    assert logs[0]["wallet"] == "0xabc"
