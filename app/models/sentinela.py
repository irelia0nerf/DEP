from pydantic import BaseModel


class Event(BaseModel):
    """Generic event monitored by Sentinela."""

    wallet: str
    gas_used: int
    context: str


class EventResponse(BaseModel):
    """Outcome of event processing."""

    reanalyze: bool
