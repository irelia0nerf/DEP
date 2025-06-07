from fastapi import APIRouter
from app.models.schemas import WalletData
from app.services.engine import calculate_score as engine_calculate_score


router = APIRouter(prefix="/score")


@router.post("/")
def calculate_score(data: WalletData):
    """Return a reputation score for the provided wallet data."""
    return engine_calculate_score(data)
