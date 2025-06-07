from __future__ import annotations


def mint_reputation_nft(analysis: dict) -> dict:
    """Return a representation of a minted reputation NFT."""
    nft_id = f"nft-{analysis['wallet']}"
    return {"nft_id": nft_id, "analysis": analysis}
