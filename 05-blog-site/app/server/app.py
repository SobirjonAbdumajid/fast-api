from fastapi import FastAPI
from app.core.settings import get_settings

from app.api.views.test import router as test_router

app = FastAPI()

settings = get_settings()


def run_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION
    )

    app.include_router(test_router, prefix='/test')

    return app

