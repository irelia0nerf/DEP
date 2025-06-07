from fastapi import APIRouter
from app.models.schemas import WalletData
from app.services import engine

router = APIRouter(prefix="/score")


@router.post("/")
def calculate_score(data: WalletData):
    """Return score information for a wallet."""
    return engine.calculate_score(data)
