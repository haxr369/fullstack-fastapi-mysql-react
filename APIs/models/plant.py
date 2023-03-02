from typing import TYPE_CHECKING

from sqlalchemy import Column,Integer, String,ForeignKey,TEXT,Index,DateTime
from sqlalchemy.orm import relationship
from db.session import engine
from db.base_class import Base




class SimpleSpecies(Base):
    Plant_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    Species_name = Column(String(50))
    Genus_name = Column(TEXT)
    Family_name = Column(Integer,ForeignKey('genus_family.id'))

class DetailSpecies(Base):
    Plant_id = Column(Integer,  primary_key=True, ForeignKey('SimpleSpecies.Plant_id'),  index=True)
    Blossom = Column(Integer, default =0)
    Flowers_fail = Column(Integer, default =0)
    Bear_fruit = Column(Integer, default =0)
    Bear_fail = Column(Integer, default =0)



