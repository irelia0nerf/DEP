
from fastapi import APIRouter


from app.models.schemas import WalletData
from app.services import engine

router = APIRouter(prefix="/score")


@router.post(
    "/",
    tags=["Score"],
    response_model=dict,
    responses={
        200: {
            "description": "Calculated score information",
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
def calculate_score(data: WalletData):
    """Calculate a score for the wallet using the engine service."""

    return engine.calculate_score(data)
