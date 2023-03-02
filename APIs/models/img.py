from typing import TYPE_CHECKING
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, BLOB
from sqlalchemy.orm import relationship
from db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class UserImage(Base):
    Image_id = Column(Integer, primary_key=True, autoincrement=True)
    User_id = Column(Integer, ForeignKey('UserList.User_id'))
    Image_url = Column(String(100))
    Send_time = Column(DateTime, default=datetime.datetime.now())

#식물 샘플 이미지 경로 테이블
class SampleImage(Base):
    Image_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    Plant_id = Column(Integer, ForeignKey('SimpleSpecies.Plant_id'))
    Image_url = Column(String(100))

#식물 샘플 이미지 경로 테이블
class MicroImage(Base):
    Image_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    Plant_id = Column(Integer, ForeignKey('SimpleSpecies.Plant_id'))
    Image_url = Column(String(100))
