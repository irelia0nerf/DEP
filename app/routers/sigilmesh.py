"""SigilMesh NFT minting endpoints."""

from fastapi import APIRouter, HTTPException

from app.models.scorelab import MintRequest
from app.services import sigilmesh


router = APIRouter(prefix="/internal/v1/sigilmesh")


@router.post("/mint", tags=["SigilMesh"])
async def mint_nft(request: MintRequest) -> dict:
    """Mint a reputation NFT for the given wallet."""

    analysis = await sigilmesh.get_latest_analysis(request.wallet_address)
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")

    return await sigilmesh.mint_reputation_nft(analysis)
