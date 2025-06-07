import os
from functools import lru_cache
from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

@lru_cache()
def get_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(MONGODB_URI)

def get_db():
    return get_client().foundlab
