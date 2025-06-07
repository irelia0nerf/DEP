
from src.scorelab_core import aggregate_flags, analyze as core_analyze

__all__ = ["aggregate_flags", "analyze"]


async def analyze(wallet_address: str) -> dict:
    """Proxy to scorelab_core.analyze."""
    return await core_analyze(wallet_address)
