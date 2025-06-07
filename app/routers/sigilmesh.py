from fastapi import APIRouter, HTTPException
from app.models.scorelab import MintRequest, MintResult
from app.services import sigilmesh, scorelab_service

router = APIRouter(prefix="/internal/v1")


@router.post("/sigilmesh/mint", response_model=MintResult)
async def mint_nft(request: MintRequest):
    """Mint a reputation NFT based on a stored analysis."""

    analysis = await scorelab_service.get_analysis(request.wallet_address)
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return await sigilmesh.mint_reputation_nft(analysis)
