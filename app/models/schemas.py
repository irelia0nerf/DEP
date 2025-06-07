 codex/update-tests-and-fix-imports
from pydantic import BaseModel

 6gjf82-codex/editar-src/utils/db.py-para-get_db
"""Compatibility module exposing wallet schemas."""

from src.models import WalletData

from src.models.schemas import WalletData
 main
 main


class WalletData(BaseModel):
    wallet_address: str
    tx_volume: float
    age_days: int
