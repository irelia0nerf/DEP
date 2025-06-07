"""Endpoints for Gas Monitor."""

from fastapi import APIRouter
from app.models.gas import GasData, GasAnalysis
from app.services import gas_monitor

router = APIRouter(prefix="/internal/v1")


@router.post("/gasmonitor/analyze", response_model=GasAnalysis)
async def analyze_gas(data: GasData) -> GasAnalysis:
    """Analyze gas usage and return detected anomalies."""

    result = await gas_monitor.analyze_gas(data.gas_values)
    return GasAnalysis(**result)
