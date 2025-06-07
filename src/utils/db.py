"""Lightweight database helpers used across services."""

import os
from functools import lru_cache

try:
    from motor.motor_asyncio import AsyncIOMotorClient
except Exception:  # pragma: no cover - optional dependency
    AsyncIOMotorClient = None  # type: ignore

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")


@lru_cache()
def get_client() -> AsyncIOMotorClient:
    if AsyncIOMotorClient is None:
        raise ImportError("motor is required for database operations")
    return AsyncIOMotorClient(MONGODB_URI)


def get_db():
    return get_client()["foundlab_dep"]
