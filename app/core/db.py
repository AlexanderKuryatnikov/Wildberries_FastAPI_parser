from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(PreBase)

engine = create_async_engine(settings.db_url)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
