"""Analyze gas usage patterns."""

from __future__ import annotations

from typing import Dict, List


async def analyze_gas(gas_values: List[int]) -> Dict:
    """Return anomalies based on gas usage statistics."""

    if not gas_values:
        return {"anomalies": []}
    avg = sum(gas_values) / len(gas_values)
    anomalies: List[str] = []
    if avg > 150:
        anomalies.append("HIGH_AVG_GAS")
    if max(gas_values) - min(gas_values) > 200:
        anomalies.append("VOLATILE_GAS")
    return {"anomalies": anomalies}
