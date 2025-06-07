from typing import List


def detect_anomalies(gas_values: List[int]) -> List[str]:
    """Return gas usage anomaly flags from a list of gas values."""
    flags: List[str] = []
    if not gas_values:
        return flags

    avg = sum(gas_values) / len(gas_values)
    if avg > 150_000:
        flags.append("HIGH_GAS_AVG")

    for value in gas_values:
        if value > 200_000 and value > avg * 1.5:
            flags.append("GAS_SPIKE")
            break

    return flags


async def analyze(wallet_address: str) -> List[str]:
    """Simulate gas analysis for a wallet."""
    sample_usage = [21_000, 22_000, 300_000]
    return detect_anomalies(sample_usage)
