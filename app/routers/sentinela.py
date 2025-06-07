from fastapi import APIRouter
from pydantic import BaseModel

from app.services import sentinela


router = APIRouter(prefix="/internal/v1/sentinela")


class Event(BaseModel):
    wallet: str | None = None
    gas: int = 0
    anomaly: bool = False


@router.post("/check")
def check_event(event: Event):
    """Check whether the given event would trigger a reanalysis."""

    return {"trigger": sentinela.is_flag_trigger(event.model_dump())}
