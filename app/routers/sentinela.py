from fastapi import APIRouter
from pydantic import BaseModel

from app.services import sentinela


class Event(BaseModel):
    wallet: str
    gas: int
    anomaly: bool | None = None


router = APIRouter(prefix="/internal/v1/sentinela")


@router.post("/check")
def check_event(event: Event):
    """Check whether the given event would trigger a reanalysis."""

    return {"trigger": sentinela.is_flag_trigger(event.model_dump())}
