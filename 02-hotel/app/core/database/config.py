# config.py
from functools import cache
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from app.core.settings import get_settings

settings = get_settings()

postgres_url = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"


@cache
def get_async_engine():
    return create_async_engine(postgres_url, pool_size=3)


def add(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x


print(add(27, 5))
