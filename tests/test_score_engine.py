from app.services.score_engine import calculate


def test_calculate_score_tier_aaa_at_threshold():
    flags = ["MIXER_USAGE", "HIGH_BALANCE", "HIGH_BALANCE", "HIGH_BALANCE"]
    score, tier, confidence = calculate(flags)
    assert score == 80
    assert tier == "AAA"
    assert confidence == 0.95


def test_calculate_score_tier_bb_at_threshold():
    flags = ["MIXER_USAGE"]
    score, tier, _ = calculate(flags)
    assert score == 50
    assert tier == "BB"


def test_calculate_unknown_flag_fallback():
    score, tier, _ = calculate(["UNKNOWN_FLAG"])
    assert score == 1
    assert tier == "RISK"
    score, tier, _ = calculate(["HIGH_BALANCE", "UNKNOWN_FLAG"])
    assert score == 11
    assert tier == "RISK"