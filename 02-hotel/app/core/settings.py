# settings.py
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cache


class Settings(BaseSettings):
    # PROJECT METADATA
    PROJECT_NAME: str = "Default Project Name"
    PROJECT_DESCRIPTION: Optional[str] = None
    PROJECT_VERSION: str = "0.0.1"

    # POSTGRES CREDENTIALS
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str

    model_config = SettingsConfigDict(env_file=".env")


@cache
def get_settings() -> Settings:
    return Settings()