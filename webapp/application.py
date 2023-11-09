"""Application module."""

from fastapi import FastAPI

from .core.containers import Container
from .endpoint import user 

import uvicorn
def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(user.router)
    return app

app = create_app()


