"""Mint reputation NFTs."""

from __future__ import annotations

import uuid
from typing import Dict


async def mint_reputation_nft(data: Dict) -> Dict:
    """Simulate minting a reputation NFT and return metadata."""

    token_id = str(uuid.uuid4())
    ipfs_url = f"ipfs://{token_id}"
    return {"token_id": token_id, "ipfs_url": ipfs_url}
