import os
import sys

import httpx
from httpx import AsyncClient
import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from main import app  # noqa: E402
from app.routers.dfc import router as dfc_router  # noqa: E402

app.include_router(dfc_router)


@pytest.mark.asyncio
async def test_propose_flag_change():
    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/internal/v1/dfc/proposals",
            json={"flag": "X", "weight": 10, "user_id": "tester"},
        )
    assert response.status_code == 200
    data = response.json()
    assert data["flag"] == "X"
