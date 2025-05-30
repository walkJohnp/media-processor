import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def load_database():
    global engine, SessionLocal

    user = os.getenv("mysql.user")
    password = os.getenv("mysql.password")
    host = os.getenv("mysql.host")
    port = os.getenv("mysql.port")
    database = os.getenv("mysql.database")
    db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

    engine = create_engine(db_url)
    # 实例化 session 工厂类
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 获取数据库连接
def get_db():
    db = SessionLocal()
    try:
        yield db  # ✅ 确保返回有效的 Session
    finally:
        db.close()