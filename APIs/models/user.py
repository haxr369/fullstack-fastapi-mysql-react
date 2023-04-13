from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column,ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.base_class import Base #자동으로 테이블을 만들어 준다.!!
from db.session import engine
from core.security import get_password_hash

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
    User_password = Column(String(255), nullable=False)
    Is_superuser = Column(Boolean(), default=False)
    Createtime = Column(DateTime, default=datetime.datetime.now())
    Access_count = Column(Integer, default =0)


class UserCollect(Base):
    Collect_id = Column(Integer, autoincrement=True, 
                    primary_key=True, index=True)
    User_id = Column(Integer,ForeignKey('userlist.User_id'))
    Collected_plant = Column(String(255), nullable=False )
    Collect_time = Column(DateTime, default=datetime.datetime.now())


Session = sessionmaker(bind=engine)
session = Session()

admin_user = UserList(
        User_id = 0,
        User_nickname = 'haxr',
        User_password = get_password_hash('1234'),
        Is_superuser = True
    )
session.add(admin_user)
try:
    session.commit()
except IntegrityError:
    session.rollback()
session.close()



Base.metadata.create_all(bind=engine)