from typing import Any, Dict


def calculate_px(
    event_flags: Dict[str, Any],
    weights: Dict[str, float],
) -> float:
    """Calculate dynamic probability Px based on event flags and weights.

    Args:
        event_flags: Mapping of flag names to values (bool or str).
        weights: Mapping of flag names to weight adjustments.

    Returns:
        Probability value between 0 and 1.
    """
    px = 0.5  # Neutral starting probability
    for flag, value in event_flags.items():
        weight = weights.get(flag, 0.0)
        if isinstance(value, bool):
            px += weight if value else -weight
        elif isinstance(value, str):
            if value.lower() == "high":
                px += weight
            elif value.lower() == "low":
                px -= weight
    return max(0.0, min(px, 1.0))
