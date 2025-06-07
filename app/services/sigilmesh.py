from datetime import datetime
from typing import Any, Dict
from uuid import uuid4

 codex/preencher-src/utils/db.py-com-lógica-de-app/utils/db.py
from app.services import scorelab_service

from . import scorelab_service
 main


async def mint_reputation_nft(analysis: Dict[str, Any]) -> Dict[str, Any]:
    """Mint a reputation NFT representing the analysis result."""

    token_id = uuid4().hex
    nft = {
        "token_id": token_id,
        "ipfs_uri": f"ipfs://{token_id}",
        "issued_at": datetime.utcnow(),
        "metadata": analysis,
    }
    return nft


async def get_latest_analysis(wallet_address: str) -> Dict[str, Any] | None:
 codex/preencher-src/utils/db.py-com-lógica-de-app/utils/db.py
    """Retrieve the most recent analysis for a wallet."""

    """Proxy to ``scorelab_service.get_analysis`` for router usage."""

 main
    return await scorelab_service.get_analysis(wallet_address)
