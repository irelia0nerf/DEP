from pydantic import BaseModel


class MintRequest(BaseModel):
    snapshot_id: str
    wallet: str


class MintResult(BaseModel):
    nft_id: str
    snapshot_id: str
    wallet: str
