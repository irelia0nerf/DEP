from fastapi import APIRouter
from app.models.sigil import MintRequest, MintResult
from app.services import sigilmesh


router = APIRouter(prefix="/internal/v1")


@router.post("/sigilmesh/mint", response_model=MintResult)
async def mint(request: MintRequest):
    return await sigilmesh.mint_snapshot(request.dict())
