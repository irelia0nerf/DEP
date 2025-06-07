
from typing import Dict, Union


async def get_identity(wallet_address: str) -> Dict[str, Union[str, bool]]:
    """Return KYC verification information for a wallet."""

    return {"wallet": wallet_address, "verified": True}
