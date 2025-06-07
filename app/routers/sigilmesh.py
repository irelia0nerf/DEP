from fastapi import APIRouter
from pydantic import BaseModel

from app.services import sigilmesh


class MintRequest(BaseModel):
    analysis: dict


router = APIRouter(prefix="/internal/v1/sigilmesh")


@router.post("/mint")
async def mint(req: MintRequest):
    """Mint a reputation NFT for a given analysis."""

    return await sigilmesh.mint_reputation_nft(req.analysis)
