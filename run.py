import os

import uvicorn

import src.app

# 防止热重载时重新创建 app
_app_instance = None
if _app_instance is None:
    _app_instance = src.build_app(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    #  设置环境变量
    # 获取当前的路径
    print("start")


    port = os.getenv('PORT')
    if port is None:
        port = 8000
    else:
        port = int(port)

    uvicorn.run("run:_app_instance", host="0.0.0.0", port=port, reload=True)
