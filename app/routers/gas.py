from fastapi import APIRouter

from app.models.gas import GasCheckRequest, GasCheckResult
from app.services import gas_monitor

router = APIRouter(prefix="/internal/v1")


@router.post("/gas/check", response_model=GasCheckResult)
async def check_gas_usage(request: GasCheckRequest):
    """Run a manual gas usage analysis."""
    flags, avg = gas_monitor.detect_gas_patterns(request.gas_used)
    return GasCheckResult(flags=flags, avg_gas=avg)
