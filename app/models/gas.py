from pydantic import BaseModel
from typing import List


class GasData(BaseModel):
    """Gas usage data for analysis."""

    gas_values: List[int]


class GasAnalysis(BaseModel):
    """Result of gas pattern analysis."""

    anomalies: List[str]
