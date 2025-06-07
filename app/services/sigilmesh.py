from uuid import uuid4
from typing import Dict


async def mint_snapshot(snapshot: Dict) -> Dict:
    """Mint a reputation NFT from a snapshot."""
    nft_id = f"nft-{uuid4().hex[:8]}"
    return {
        "nft_id": nft_id,
        "snapshot_id": snapshot.get("snapshot_id"),
        "wallet": snapshot.get("wallet"),
    }
