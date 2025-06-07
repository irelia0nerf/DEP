import sys
from pathlib import Path
import httpx
from httpx import AsyncClient
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402


@pytest.mark.asyncio
async def test_gas_analysis():
    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/internal/v1/gasmonitor/analyze",
            json={"gas_values": [100, 250, 300]},
        )
    assert response.status_code == 200
    data = response.json()
    assert "HIGH_AVG_GAS" in data["anomalies"]
