from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from svc.core import auth
from svc.routes import views


def create_app() -> FastAPI:
    """Create a FastAPI application."""

    app = FastAPI()

    # Set all CORS enabled origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth.router)
    app.include_router(views.router)
    return app


app = create_app()
