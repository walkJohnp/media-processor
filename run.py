import os

import uvicorn

import src.app

app = src.build_app(os.path.dirname(os.path.abspath(__file__)))

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
