"""Database utilities wrapping the core app helpers."""

from app.utils.db import get_client as app_get_client, get_db as app_get_db

get_client = app_get_client
get_db = app_get_db

__all__ = ["get_client", "get_db"]
