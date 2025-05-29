from sqlalchemy import Column, Integer, String

from .CustomBase import Base


class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    origin_url = Column(String(100)) # 源文件
    thumbnail_url = Column(String(100)) # 缩略图
    audit_status = Column(Integer) # 审核状态 0-未审核 1=审核中， 2=审核通过 3=审核不通过
    created_at = Column(String(50))
    updated_at = Column(String(50))
    created_by = Column(String(50))
    updated_by = Column(String(50))
