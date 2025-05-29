from sqlalchemy import Column, Integer, String, BIGINT

from .CustomBase import Base


class AuditRecord(Base):
    __tablename__ = "audit_record"

    id = Column(Integer, primary_key=True)
    content_id = Column(BIGINT)
    machine_audit_status = Column(String(50)) # 机器审核状态
    human_audit_status = Column(String(50))

    created_at = Column(String(50))
    updated_at = Column(String(50))
    created_by = Column(String(50))
    updated_by = Column(String(50))
