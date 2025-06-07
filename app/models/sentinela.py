from pydantic import BaseModel


class Event(BaseModel):
    """Event data monitored by Sentinela."""

    wallet: str
    gas: int = 0
    anomaly: bool = False


class EventResponse(BaseModel):
    """Outcome of event processing."""

    reanalyze: bool
