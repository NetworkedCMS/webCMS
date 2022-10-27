from __future__ import annotations
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import inspect, MetaData, Table


class AsyncEngine:
    _engine = None

    def __init__(self, user: str = None, password: str = None,
                 host: str = None, port: int = None, database: str = None) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def setup_conn_str(self):
        """Returns  a concatenated url """
        return "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
            self.user, self.password, self.host, self.port, self.database)

    @classmethod
    def create_engine(cls, *args, **kwargs):
        if cls._engine is None:
            _engine = create_async_engine(cls.setup_conn_str(), echo=True,
                                          *args, **kwargs)
            return _engine
        else:
            return _engine

    def async_engine(self):
        """Creates an async engine""" 

        ... 

    
    # Dependency
    async def get_session(self) -> AsyncSession:
        async with self.async_engine() as session:
            yield session
            async with self._engine.begin() as conn:
                metadata = MetaData(bind=conn)
                metadata.reflect()         


@as_declarative()
class Base():
    """SQLAlchemy :class:`~sqlalchemy.orm.query.Query` subclass with convenience methods for querying in a web application.
    This is the default :attr:`~Model.query` object used for models, and exposed as :attr:`~SQLAlchemy.Query`.
    Override the query class for an individual model by subclassing this and setting :attr:`~Model.query_class`.
    """

    def _asdict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"









