import pytest
from cryptography.fernet import Fernet

from app.services import kyc


@pytest.mark.asyncio
async def test_get_identity_verified_level():
    result = await kyc.get_identity("0x1234")
    assert result["wallet"] == "0x1234"
    assert result["verified"] is True
    assert 1 <= result["kyc_level"] <= 3
    assert result["pii"]["email"] == "user1234@example.com"


@pytest.mark.asyncio
async def test_get_identity_unverified_level_zero():
    result = await kyc.get_identity("0x1235")
    assert result["wallet"] == "0x1235"
    assert result["verified"] is False
    assert result["kyc_level"] == 0
    assert result["pii"]["email"] == "user1235@example.com"


@pytest.mark.asyncio
async def test_get_identity_encrypted_email():
    key = Fernet.generate_key()
    f = Fernet(key)
    result = await kyc.get_identity("0x1234", fernet=f)
    encrypted = result["pii"]["email"]
    assert encrypted != "user1234@example.com"
    assert f.decrypt(encrypted.encode()).decode() == "user1234@example.com"
