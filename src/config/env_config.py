import os

from dotenv import load_dotenv


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
