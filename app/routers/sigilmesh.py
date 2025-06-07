"""Endpoints for SigilMesh NFT minting."""

from fastapi import APIRouter
from app.models.sigil import SigilRequest, SigilResult
from app.services import sigilmesh

router = APIRouter(prefix="/internal/v1")


@router.post("/sigilmesh/mint", response_model=SigilResult)
async def mint_sigil(data: SigilRequest) -> SigilResult:
    """Mint a reputation NFT from analysis results."""

    result = await sigilmesh.mint_reputation_nft(data.dict())
    return SigilResult(**result)
