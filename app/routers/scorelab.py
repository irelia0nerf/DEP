from fastapi import APIRouter
from app.models.scorelab import AnalysisRequest, AnalysisResult
from app.services import scorelab_service

router = APIRouter()


@router.post("/scorelab/analyze", response_model=AnalysisResult)
async def analyze(request: AnalysisRequest):
    """Analyze a wallet and return reputation results."""
    return await scorelab_service.analyze(request.wallet_address)
