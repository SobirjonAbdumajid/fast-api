from functools import cache
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from app.core.settings import Settings

settings = Settings()


@cache
def get_async_engine() -> AsyncEngine:
    return create_async_engine(
        f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}",
        pool_size=2
    )
