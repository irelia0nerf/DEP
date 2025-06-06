from typing import Dict, List, Tuple


def load_weights() -> Dict[str, int]:
    return {"HIGH_BALANCE": 10, "MIXER_USAGE": 50, "KYC_VERIFIED": -5}


def calculate(flags: List[str]) -> Tuple[int, str, float]:
    weights = load_weights()
    score = sum(weights.get(flag, 1) for flag in flags)
    if score >= 80:
        tier = "AAA"
    elif score >= 50:
        tier = "BB"
    else:
        tier = "RISK"
    confidence = 0.95
    return score, tier, confidence
