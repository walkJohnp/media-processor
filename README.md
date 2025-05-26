# media-processor
媒体处理

#  目录结构
```
my_project/
├── src/               # 源代码目录（核心逻辑）
│   ├── module1/       # 功能模块1
│   │   ├── __init__.py
│   │   └── core.py
│   └── module2/       # 功能模块2
├── tests/             # 测试代码（单元测试/集成测试）
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
├── docs/              # 项目文档（如API说明）
├── scripts/           # 可执行脚本（如部署脚本）
├── requirements.txt   # 项目依赖库清单
├── setup.py           # 项目打包配置
├── .gitignore         # Git忽略规则
└── README.md          # 项目说明
```

# Quick start
1. 创建虚拟环境 
``` 
conda create -n media-processor python=3.11
```
2. 安装依赖库
