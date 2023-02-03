from typing import TYPE_CHECKING

from sqlalchemy import Column,Integer, String,ForeignKey,TEXT,Index,DateTime
from sqlalchemy.orm import relationship
from db.session import engine
from db.base_class import Base


class Genus(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    genus = Column(String(50))
    family = Column(String(50))

class Species(Base):
    plantno = Column(Integer, primary_key=True)
    species = Column(String(50))
    genus = Column(String(50))


#식물 샘플 이미지 경로 테이블
class Samplepath(Base):
    plantno = Column(Integer, ForeignKey('species.plantno'), primary_key=True)
    path = Column(String(100))
    
class Overview(Base):
    plantno = Column(Integer,ForeignKey('species.plantno') , primary_key=True )
    overview = Column(TEXT)

class Lifetime(Base):
    plantno = Column(Integer,ForeignKey('species.plantno') , primary_key=True )
    describe = Column(String(50))       #잎이 있는 기간, 꽃이 있는 기간 등등 규칙에 맞게 설명을 쓴다.
    start = Column(DateTime)    # 기간의 시작 월, 일.
    end = Column(DateTime)      # 기간의 끝 월, 일.

class Micropath(Base):
    plantno = Column(Integer, ForeignKey('species.plantno'), primary_key=True )
    path = Column(String(100))



#자동으로 DB의 table을 생성하는 것.
Base.metadata.create_all(bind=engine)