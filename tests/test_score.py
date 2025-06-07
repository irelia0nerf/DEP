import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from fastapi.testclient import TestClient  # noqa: E402
from app.models.schemas import WalletData  # noqa: E402
from app.services import engine  # noqa: E402
import asyncio  # noqa: E402


def test_score_endpoint():
    from main import app  # noqa: E402

    data = {"wallet_address": "0xabc", "tx_volume": 1200, "age_days": 365}
    expected = asyncio.run(engine.calculate_score(WalletData(**data)))

    with TestClient(app) as client:
        response = client.post("/score/", json=data)

    assert response.status_code == 200
    assert response.json() == expected

