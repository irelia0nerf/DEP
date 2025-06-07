from fastapi import APIRouter
from src.models import WalletData
from src.services import calculate_score as engine_calculate_score

router = APIRouter(prefix="/score")


@router.post("/")
async def calculate_score(data: WalletData):
    """Return a reputation score using ``src`` utilities."""
    return await engine_calculate_score(data)
