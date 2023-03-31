from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column,ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from db.base_class import Base #자동으로 테이블을 만들어 준다.!!
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
    User_id = Column(Integer, autoincrement=True, 
                    primary_key=True, index=True)
    User_nickname = Column(String(255),   
                    unique=True, primary_key=True, nullable=False)
    User_password = Column(String, nullable=False)
    Is_superuser = Column(Boolean(), default=False)
    Createtime = Column(DateTime, default=datetime.datetime.now())
    Access_count = Column(Integer, default =0)


class UserCollect(Base):
    Collect_id = Column(Integer, autoincrement=True, 
                    primary_key=True, index=True)
    User_id = Column(Integer,ForeignKey('userlist.User_id'))
    Collected_plant = Column(String(255), nullable=False )
    Collect_time = Column(DateTime, default=datetime.datetime.now())

Base.metadata.create_all(bind=engine)