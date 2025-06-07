from typing import List
from pydantic import BaseModel


class GasCheckRequest(BaseModel):
    gas_used: List[int]


class GasCheckResult(BaseModel):
    flags: List[str]
