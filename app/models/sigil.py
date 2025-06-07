from pydantic import BaseModel
from typing import List


class SigilRequest(BaseModel):
    """Input for minting a reputation NFT."""

    wallet: str
    score: int
    flags: List[str]


class SigilResult(BaseModel):
    """Details about the minted NFT."""

    token_id: str
    ipfs_url: str
