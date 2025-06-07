
from fastapi import APIRouter
from app.models.schemas import WalletData
from app.services import engine


router = APIRouter(prefix="/score")


@router.post("/")
def calculate_score(data: WalletData):
    """Return a reputation score for the given wallet."""
    return engine.calculate_score(data)
