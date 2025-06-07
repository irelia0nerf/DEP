
from fastapi import APIRouter


from app.models.schemas import WalletData
from app.services import engine

router = APIRouter(prefix="/score")


@router.post(
    "/",
    tags=["Score"],
    description="Calculate a wallet risk score",
    responses={
        200: {
            "description": "Score calculation result",
            "content": {
                "application/json": {
                    "example": {
                        "score": 752,
                        "tier": "B",
                        "probability": 0.75,
                        "flags": ["mixer_usage", "low_activity"],
                    }
                }
            },
        }
    },
)
async def calculate_score(data: WalletData):
    """Calculate a wallet risk score using the engine."""
    return await engine.calculate_score(data)
