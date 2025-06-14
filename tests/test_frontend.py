import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from fastapi.testclient import TestClient  # noqa: E402
from main import app  # noqa: E402


def test_ui_page() -> None:
    client = TestClient(app)
    response = client.get('/ui')
    assert response.status_code == 200
    assert '<form' in response.text
