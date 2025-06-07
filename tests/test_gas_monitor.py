from app.services import gas_monitor
import httpx
from httpx import AsyncClient
import pytest
from main import app


def test_detect_no_anomalies():
    assert gas_monitor.detect_anomalies([21000, 22000, 21000]) == []


def test_detect_high_avg():
    flags = gas_monitor.detect_anomalies([200000, 180000, 170000])
    assert "HIGH_GAS_AVG" in flags


def test_detect_gas_spike():
    flags = gas_monitor.detect_anomalies([21000, 22000, 600000])
    assert "GAS_SPIKE" in flags


@pytest.mark.asyncio
async def test_gas_monitor_endpoint():
    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/internal/v1/gasmonitor/check",
            json={"gas_used": [21000, 600000]},
        )
    assert response.status_code == 200
    assert "GAS_SPIKE" in response.json()["flags"]
