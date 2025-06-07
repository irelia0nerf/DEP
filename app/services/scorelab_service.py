"""High level service that orchestrates wallet reputation analysis."""

from datetime import datetime
from typing import List

from app.services import kyc, score_engine, sherlock
from app.utils.db import get_db


def aggregate_flags(onchain_flags: List[str], identity: dict) -> List[str]:


    flags = sorted(set(onchain_flags))

    if identity.get("verified"):
        flags.add("KYC_VERIFIED")
    return sorted(flags)


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
    identity = await kyc.get_identity(wallet_address)
    flags = aggregate_flags(onchain_flags, identity)
    score, tier, confidence = score_engine.calculate(flags)

    result = {
        "wallet": wallet_address,
        "flags": flags,
        "score": score,
        "tier": tier,
        "confidence": confidence,
        "timestamp": datetime.utcnow(),
    }

    db = get_db()
    await db.analysis.insert_one(result)
    return result
