from fastapi import APIRouter
from app.models.gas_monitor import GasCheckRequest, GasCheckResult
from app.services import gas_monitor

router = APIRouter(prefix="/internal/v1")


@router.post("/gasmonitor/check", response_model=GasCheckResult)
async def gas_check(request: GasCheckRequest) -> GasCheckResult:
    flags = gas_monitor.detect_anomalies(request.gas_used)
    return GasCheckResult(flags=flags)
