
from fastapi import APIRouter
from src.models import WalletData
from app.services import engine

router = APIRouter(prefix="/score")


@router.post("/")
async def calculate_score(data: WalletData):
    """Return a reputation score calculated via Bayesian inference."""
    return engine.calculate_score(data)
