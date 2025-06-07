from fastapi import APIRouter, HTTPException
from app.models.scorelab import MintRequest, MintResult
from app.services import sigilmesh

router = APIRouter(prefix="/internal/v1/sigilmesh")


@router.post("/mint", response_model=MintResult)
async def mint(request: MintRequest):
    """Mint a reputation NFT for the latest analysis of a wallet."""
    analysis = await sigilmesh.get_latest_analysis(request.wallet_address)
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return await sigilmesh.mint_reputation_nft(analysis)
