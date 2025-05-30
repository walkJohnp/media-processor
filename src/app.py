import contextvars
import uuid
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from uvicorn import lifespan

from src.dao.database import load_database
from src.log_config import setup_logger
from src.routes import register_routes


trace_id_context = contextvars.ContextVar('trace_id', default=None)

async def add_trace_id_to_context(request: Request, call_next):
    trace_id = str(uuid.uuid4())
    # 上下文设置 trace_id
    trace_id_context.set(trace_id)
    try:
        response = await call_next(request)
        # 在 response 中设置 trace_id这个 header
        response.headers['trace_id'] = trace_id
    finally:
        trace_id_context.set(None)
    return response


def build_app(path) -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.middleware("http")(add_trace_id_to_context)  # 注册中间件

    # 加载环境变量
    #set_env(path)

    # 加载数据库
    load_database()

    # 注册路由
    register_routes(app)

    # 设置日志
    setup_logger(trace_id_context)

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
