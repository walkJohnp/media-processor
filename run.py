import os

import uvicorn

import src.app
from src.config.env_config import set_env

set_env(os.path.dirname(os.path.abspath(__file__)))
app = src.build_app()


if __name__ == '__main__':
    #  设置环境变量
    # 获取当前的路径
    print("start")


    port = os.getenv('PORT')
    if port is None:
        port = 8000
    else:
        port = int(port)


    uvicorn.run("run:app", host="0.0.0.0", port=port, reload=True)
