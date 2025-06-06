from app.services import score_engine


def test_load_weights_env(monkeypatch):
    monkeypatch.setenv("SCORE_WEIGHTS", '{"A": 1, "B": 2}')
    weights = score_engine.load_weights()
    assert weights == {"A": 1, "B": 2}


def test_load_weights_default(monkeypatch):
    monkeypatch.delenv("SCORE_WEIGHTS", raising=False)
    weights = score_engine.load_weights()
    assert "HIGH_BALANCE" in weights
