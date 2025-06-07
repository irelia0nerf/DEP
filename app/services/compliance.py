from __future__ import annotations

from datetime import datetime
from typing import Dict, List

from app.services import kyc, sherlock
from app.utils.db import get_db


async def evaluate(wallet_address: str) -> Dict[str, object]:
    """Evaluate KYC and KYT rules for a wallet and store the result."""
    identity = await kyc.get_identity(wallet_address)
    kyt_flags = await sherlock.analyze_wallet(wallet_address)
    status = "pass" if identity.get("verified") and not kyt_flags else "fail"

    record = {
        "wallet": wallet_address,
        "kyc_verified": bool(identity.get("verified")),
        "kyt_flags": kyt_flags,
        "status": status,
        "ts": datetime.utcnow(),
    }

    db = get_db()
    await db.compliance_logs.insert_one(record)

    record["ts"] = record["ts"].isoformat()
    return record


async def get_logs(limit: int = 10) -> List[Dict[str, object]]:
    """Return the most recent compliance evaluation logs."""
    db = get_db()
    cursor = (
        db.compliance_logs.find({}, {"_id": 0}).sort("ts", -1).limit(limit)
    )
    logs = await cursor.to_list(length=limit)
    for log in logs:
        ts = log.get("ts")
        if isinstance(ts, datetime):
            log["ts"] = ts.isoformat()
    return logs
