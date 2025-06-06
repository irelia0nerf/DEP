"""Flag-based reputation scoring utilities."""

import json
import os
from typing import Dict, List, Tuple


def load_weights() -> Dict[str, int]:
    """Load scoring weights from the ``SCORE_WEIGHTS`` environment variable."""
    raw = os.getenv("SCORE_WEIGHTS")
    if raw:
        try:
            data = json.loads(raw)
            if isinstance(data, dict):
                return {str(k): int(v) for k, v in data.items()}
        except Exception:  # pragma: no cover - fallback
            pass
    return {"HIGH_BALANCE": 10, "MIXER_USAGE": 50, "KYC_VERIFIED": -5}


def calculate(flags: List[str]) -> Tuple[int, str, float]:
    """Return score, tier and confidence for a set of flags."""
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
