from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from svc.core import auth
from svc.core.config import get_settings
from svc.core.logger import configure_logger
from svc.routes import views


def create_app() -> FastAPI:
    """Create a FastAPI application."""

    configure_logger()
    settings = get_settings()
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allow_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["Accept", "Authorization", "Content-Type"],
    )

    app.include_router(auth.router)
    app.include_router(views.router)
    return app


app = create_app()
