"""Database utilities for MongoDB access."""

import os
from functools import lru_cache

from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")


@lru_cache()
def get_client() -> AsyncIOMotorClient:
    """Return a cached Motor client instance."""
    return AsyncIOMotorClient(MONGODB_URI)


def get_db():
    """Return a handle to the FoundLab database."""
    return get_client().foundlab
