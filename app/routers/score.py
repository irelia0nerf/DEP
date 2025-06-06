from fastapi import APIRouter
from app.models.schemas import WalletData
from app.services.engine import calculate_score


router = APIRouter(prefix="/score")


@router.post("/")
async def score_wallet(data: WalletData) -> dict:
    """Return a Bayesian risk score for the given wallet."""
    return await calculate_score(data)

