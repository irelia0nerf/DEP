from fastapi import APIRouter
from app.models.schemas import WalletData

router = APIRouter(prefix="/score")


@router.post("/")
def calculate_score(data: WalletData):
    # mock score
    return {
        "score": 752,
        "tier": "B",
        "probability": 0.75,
        "flags": ["mixer_usage", "low_activity"],
    }
