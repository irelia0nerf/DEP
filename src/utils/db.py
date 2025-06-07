from app.utils.db import get_client as app_get_client, get_db as app_get_db
from app.utils.db import get_client as app_get_client, get_db as app_get_db

__all__ = ["get_client", "get_db"]


def get_client():
    """Return the Motor client from :mod:`app.utils.db`."""
    return app_get_client()


def get_db():
    """Return the main database handle from :mod:`app.utils.db`."""
    return app_get_db()
