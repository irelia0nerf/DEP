from datetime import datetime
from typing import Any, Dict, Optional
from uuid import uuid4

 codex/update-tests-and-fix-imports
from . import scorelab_service

from app.services import scorelab_service
 main


async def mint_reputation_nft(analysis: Dict[str, Any]) -> Dict[str, Any]:
    """Mint a reputation NFT representing the analysis result."""
    token_id = uuid4().hex
    return {
        "token_id": token_id,
        "ipfs_uri": f"ipfs://{token_id}",
        "issued_at": datetime.utcnow(),
        "metadata": analysis,
    }


 codex/update-tests-and-fix-imports
async def get_latest_analysis(wallet_address: str) -> Optional[Dict[str, Any]]:

async def get_latest_analysis(wallet_address: str) -> Dict[str, Any] | None:
 main
    """Retrieve the most recent analysis for a wallet."""
    return await scorelab_service.get_analysis(wallet_address)
