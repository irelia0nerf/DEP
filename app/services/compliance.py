"""Compliance Orchestrator logic."""

from __future__ import annotations

from typing import Dict

from app.services import kyc


async def check_compliance(wallet_address: str) -> Dict:
    """Perform basic compliance checks using KYC information."""

    identity = await kyc.get_identity(wallet_address)
    issues = []
    if not identity.get("verified"):
        issues.append("KYC_MISSING")
    passes = not issues
    return {"wallet": wallet_address, "passes": passes, "issues": issues}
