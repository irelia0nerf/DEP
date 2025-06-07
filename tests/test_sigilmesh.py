import sys
from pathlib import Path
import httpx
from httpx import AsyncClient
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402


@pytest.mark.asyncio
async def test_mint_sigil():
    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/internal/v1/sigilmesh/mint",
            json={"wallet": "0x1", "score": 80, "flags": ["A"]},
        )
    assert response.status_code == 200
    data = response.json()
    assert data["token_id"]
    assert data["ipfs_url"].startswith("ipfs://")
