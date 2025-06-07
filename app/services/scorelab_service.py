from src.scorelab_core import aggregate_flags, analyze as core_analyze

__all__ = ["aggregate_flags", "analyze"]


async def analyze(wallet_address: str) -> dict:
    """Proxy to scorelab_core.analyze."""
    return await core_analyze(wallet_address)

    db = get_db()
    await db.analysis.insert_one(result)
    return result


async def get_analysis(wallet_address: str) -> dict | None:
    """Retrieve the latest analysis for a wallet from MongoDB."""

    db = get_db()
    doc = await db.analysis.find_one({"wallet": wallet_address}, {"_id": 0})
    return doc
