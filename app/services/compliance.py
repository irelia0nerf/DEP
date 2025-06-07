from typing import Dict


async def check_compliance(data: Dict) -> Dict:
    """Perform a simplified compliance evaluation."""
    return {"wallet": data.get("wallet"), "compliant": data.get("tier") != "RISK"}
