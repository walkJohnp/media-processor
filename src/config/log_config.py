import contextvars
import logging
import os
from logging.handlers import RotatingFileHandler




class ContextFilter(logging.Filter):

    def __init__(self, trace_id_var:  contextvars.ContextVar):
        super().__init__()
        self.trace_id_var = trace_id_var
    def filter(self, record):
        record.trace_id = self.trace_id_var.get()
        return True

def setup_logger(trace_id_context_var:  contextvars.ContextVar):
    # 从 .env 文件读取 LOG_PATH
    log_path = os.getenv('LOG_PATH', 'logs')  # 如果未设置，默认使用 'logs' 目录

    # 确保日志目录存在
    os.makedirs(log_path, exist_ok=True)

    # 构建日志文件的完整路径
    log_file = os.path.join(log_path, 'app.config')

    logger = logging.getLogger('appLogger')
    log_level = os.getenv('log.level')
    logger.setLevel(log_level)

    # 创建 RotatingFileHandler
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)

    # 创建格式器
    formatter = logging.Formatter(os.getenv('config.format'), datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)

    # 添加处理器到 logger
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level=log_level)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addFilter(ContextFilter(trace_id_context_var))
    return logger
