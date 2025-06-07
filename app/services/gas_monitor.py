from __future__ import annotations

from typing import List, Tuple


HIGH_GAS_THRESHOLD = 300_000


def detect_gas_patterns(
    gas_used: List[int], high_threshold: int = HIGH_GAS_THRESHOLD
) -> Tuple[List[str], float]:
    """Analyze gas usage values and flag abnormalities.

    Parameters
    ----------
    gas_used:
        List of gas amounts consumed per transaction.
    high_threshold:
        Baseline considered high for a single transaction.

    Returns
    -------
    Tuple[List[str], float]
        Sorted list of flags and the average gas used.
    """
    if not gas_used:
        return [], 0.0

    avg = sum(gas_used) / len(gas_used)
    flags: List[str] = []
    if avg > high_threshold:
        flags.append("HIGH_AVG_GAS")

    if max(gas_used) - min(gas_used) > high_threshold:
        flags.append("GAS_SPIKE")

    if any(g > high_threshold * 1.5 for g in gas_used):
        flags.append("EXTREME_GAS_USAGE")

    return sorted(set(flags)), avg


async def analyze_wallet(wallet_address: str) -> List[str]:
    """Simulate gas analysis for a wallet address."""
    seed = int(wallet_address[-2:], 16)
    gas_values = [21_000 + seed * 10 for _ in range(3)]
    if seed % 5 == 0:
        gas_values.append(450_000)
    flags, _ = detect_gas_patterns(gas_values)
    return flags
