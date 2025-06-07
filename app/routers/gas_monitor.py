from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app.services import gas_monitor


class GasHistory(BaseModel):
    gas_prices: List[int]


router = APIRouter(prefix="/internal/v1/gasmonitor")


@router.post("/analyze")
def analyze_gas(history: GasHistory):
    """Return gas usage analysis for the provided history."""

    return gas_monitor.analyze_gas_usage(history.gas_prices)
