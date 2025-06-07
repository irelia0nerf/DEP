import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from main import app  # noqa: E402


def test_openapi_contains_router_metadata():
    schema = app.openapi()
    score_op = schema["paths"]["/score/"]["post"]
    assert "Calculate a wallet risk score" in score_op["description"]
    assert score_op["tags"] == ["Score"]
    example = score_op["responses"]["200"]["content"]["application/json"]["example"]
    assert example["tier"] == "B"

    analyze_op = schema["paths"]["/internal/v1/scorelab/analyze"]["post"]
    assert "Analyze a wallet with ScoreLab" in analyze_op["description"]
    assert analyze_op["tags"] == ["ScoreLab"]
