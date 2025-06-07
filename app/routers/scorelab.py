from fastapi import APIRouter

from app.models.scorelab import AnalysisRequest, AnalysisResult
from app.services import scorelab_service

router = APIRouter(prefix="/internal/v1")


@router.post(
    "/scorelab/analyze",
    tags=["ScoreLab"],
    response_model=AnalysisResult,
    responses={200: {"description": "Analysis result"}},
)
async def analyze(request: AnalysisRequest):
    """Analyze a wallet with ScoreLab and return reputation results."""
    return await scorelab_service.analyze(request.wallet_address)
