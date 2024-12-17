from fastapi import FastAPI

from app.core.settings import get_settings

from app.api.views.test import router as test_router

settings = get_settings()


def create_app() -> FastAPI:
    app_ = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
    )
    app_.include_router(test_router)
    return app_
