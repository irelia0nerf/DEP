import asyncio
import httpx
import pytest
from httpx import AsyncClient

from main import app
from app.routers.sentinela import router as sentinela_router
from infra import event_bus

app.include_router(sentinela_router)


@pytest.mark.asyncio
async def test_monitor_reanalyzes_on_event(monkeypatch):
    analyzed = []

    async def mock_analyze(wallet_address: str):
        analyzed.append(wallet_address)
        return {"wallet": wallet_address}

    monkeypatch.setattr("app.services.scorelab_service.analyze", mock_analyze)

    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post("/internal/v1/sentinela/start")
        assert resp.status_code == 200
        await event_bus.publish_event("wallet.activity", {"wallet_address": "0xabc"})
        await asyncio.sleep(0.05)
        resp = await ac.post("/internal/v1/sentinela/stop")
        assert resp.status_code == 200

    assert analyzed[-1] == "0xabc"
