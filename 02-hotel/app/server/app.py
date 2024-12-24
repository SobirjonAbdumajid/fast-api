from fastapi import FastAPI

from app.core.settings import get_settings

from app.api.views.rooms import router as rooms_router

from app.api.views.auth import router as auth_router

from app.api.views.bookings import router as bookings_router

settings = get_settings()


def create_app() -> FastAPI:
    app_ = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
    )
    app_.include_router(rooms_router, prefix="/rooms")
    app_.include_router(auth_router, prefix="/auth")
    app_.include_router(bookings_router, prefix="/bookings")
    return app_
