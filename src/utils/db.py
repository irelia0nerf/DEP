 6gjf82-codex/editar-src/utils/db.py-para-get_db
"""Compatibility layer for database helpers."""

from app.utils.db import get_client as app_get_client, get_db as app_get_db


def get_client():
    """Return the Motor client from :mod:`app.utils.db`."""

    return app_get_client()


def get_db():
    """Return the main database handle from :mod:`app.utils.db`."""

    return app_get_db()


__all__ = ["get_client", "get_db"]

 codex/preencher-src/utils/db.py-com-lógica-de-app/utils/db.py
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

"""Database utilities."""


def get_db():
    """Return a database handle (placeholder)."""
    raise NotImplementedError
 main
 main
