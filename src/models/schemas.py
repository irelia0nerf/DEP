from typing import List

from pydantic import BaseModel


class WalletData(BaseModel):
    wallet_address: str
    tx_volume: float
    age_days: int
    flags: List[str] | None = None
