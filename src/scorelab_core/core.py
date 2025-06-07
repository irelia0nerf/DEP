"""Core analysis logic used by ScoreLab services."""

from app.services import kyc, score_engine, sherlock
from src.utils.db import get_db

 codex/update-tests-and-fix-imports
# expose analyze_wallet for testing
analyze_wallet = sherlock.analyze_wallet


def aggregate_flags(onchain_flags: List[str], identity: dict) -> List[str]:
    """Return a unique, sorted list of flags, adding KYC flag when verified."""

analyze_wallet = sherlock.analyze_wallet


def aggregate_flags(onchain_flags: list[str], identity: dict) -> list[str]:
    """Return a unique, sorted list of flags, adding a KYC flag when verified."""
 main
    flags = sorted(set(onchain_flags))
    if identity.get("verified"):
        flags.append("KYC_VERIFIED")
    return flags


async def analyze(wallet_address: str) -> dict:
    """Analyze a wallet and store the result in MongoDB."""
    onchain_flags = await analyze_wallet(wallet_address)
    identity = await kyc.get_identity(wallet_address)
    flags = aggregate_flags(onchain_flags, identity)
    score, tier, confidence = score_engine.calculate(flags)

    result = {
        "wallet": wallet_address,
        "flags": flags,
        "score": score,
        "tier": tier,
        "confidence": confidence,
    }

    db = get_db()
    await db.analysis.insert_one(result)
    return result
