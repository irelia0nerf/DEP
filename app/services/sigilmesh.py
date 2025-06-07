from datetime import datetime
from typing import Any, Dict
from uuid import uuid4


async def mint_reputation_nft(analysis: Dict[str, Any]) -> Dict[str, Any]:
    """Mint a reputation NFT representing the analysis result."""

    token_id = uuid4().hex
    nft = {
        "token_id": token_id,
        "ipfs_uri": f"ipfs://{token_id}",
        "issued_at": datetime.utcnow(),
        "analysis": analysis,
    }
    return nft
