from typing import List
from app.services import (
    sherlock,
    kyc,
    score_engine,
    mirror_engine,
    gas_monitor,
)
from app.utils.db import get_db


def aggregate_flags(
    onchain_flags: List[str], identity: dict, gas_flags: List[str] | None = None
) -> List[str]:
    """Combine flags from multiple sources."""

    flags = set(onchain_flags)
    if gas_flags:
        flags.update(gas_flags)
    ordered = sorted(flags)
    if identity.get("verified"):
        ordered.append("KYC_VERIFIED")
    return ordered


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
