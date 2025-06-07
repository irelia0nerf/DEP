from fastapi import APIRouter
from app.models.schemas import WalletData
from app.services import engine


router = APIRouter(prefix="/score")


@router.post("/")
def calculate_score(data: WalletData):
    """Calculate a Bayesian reputation score for a wallet."""
    return engine.calculate_score(data)
