from fastapi import APIRouter
from app.models.schemas import WalletData
from app.services import engine


router = APIRouter(prefix="/score")


@router.post(
    "/",
    tags=["Score"],
    responses={
        200: {
            "description": "Score computed successfully",
            "content": {
                "application/json": {
                    "example": {
                        "score": 752,
                        "tier": "B",
                        "flags": ["mixer_usage", "low_activity"],
                    }
                }
            },
        }
    },
)
def calculate_score(data: WalletData):
    """Calculate a wallet risk score using basic heuristics.

    Example request body::

        {
            "wallet_address": "0xabc",
            "tx_volume": 1200,
            "age_days": 365
        }
    """

    # mock score
    return {"score": 752, "tier": "B", "flags": ["mixer_usage", "low_activity"]}
