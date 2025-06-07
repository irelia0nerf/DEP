import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import pytest  # noqa: E402
from app.services import sigilmesh  # noqa: E402


@pytest.mark.asyncio
async def test_mint_reputation_nft():
    nft = await sigilmesh.mint_reputation_nft({"score": 900})
    assert "token_id" in nft
    assert nft["ipfs_uri"].startswith("ipfs://")
