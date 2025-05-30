# 示例：在 FastAPI 路由中使用
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.dao.database import get_db
from src.dao.models.content import Content

router = APIRouter()

@router.get("/contents")
def read_contents(db: Session = Depends(get_db)):
    contents = db.query(Content).all()
    return {"data": contents}
