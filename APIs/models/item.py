from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String,TEXT
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(1000), index=True)
    description = Column(TEXT, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")