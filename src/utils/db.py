 tl99zw-codex/substituir-lógica-de-db.py-por-get_db

 codex/substituir-lógica-de-db.py-por-get_db

 codex/update-tests-and-fix-imports
"""Database utilities."""

 codex/remove-unused-imports-and-fix-flake8-issues
"""Database utilities."""

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
 main
 main

 main
 main
import os
from functools import lru_cache
from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

@lru_cache()
 tl99zw-codex/substituir-lógica-de-db.py-por-get_db
def get_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(MONGODB_URI)


 codex/substituir-lógica-de-db.py-por-get_db
def get_client() -> AsyncIOMotorClient:

def get_client():
    """Return a cached Motor client."""
    from motor.motor_asyncio import AsyncIOMotorClient

 main
    return AsyncIOMotorClient(MONGODB_URI)

 main
def get_db():
    """Return the default database handle."""
    return get_client().foundlab
 tl99zw-codex/substituir-lógica-de-db.py-por-get_db

 codex/substituir-lógica-de-db.py-por-get_db

 codex/update-tests-and-fix-imports

 codex/remove-unused-imports-and-fix-flake8-issues


"""Database utilities."""


def get_db():
    """Return a database handle (placeholder)."""
    raise NotImplementedError
 main
 main
 main
 main
 main
 main