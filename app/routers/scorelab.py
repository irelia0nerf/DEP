from fastapi import APIRouter
from app.models.scorelab import AnalysisRequest, AnalysisResult
from app.services import scorelab_service

router = APIRouter(prefix="/internal/v1")


@router.post(
    "/scorelab/analyze",
    response_model=AnalysisResult,
    tags=["ScoreLab"],
    responses={
        200: {
            "description": "Detailed reputation analysis",
            "content": {
                "application/json": {
                    "example": {
                        "wallet": "0x123",
                        "flags": ["MOCK_FLAG"],
                        "score": 90,
                        "tier": "AAA",
                        "confidence": 0.99,
                    }
                }
            },
        }
    },
)
async def analyze(request: AnalysisRequest):
    """Analyze a wallet with ScoreLab and return its reputation.

    Example request body::

        {
            "wallet_address": "0x123"
        }
    """

    return await scorelab_service.analyze(request.wallet_address)
