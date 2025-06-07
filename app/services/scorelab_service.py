from typing import List

from app.services import kyc, score_engine, sherlock, gas_monitor
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

    """Analyze a wallet and store the result in MongoDB.

    Parameters
    ----------
    wallet_address:
        Address of the wallet being analyzed.

    Returns
    -------
    dict
        A dictionary containing score and flag information.
    """
    onchain_flags = await sherlock.analyze_wallet(wallet_address)
    gas_flags = await gas_monitor.analyze_wallet(wallet_address)
    identity = await kyc.get_identity(wallet_address)
    flags = aggregate_flags(onchain_flags + gas_flags, identity)
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
    diff = await mirror_engine.compare_snapshot(wallet_address, result)
    await mirror_engine.save_snapshot(result)
    result["snapshot_diff"] = diff
    return result


async def get_analysis(wallet_address: str) -> dict | None:
    """Retrieve the latest analysis for a wallet from MongoDB."""

    db = get_db()
    doc = await db.analysis.find_one({"wallet": wallet_address}, {"_id": 0})
    return doc
