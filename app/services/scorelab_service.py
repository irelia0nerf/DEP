from src.scorelab_core import aggregate_flags, analyze as core_analyze
from app.utils.db import get_db

__all__ = ["aggregate_flags", "analyze", "get_analysis"]


async def analyze(wallet_address: str) -> dict:
    """Run a ScoreLab analysis and persist the result."""
    onchain_flags = await sherlock.analyze_wallet(wallet_address)
    identity = await kyc.get_identity(wallet_address)
    flags = aggregate_flags(onchain_flags, identity)
    score, tier, confidence = score_engine.calculate(flags)


async def get_analysis(wallet_address: str) -> dict | None:
    """Retrieve the latest analysis for a wallet."""
    db = get_db()
    return await db.analysis.find_one({"wallet": wallet_address}, {"_id": 0})
