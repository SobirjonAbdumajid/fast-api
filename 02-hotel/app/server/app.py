# app.py
from fastapi import FastAPI
from app.core.settings import get_settings

settings = get_settings()


def create_app() -> FastAPI:
    app_ = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
    )
    return app_


app = create_app()


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}
