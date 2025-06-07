from fastapi import APIRouter, HTTPException

from app.models.scorelab import MintRequest, MintResult
from app.services import sigilmesh

router = APIRouter(prefix="/internal/v1/sigilmesh")


 codex/update-tests-and-fix-imports
@router.post("/mint", tags=["SigilMesh"])
async def mint_nft(request: MintRequest) -> dict:

@router.post("/mint", response_model=MintResult, tags=["SigilMesh"])
async def mint_nft(request: MintRequest) -> MintResult:
 main
    """Mint a reputation NFT for the given wallet."""
    analysis = await sigilmesh.get_latest_analysis(request.wallet_address)
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return await sigilmesh.mint_reputation_nft(analysis)
