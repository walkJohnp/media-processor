from sqlalchemy import Column, Integer, String, BIGINT, DateTime, func
from sqlalchemy.ext.declarative import declarative_base


class CustomBase:
    # 添加公共字段
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    created_by = Column(String(50))
    updated_by = Column(String(50))

    # 添加自定义方法（示例）
    def __init__(self):
        self.__table__ = None

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base = declarative_base(cls = CustomBase)
