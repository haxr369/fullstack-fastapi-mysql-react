from typing import TYPE_CHECKING

from sqlalchemy import Column,Integer, String,ForeignKey,TEXT,Index,DateTime
from sqlalchemy.orm import relationship
from db.session import engine
from db.base_class import Base
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime

class PlantCompare(Base):
    Compare_id = Column(Integer, autoincrement=True, 
                                primary_key=True, index=True)
    Left_Species_name = Column(String(255))
    Right_Species_name = Column(String(255))
    Title = Column(String(255))
    Tip = Column(TEXT)

class CompareComment(Base):
    Comment_id = Column(Integer, autoincrement=True, 
                    primary_key=True, index=True)
    Compare_id = Column(Integer,  
                    ForeignKey('plantcompare.Compare_id'))
    Contents = Column(TEXT)
    Write_time = Column(DateTime, default=datetime.datetime.now())

Base.metadata.create_all(bind=engine)