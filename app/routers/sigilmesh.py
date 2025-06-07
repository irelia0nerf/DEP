 codex/preencher-src/utils/db.py-com-lógica-de-app/utils/db.py
from fastapi import APIRouter, HTTPException
from app.models.scorelab import MintRequest, MintResult
from app.services import sigilmesh

"""SigilMesh NFT minting endpoints."""

from fastapi import APIRouter, HTTPException

from app.models.scorelab import MintRequest
from app.services import sigilmesh

 main

router = APIRouter(prefix="/internal/v1/sigilmesh")


 codex/preencher-src/utils/db.py-com-lógica-de-app/utils/db.py
@router.post("/mint", response_model=MintResult)
async def mint(request: MintRequest):
    """Mint a reputation NFT for the latest analysis of a wallet."""

@router.post("/mint", tags=["SigilMesh"])
async def mint_nft(request: MintRequest) -> dict:
    """Mint a reputation NFT for the given wallet."""

 main
    analysis = await sigilmesh.get_latest_analysis(request.wallet_address)
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")

    return await sigilmesh.mint_reputation_nft(analysis)
