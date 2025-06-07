import sys
from pathlib import Path
import httpx
from httpx import AsyncClient
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402


@pytest.mark.asyncio
async def test_proposal_flow():
    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/internal/v1/dfc/proposals",
            json={"flag": "MIXER_USAGE", "description": "mixers", "user_id": "u1"},
        )
    assert response.status_code == 200
    data = response.json()
    assert data["proposal_id"]
    assert data["status"] in {"PENDING", "APPROVED_FOR_STAGING"}
