from typing import TYPE_CHECKING

from sqlalchemy import Column,Integer, String,ForeignKey,TEXT,Index,DateTime
from sqlalchemy.orm import relationship
from db.session import engine
from db.base_class import Base
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

class SimpleSpecies(Base):
    Plant_id = Column(Integer, autoincrement=True, 
                                primary_key=True)
    Species_name = Column(String(255),  unique=True, 
                            primary_key=True, index=True)
    Genus_name = Column(String(255))
    Family_name = Column(String(255))

class DetailSpecies(Base):
    Plant_id = Column(Integer, autoincrement=True, 
                    primary_key=True, index=True)
    Species_name = Column(String(255),  
                    ForeignKey('simplespecies.Species_name'),  
                    unique=True, primary_key=True, index=True)
    Blossom = Column(Integer, default =0)
    Flowers_fail = Column(Integer, default =0)
    Bear_fruit = Column(Integer, default =0)
    Bear_fail = Column(Integer, default =0)
    Describe = Column(TEXT)



Base.metadata.create_all(bind=engine)



# 데이터 삽입


df = pd.read_excel('/code/app/plant_149_DB.xlsx')

#print(df.info())
simple_df = df.drop(['번호','Blossom','Flowers_fail','Bear_fruit','Bear_fail','Describe'],axis=1)
detail_df = df.drop(['번호','Genus_name','Family_name'],axis=1)

#print(simple_df.info())
#print(detail_df.info())

#df.to_sql(name='simplespecies', con=engine, if_exists='append', index=False)
Session = sessionmaker(bind=engine)
session = Session()

# 데이터프레임을 DB 테이블에 저장
for index, row in simple_df.iterrows():
    simple_species = SimpleSpecies(
        Species_name=row["Species_name"],
        Genus_name=row["Genus_name"],
        Family_name=row["Family_name"]
    )
    session.add(simple_species)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()


# 데이터프레임을 DB 테이블에 저장
for index, row in detail_df.iterrows():
    simple_species = DetailSpecies(
        Species_name=row["Species_name"],
        Blossom=row["Blossom"],
        Flowers_fail=row["Flowers_fail"],
        Bear_fruit=row["Bear_fruit"],
        Bear_fail=row["Bear_fail"],
        Describe=row["Describe"]
    )
    session.add(simple_species)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()

session.close()

