

"""KYC service module."""

from typing import Dict


async def get_identity(wallet_address: str) -> Dict[str, bool]:
    """Return KYC verification information for a wallet.

    A very small heuristic is applied: if the wallet address ends with an even
    hexadecimal digit, it is considered verified. This simulates the behaviour
    of a third-party KYC provider without exposing any secrets or real
    integration.

    Parameters
    ----------
    wallet_address:
        Wallet address in hexadecimal format.

    Returns
    -------
    Dict[str, bool]
        Example::

            {"wallet": "0xabc", "verified": False}
    """

    if not wallet_address:
        return {"wallet": wallet_address, "verified": False}

    even_digits = set("02468aceACE")
    is_verified = wallet_address[-1] in even_digits
    return {"wallet": wallet_address, "verified": is_verified}
