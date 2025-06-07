"""SigilMesh NFT minting simulation service."""

from datetime import datetime
from typing import Any, Dict, Optional

from app.utils.db import get_db


async def get_latest_analysis(wallet_address: str) -> Optional[Dict[str, Any]]:
    """Return the most recent analysis for a wallet from MongoDB."""
    db = get_db()
    doc = await db.analysis.find_one(
        {"wallet": wallet_address}, sort=[("timestamp", -1)]
    )
    return doc


async def mint_reputation_nft(analysis: Dict[str, Any]) -> Dict[str, Any]:
    """Simulate minting a reputation NFT from an analysis result."""
    metadata = {
        "wallet": analysis["wallet"],
        "score": analysis["score"],
        "tier": analysis["tier"],
        "flags": analysis["flags"],
        "timestamp": (
            analysis["timestamp"].isoformat()
            if hasattr(analysis["timestamp"], "isoformat")
            else analysis["timestamp"]
        ),
    }
    token_id = int(datetime.utcnow().timestamp())
    return {"token_id": token_id, "metadata": metadata}
