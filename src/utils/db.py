"""Database utilities."""

import os
from functools import lru_cache

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")


@lru_cache()
def get_client():
    """Return a cached Motor client."""
    from motor.motor_asyncio import AsyncIOMotorClient

    return AsyncIOMotorClient(MONGODB_URI)


def get_db():
    """Return the default database handle."""
    return get_client().foundlab
