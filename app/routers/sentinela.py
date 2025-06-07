"""Endpoints for Sentinela monitoring service."""

from fastapi import APIRouter
from app.models.sentinela import Event, EventResponse
from app.services import sentinela

router = APIRouter(prefix="/internal/v1")


@router.post("/sentinela/event", response_model=EventResponse)
async def process(event: Event) -> EventResponse:
    """Process an incoming event and signal if reanalysis is needed."""

    result = await sentinela.process_event(event.dict())
    return EventResponse(**result)
