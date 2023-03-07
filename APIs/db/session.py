from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from core.config import settings

print("DSN:",settings.SQLALCHEMY_DATABASE_URI)


engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
ins = inspect(engine)
for _t in ins.get_table_names():
    print("여기는 DB의 table 체크!!!!" ,_t)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)