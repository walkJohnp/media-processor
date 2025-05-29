import contextvars
import os
import uuid
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from flask import Request

import src.config.log_config
from src.route.hello_api import router
import src.config
from src.config.env_config import set_env

trace_id_context = contextvars.ContextVar('trace_id', default=None)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行
    await startup_event()
    yield
    # 关闭时执行
    await shutdown_event()

async def startup_event():
    print("startup_event")
    for route in app.routes:
        if hasattr(route, "path"):
            print(f"Route: {route.path} | Name: {route.name} | Method: {getattr(route, 'methods', '')}")


async def shutdown_event():
    print("shutdown_event")


async def add_trace_id_to_context(request: Request, call_next):
    trace_id = str(uuid.uuid4())
    # 上下文设置 trace_id
    trace_id_context.set(trace_id)
    try:
        response = await call_next(request)
    finally:
        trace_id_context.set(None)
    return response

def buildApp() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.middleware("http") (add_trace_id_to_context)
    app.include_router(router)
    return app


app = buildApp()


if __name__ == '__main__':
    #  设置环境变量
    # 获取当前的路径
    print("start")

    set_env(os.path.dirname(os.path.abspath(__file__)))

    port = os.getenv('PORT')
    if port is None:
        port = 8000
    else:
        port = int(port)

    #  设置日志，trace_id
    src.config.log_config.setup_logger(trace_id_context)

    # 加载路由模块
    uvicorn.run("run:app", host="0.0.0.0", port=port, reload=True)