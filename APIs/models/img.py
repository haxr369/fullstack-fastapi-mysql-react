from typing import TYPE_CHECKING
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, BLOB
from sqlalchemy.orm import relationship
from db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class user_imgs(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    path = Column(String(100))
    send_time = Column(DateTime, default=datetime.datetime.now())

#식물 샘플 이미지 경로 테이블
class Sample_imgs(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    plantno = Column(Integer, ForeignKey('species.plantno'))
    path = Column(String(100))

class Micro_imgs(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    plantno = Column(Integer, ForeignKey('species.plantno'))
    path = Column(String(100))