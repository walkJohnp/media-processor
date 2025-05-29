import contextvars
import uuid
from contextlib import asynccontextmanager
from urllib.request import Request

from fastapi import FastAPI
from uvicorn import lifespan

from src import routes
from src.config import log_config

trace_id_context = contextvars.ContextVar('trace_id', default=None)


async def add_trace_id_to_context(request: Request, call_next):
    trace_id = str(uuid.uuid4())
    # 上下文设置 trace_id
    trace_id_context.set(trace_id)
    try:
        response = await call_next(request)
    finally:
        trace_id_context.set(None)
    return response


class App:
    def __init__(self):
        self.app = build_app()
        self.app.middleware("http")(add_trace_id_to_context)

        # 监听启动事件


def build_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(routes.hello_api.router)
    log_config.setup_logger(trace_id_context)
    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行
    await startup_event(app)
    yield
    # 关闭时执行
    await shutdown_event()


async def shutdown_event():
    print("shutdown_event")


async def startup_event(app: FastAPI):
    print("startup_event")
    for route in app.routes:
        if hasattr(route, "path"):
            print(f"Route: {route.path} | Name: {route.name} | Method: {getattr(route, 'methods', '')}")
