import pytest

from src.scorelab_core import aggregate_flags, analyze


def test_aggregate_flags():
    result = aggregate_flags(["A", "A"], {"verified": True})
    assert "KYC_VERIFIED" in result
    assert len(result) == 2


@pytest.mark.asyncio
async def test_analyze(monkeypatch):
    async def mock_analyze_wallet(addr: str):
        return ["FLAG1"]

    async def mock_get_identity(addr: str):
        return {"verified": True}

    def mock_calculate(flags):
        return 100, "AAA", 0.9

    class DummyCollection:
        def __init__(self):
            self.saved = None

        async def insert_one(self, data):
            self.saved = data

    class DummyDB:
        def __init__(self):
            self.analysis = DummyCollection()

    monkeypatch.setattr("src.scorelab_core.core.analyze_wallet", mock_analyze_wallet)
    monkeypatch.setattr("src.scorelab_core.core.kyc.get_identity", mock_get_identity)
    monkeypatch.setattr("src.scorelab_core.core.score_engine.calculate", mock_calculate)
    dummy_db = DummyDB()
    monkeypatch.setattr("src.scorelab_core.core.get_db", lambda: dummy_db)

    result = await analyze("0xabc")
    assert result["wallet"] == "0xabc"
    assert dummy_db.analysis.saved == result
