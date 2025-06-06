
from typing import Dict


async def get_identity(wallet_address: str) -> Dict[str, bool]:
    return {"wallet": wallet_address, "verified": True}
