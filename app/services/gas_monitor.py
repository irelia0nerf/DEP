from typing import Any, Dict, List


def analyze_gas_usage(gas_prices: List[int]) -> Dict[str, Any]:
    """Analyze gas price history and return anomaly flags."""

    if not gas_prices:
        return {"average": 0.0, "flags": []}

    average = sum(gas_prices) / len(gas_prices)
    flags: List[str] = []
    if max(gas_prices) > average * 2:
        flags.append("GAS_SPIKE")
    if all(price < 20 for price in gas_prices):
        flags.append("LOW_GAS_USAGE")
    return {"average": average, "flags": flags}
