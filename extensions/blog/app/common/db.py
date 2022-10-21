import os
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine


from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from config import config


def get_app_config():
    if os.getenv('FLASK_CONFIG') == "development":
        return config['development']
    elif os.getenv('FLASK_CONFIG') == "testing":
        return config['testing'] 
    elif os.getenv('FLASK_CONFIG') == "production":
        return config['production']       




engine = create_async_engine(get_app_config().SQLALCHEMY_DATABASE_URI, echo=True)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)



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



        



async def init_models():
    async with engine.begin() as conn:
        #await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)




# Dependency
db_session = AsyncSession(engine)

        




