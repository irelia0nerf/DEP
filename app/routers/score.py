from fastapi import APIRouter

from app.models.schemas import WalletData

router = APIRouter(prefix="/score")


@router.post(
    "/",
    description="Calculate a wallet risk score",
    tags=["Score"],
    responses={
        200: {
            "content": {
                "application/json": {"example": {"score": 752, "tier": "B"}}
            }
        }
    },
)
async def calculate_score(data: WalletData):
    """Calculate a wallet score using the engine service."""
    from app.services import engine

    return await engine.calculate_score(data)
