import os

import uvicorn
from dotenv import load_dotenv

import src.app

# 防止热重载时重新创建 app
#_app_instance = None
if __name__ == 'run':
    _app_instance = src.build_app(os.path.dirname(os.path.abspath(__file__)))

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


if __name__ == '__main__':
    #  设置环境变量
    set_env(os.path.dirname(os.path.abspath(__file__)))
    # 获取当前的路径
    print("start")

    port = os.getenv('PORT')
    if port is None:
        port = 8000
    else:
        port = int(port)

    uvicorn.run("run:_app_instance", host="0.0.0.0", port=port, reload=True)
