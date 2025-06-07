from pydantic import BaseModel


class WalletData(BaseModel):
    """Basic wallet information for score calculation."""

    wallet_address: str
    tx_volume: float
    age_days: int
