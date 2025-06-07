from fastapi import APIRouter, HTTPException
from app.models.scorelab import AnalysisRequest
from app.services import sigilmesh

router = APIRouter(prefix="/internal/v1")


@router.post("/sigilmesh/mint")
async def mint(request: AnalysisRequest):
    analysis = await sigilmesh.get_latest_analysis(request.wallet_address)
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return await sigilmesh.mint_reputation_nft(analysis)
