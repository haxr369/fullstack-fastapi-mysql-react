from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, BLOB
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Img_Model(Base):
    ip_name = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, index=True)
    send_time = Column(DateTime(timezone=True))
