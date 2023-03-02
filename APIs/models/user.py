from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from db.base_class import Base#자동으로 테이블을 만들어 준다.!!
from db.session import engine
if TYPE_CHECKING:
    from .item import Item  # noqa: F401

"""class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean(), default=True)
    
    items = relationship("Item", back_populates="owner")"""


class UserList(Base):
    User_id = Column(Integer, primary_key = True)
    Is_superuser = Column(Boolean(), default=False)
    Create_time = Column(DateTime, default=datetime.datetime.now())
    Access_count = Column(Integer, default =0)