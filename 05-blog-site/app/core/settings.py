from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cache
settings = SettingsConfigDict()


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    PROJECT_VERSION: str

    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_USER: str

    model_config = SettingsConfigDict(env_file=".env")


def get_settings():
    return Settings()
