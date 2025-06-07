from fastapi import APIRouter
from src.models.schemas import WalletData

router = APIRouter(prefix="/score")


@router.post("/")
async def calculate_score(data: WalletData):
    # mock score
    return {"score": 752, "tier": "B", "flags": ["mixer_usage", "low_activity"]}
