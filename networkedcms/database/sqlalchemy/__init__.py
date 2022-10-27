from networkedcms.database.sqlalchemy.engine import Base
from networkedcms.database.sqlalchemy.fields import IntegerField, DateTimeField
from sqlalchemy import func, Column
from sqlalchemy.ext.asyncio import AsyncSession





async def init_models(engine):
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.run_sync(
            Base.metadata.reflect)


class BaseModel(Base):
    """Base model class that includes CRUD convenience methods."""
    __abstract__ = True

    id = Column(IntegerField, autoincrement=True, primary_key=True, index=True)

    created_at = Column(DateTimeField, default=func.now())
    updated_at = Column(DateTimeField, default=func.now(), onupdate=func.now())
