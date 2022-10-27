"""Provides access to the Mongo database."""
import os
from datetime import datetime
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Type, Union
import pymongo.errors
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from settings.conf import settings

# region Internal functionality


# endregion

_engine: Optional[AIOEngine] = None


async def set_engine_connection(conn: str, db: str):
    """Connect or re-connect the database engine to the specified connection string."""
    global _engine
    if _engine is not None:
        del _engine
    _engine = AIOEngine(
        AsyncIOMotorClient(conn),
        database=db
    )


async def get_engine() -> AIOEngine:
    """Return a MongoDB engine. Reuses an already-initialized instance, if available."""
    global _engine
    if _engine:
        return _engine
    await set_engine_connection(conn=settings.MONGO_CONN_URI, db=settings.MONGO_DATABASE)
    if not _engine:
        raise RuntimeError('Failed to connect to MongoDB.')
    return _engine
