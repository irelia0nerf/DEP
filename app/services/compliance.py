from typing import Any, Dict, List


def evaluate(
    wallet_address: str, kyc_info: Dict[str, Any], flags: List[str]
) -> Dict[str, Any]:
    """Compute a simple compliance score based on KYC and flags."""

    score = 100
    if not kyc_info.get("verified"):
        score -= 40
    score -= len(flags) * 10
    if score >= 95:
        status = "PASS"
    elif score >= 60:
        status = "REVIEW"
    else:
        status = "FAIL"
    return {
        "wallet": wallet_address,
        "compliance_score": score,
        "status": status,
    }
