import sys
from pathlib import Path
import httpx
from httpx import AsyncClient
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402


@pytest.mark.asyncio
async def test_snapshot_diff():
    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        await ac.post(
            "/internal/v1/mirror/snapshot",
            json={"wallet": "0x1", "score": 50, "flags": ["A"]},
        )
        response = await ac.post(
            "/internal/v1/mirror/snapshot",
            json={"wallet": "0x1", "score": 60, "flags": ["A", "B"]},
        )
    assert response.status_code == 200
    data = response.json()
    assert data["delta_score"] == 10
    assert "B" in data["added_flags"]
