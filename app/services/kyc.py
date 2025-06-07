

"""KYC service module."""

from typing import Any, Dict, Optional

from cryptography.fernet import Fernet


async def get_identity(
    wallet_address: str, *, fernet: Optional[Fernet] = None
) -> Dict[str, Any]:
    """Return simulated KYC information for a wallet.

    A deterministic heuristic based on the last hexadecimal digit is used to
    assign a verification flag and KYC level. Even digits mean the wallet is
    verified while the digit modulo ``3`` defines the level (1-3). If the
    wallet is not verified, the level is ``0``.

    The function also returns a mock email derived from the wallet. When a
    :class:`~cryptography.fernet.Fernet` instance is provided via ``fernet`` the
    email is encrypted, simulating secure PII storage.

    Parameters
    ----------
    wallet_address:
        Wallet address in hexadecimal format.

    Returns
    -------
    Dict[str, Any]
        Example::

            {
                "wallet": "0xabc",
                "verified": True,
                "kyc_level": 2,
                "pii": {"email": "user0xabc@example.com"}
            }
    """

    if not wallet_address:
        return {
            "wallet": wallet_address,
            "verified": False,
            "kyc_level": 0,
            "pii": None,
        }

    last = wallet_address[-1]
    try:
        val = int(last, 16)
    except ValueError:  # pragma: no cover - invalid hex should rarely happen
        val = 0

    verified = val % 2 == 0
    kyc_level = (val % 3) + 1 if verified else 0
    email = f"user{wallet_address[-4:]}@example.com"
    if fernet is not None:
        email = fernet.encrypt(email.encode()).decode()

    return {
        "wallet": wallet_address,
        "verified": verified,
        "kyc_level": kyc_level,
        "pii": {"email": email},
    }
