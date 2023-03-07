from typing import TYPE_CHECKING

from sqlalchemy import Column,Integer, String,ForeignKey,TEXT,Index,DateTime
from sqlalchemy.orm import relationship
from db.session import engine
from db.base_class import Base




class SimpleSpecies(Base):
    Plant_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    Species_name = Column(String(50))
    Genus_name = Column(String(50))
    Family_name = Column(String(50))

class DetailSpecies(Base):
    Plant_id = Column(Integer,  ForeignKey('simplespecies.Plant_id'), primary_key=True , index=True)
    #Detail_id =  Column(Integer, primary_key=True, autoincrement=True, index=True)
    Blossom = Column(Integer, default =0)
    Flowers_fail = Column(Integer, default =0)
    Bear_fruit = Column(Integer, default =0)
    Bear_fail = Column(Integer, default =0)
    Describe = Column(TEXT)

Base.metadata.create_all(bind=engine)


