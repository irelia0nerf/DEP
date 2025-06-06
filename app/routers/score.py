from fastapi import APIRouter
from app.models.schemas import WalletData
from app.services.engine import calculate_px

router = APIRouter(prefix="/score")


@router.post("/")
async def calculate_score(data: WalletData):
    """Calculate Px score for the provided wallet data."""
    flags = {
        "new_wallet": data.age_days < 30,
        "high_volume": data.tx_volume > 1000,
    }
    weights = {
        "new_wallet": -0.15,
        "high_volume": 0.10,
    }
    px = calculate_px(flags, weights)
    return {"px": px, "flags": flags}
