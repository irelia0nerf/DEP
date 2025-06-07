import pytest

from app.services import sigilmesh


@pytest.mark.asyncio
async def test_mint_reputation_nft():
    nft = await sigilmesh.mint_reputation_nft({"score": 900})
    assert "token_id" in nft
    assert nft["ipfs_uri"].startswith("ipfs://")
