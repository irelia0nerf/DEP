"""KYC service module."""

from typing import Any, Dict, Optional

from cryptography.fernet import Fernet


async def get_identity(
    wallet_address: str,
    *,
    fernet: Optional[Fernet] = None,
) -> Dict[str, Any]:
    """Return simulated KYC information for a wallet."""
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

    even_digits = set("02468aceACE")
    is_verified = last in even_digits
    kyc_level = val % 3 + 1 if is_verified else 0
    local_part = (
        wallet_address[2:] if wallet_address.startswith("0x") else wallet_address
    )
    email = f"user{local_part}@example.com"
    if fernet:
        email = fernet.encrypt(email.encode()).decode()

    return {
        "wallet": wallet_address,
        "verified": is_verified,
        "kyc_level": kyc_level,
        "pii": {"email": email},
    }
