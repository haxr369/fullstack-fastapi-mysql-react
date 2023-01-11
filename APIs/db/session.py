from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
print("DSN:",settings.SQLALCHEMY_DATABASE_URI)
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)