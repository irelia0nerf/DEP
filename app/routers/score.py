from fastapi import APIRouter

from app.models.schemas import WalletData
from app.services import engine

router = APIRouter(prefix="/score")


@router.post("/")
async def calculate_score_endpoint(data: WalletData):
    """Return a probability-based score for the wallet."""
    return engine.calculate_score(data)

