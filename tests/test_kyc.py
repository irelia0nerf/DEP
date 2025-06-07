import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import pytest  # noqa: E402
from app.services import kyc  # noqa: E402


@pytest.mark.asyncio
async def test_get_identity_verified():
    result = await kyc.get_identity("0x1234")
    assert result["verified"] is True


@pytest.mark.asyncio
async def test_get_identity_unverified():
    result = await kyc.get_identity("0x1235")
    assert result["verified"] is False
