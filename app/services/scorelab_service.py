from typing import List
from app.services import sherlock, kyc, score_engine, mirror_engine
from app.utils.db import get_db


def aggregate_flags(
    onchain_flags: List[str], identity: dict, gas_flags: List[str]
) -> List[str]:
    """Combine flags from multiple sources."""

    flags = list(set(onchain_flags + gas_flags))
    if identity.get("verified"):
        flags.append("KYC_VERIFIED")
    return flags


async def analyze(wallet_address: str) -> dict:
    """Analyze a wallet and store the result in MongoDB."""

    onchain_flags = await sherlock.analyze_wallet(wallet_address)
    identity = await kyc.get_identity(wallet_address)
    gas_flags = await gas_monitor.analyze(wallet_address)
    flags = aggregate_flags(onchain_flags, identity, gas_flags)
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
    await mirror_engine.snapshot_event(result)
    return result


async def get_analysis(wallet_address: str) -> dict | None:
    """Retrieve the latest analysis for a wallet from MongoDB."""

    db = get_db()
    doc = await db.analysis.find_one({"wallet": wallet_address}, {"_id": 0})
    return doc
