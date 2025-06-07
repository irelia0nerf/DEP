from fastapi import APIRouter
from app.models.scorelab import AnalysisRequest, AnalysisResult
from app.services import scorelab_service

router = APIRouter(prefix="/internal/v1")


@router.post(
    "/scorelab/analyze",
    tags=["ScoreLab"],
    response_model=AnalysisResult,
    responses={
        200: {
            "description": "Analysis result",
            "content": {
                "application/json": {
                    "example": {
                        "wallet": "0xabc",
                        "flags": ["MOCK_FLAG"],
                        "score": 90,
                        "tier": "AAA",
                        "confidence": 0.99,
                        "timestamp": "2024-01-01T00:00:00Z",
                    }
                }
            },
        }
    },
)
async def analyze(request: AnalysisRequest):
    """Analyze a wallet with ScoreLab and return reputation results.

    Example
    -------
    Request payload::

        {
            "wallet_address": "0xabc"
        }
    """

    return await scorelab_service.analyze(request.wallet_address)
