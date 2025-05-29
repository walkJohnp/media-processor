# src/routes/__init__.py
from . import hello_api  # Use relative import


def register_routes(app):
    app.include_router(hello_api.router)
