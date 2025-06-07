import sys
from pathlib import Path
import httpx
from httpx import AsyncClient
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402


@pytest.mark.asyncio
async def test_event_reanalysis():
    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/internal/v1/sentinela/event",
            json={"wallet": "0x1", "gas_used": 300, "context": "tx"},
        )
    assert response.status_code == 200
    assert response.json()["reanalyze"] is True
