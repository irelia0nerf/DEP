"""Bayesian scoring utilities shared across services."""

from typing import List

from src.models import WalletData


def bayes_px(p_e_given_x: float, p_x: float, p_e: float) -> float:
    """Return probability of event X given evidence E using Bayes' theorem."""
    if p_e <= 0:
        return 0.0
    px = (p_e_given_x * p_x) / p_e
    return max(0.0, min(px, 1.0))


def compute_probabilities(data: WalletData) -> tuple[float, float, float]:
    """Derive probabilities from wallet data using simple heuristics."""
    p_x = 0.4 if data.tx_volume > 1000 else 0.3
    p_e_given_x = 0.8 if data.age_days > 180 else 0.5
    p_e = 0.6 if data.tx_volume > 500 and data.age_days > 90 else 0.2
    return p_e_given_x, p_x, p_e


def calculate_score(data: WalletData) -> dict:
    """Calculate a score for the wallet based on Bayesian inference."""
    p_e_given_x, p_x, p_e = compute_probabilities(data)
    probability = bayes_px(p_e_given_x, p_x, p_e)
    score = int(probability * 1000)
    if score >= 800:
        tier = "AAA"
    elif score >= 500:
        tier = "BB"
    else:
        tier = "RISK"
    flags: List[str] = []
    if probability < 0.5:
        flags.append("low_probability")
    if data.tx_volume < 100:
        flags.append("low_activity")
    return {"score": score, "tier": tier, "probability": probability, "flags": flags}
