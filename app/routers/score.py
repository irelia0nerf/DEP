from fastapi import APIRouter
from app.models.schemas import WalletData
from app.services import engine
from app.services import engine

router = APIRouter(prefix="/score")


@router.post("/")
def calculate_score(data: WalletData):
    """Return a reputation score using the Engine service."""
    return engine.calculate_score(data)
