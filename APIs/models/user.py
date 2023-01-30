from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from db.base_class import Base #자동으로 테이블을 만들어 준다.!!

if TYPE_CHECKING:
    from .item import Item  # noqa: F401

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")


class jwtUser(Base):
    username = Column(String, primary_key = True)
    create_date = Column(DateTime, default=datetime.datetime.now())


