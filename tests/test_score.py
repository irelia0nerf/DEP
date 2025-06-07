import asyncio
from fastapi.testclient import TestClient

from main import app
from app.models.schemas import WalletData
from app.services import engine


def test_score_endpoint():
    data = {"wallet_address": "0xabc", "tx_volume": 1200, "age_days": 365}
    expected = asyncio.run(engine.calculate_score(WalletData(**data)))

    with TestClient(app) as client:
        response = client.post("/score/", json=data)

    assert response.status_code == 200
    assert response.json() == expected
