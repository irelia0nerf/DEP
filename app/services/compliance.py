from datetime import datetime
from typing import Dict, List

from app.services import scorelab_service
from app.utils.db import get_db


async def evaluate_rules(wallet_address: str, rules: List[str]) -> dict:
    """Evaluate compliance rules for a wallet and log the result."""
    analysis = await scorelab_service.analyze(wallet_address)
    flags = analysis.get("flags", [])
    tier = analysis.get("tier", "RISK")

    results: Dict[str, bool] = {}
    for rule in rules:
        if rule == "kyc_verified":
            results[rule] = "KYC_VERIFIED" in flags
        elif rule == "no_mixer":
            results[rule] = "MIXER_USAGE" not in flags
        elif rule == "tier_bb_or_higher":
            results[rule] = tier in ("AAA", "BB")
        else:
            results[rule] = False

    passed = all(results.values())
    record = {
        "wallet": wallet_address,
        "rules": rules,
        "results": results,
        "passed": passed,
        "flags": flags,
        "tier": tier,
        "timestamp": datetime.utcnow(),
    }

    db = get_db()
    await db.compliance_logs.insert_one(record)
    return record


async def get_logs(limit: int = 20) -> List[dict]:
    """Return recent compliance logs."""
    db = get_db()
    cursor = db.compliance_logs.find().sort("timestamp", -1).limit(limit)
    logs = await cursor.to_list(length=limit)
    return logs
