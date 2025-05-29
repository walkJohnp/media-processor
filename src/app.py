import contextvars
import os
import uuid
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI,Request
from uvicorn import lifespan

from src.log_config import setup_logger
from src.routes import register_routes


def set_env(path):
    # 读取环境变量
    env = os.getenv('ENV')

    # 加载基础配置文件
    load_dotenv(path + '/.env')

    env_path = '.env'
    # 设定dotenv 读取的 env配置文件
    if env == 'dev':
        env_path = '.env.dev'
    elif env == 'test':
        env_path = '.env.test'
    elif env == 'prod':
        env_path = '.env.prod'

    load_dotenv(env_path, override=True)


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
        print("build app")


def build_app(path) -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.middleware("http")(add_trace_id_to_context)  # 注册中间件

    # 加载环境变量
    set_env(path)

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
