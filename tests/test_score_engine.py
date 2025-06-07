from app.services import score_engine


def test_high_score():
    flags = ["MIXER_USAGE", "MIXER_USAGE", "HIGH_BALANCE"]
    score, tier, confidence = score_engine.calculate(flags)
    assert score >= 80
    assert tier == "AAA"
    assert confidence == 0.95


def test_medium_score():
    flags = ["MIXER_USAGE", "HIGH_BALANCE"]
    score, tier, confidence = score_engine.calculate(flags)
    assert 50 <= score < 80
    assert tier == "BB"
    assert confidence == 0.95


def test_low_score():
    flags = ["KYC_VERIFIED", "UNKNOWN"]
    score, tier, confidence = score_engine.calculate(flags)
    assert score < 50
    assert tier == "RISK"
    assert confidence == 0.95
