from typing import List
from app.services import sherlock, kyc, score_engine, mirror_engine
from app.utils.db import get_db


def aggregate_flags(onchain_flags: List[str], identity: dict) -> List[str]:
    """Combine on-chain flags with identity information."""

    flags = list(set(onchain_flags))
    if identity.get("verified"):
        flags.append("KYC_VERIFIED")
    return flags


async def analyze(wallet_address: str) -> dict:
    """Analyze a wallet and store the result in MongoDB."""

    onchain_flags = await sherlock.analyze_wallet(wallet_address)
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
    await mirror_engine.snapshot_event(result)
    return result
