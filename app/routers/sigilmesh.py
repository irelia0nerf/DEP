from fastapi import APIRouter, HTTPException
from app.models.scorelab import MintRequest, MintResult
from app.services import sigilmesh, scorelab_service


class MintRequest(BaseModel):
    analysis: dict


router = APIRouter(prefix="/internal/v1/sigilmesh")

    analysis = await scorelab_service.get_analysis(request.wallet_address)
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return await sigilmesh.mint_reputation_nft(analysis)
