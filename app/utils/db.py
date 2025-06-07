
"""Wrapper around ``src.utils`` database helpers."""

import os
from functools import lru_cache

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")


@lru_cache()
def get_client():
    try:
        from motor.motor_asyncio import AsyncIOMotorClient
    except Exception as exc:  # pragma: no cover - optional dependency
        raise ImportError("motor is required for database operations") from exc
    return AsyncIOMotorClient(MONGODB_URI)


def get_db():
    return get_client().foundlab
