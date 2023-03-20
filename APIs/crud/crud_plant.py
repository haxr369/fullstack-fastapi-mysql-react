from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import or_
from crud.base import CRUDBase
from models.plant import SimpleSpecies, DetailSpecies
from schemas.plant_sch import SimpleSpeciesSCHCreate, DetailSpeciesSCHCreate, SearchSCH

#누가 넣었는지 알 필요가 있을까?...
class CRUDSimpleSpecies(CRUDBase[SimpleSpecies, SimpleSpeciesSCHCreate, SimpleSpeciesSCHCreate]):
    def create_with_species(
        self, db: Session, *, obj_in: SimpleSpeciesSCHCreate
    ) -> SimpleSpecies:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_plants_by_query(
        self, db: Session, *, query: str
    ) -> List[SimpleSpeciesSCHCreate]:

        searchResults = db.query(SimpleSpecies).filter(
            or_(
                SimpleSpecies.Species_name.ilike(f"%{query}%"),
                SimpleSpecies.Genus_name.ilike(f"%{query}%"),
                SimpleSpecies.Family_name.ilike(f"%{query}%")
            )
        ).all()

        result = [ SimpleSpeciesSCHCreate(Species_name= searchResult.Species_name,
                                            Genus_name= searchResult.Genus_name,
                                            Family_name = searchResult.Family_name )     
                        for searchResult in searchResults]

        return result 

    # 식물의 간단 정보 조회
    def get_by_plant_species(
        self, db: Session,*, species : str
    ) -> SimpleSpecies:
        species = db.query(SimpleSpecies).filter(SimpleSpecies.species_name == species).first()
        return species

    # 쿼리로 식물 검색하는 함수 넣을 예정

    def delete(self, db: Session, *, species_name: str) -> SimpleSpecies:
            obj = db.query(self.model).get(species_name)
            db.delete(obj)
            db.commit()
            return obj


crud_SimpleSpecies= CRUDSimpleSpecies(SimpleSpecies)

class CRUDDetailSpecies(CRUDBase[DetailSpecies, DetailSpeciesSCHCreate, DetailSpeciesSCHCreate]):
    def create(
        self, db: Session, *, obj_in: DetailSpeciesSCHCreate
    ) -> DetailSpecies:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # 식물의 세부 정보 조회
    def get_by_plant_species(
        self, db: Session,*, species : str
    ) -> DetailSpecies:
        species = db.query(DetailSpecies).filter(DetailSpecies.species_name == species).first()
        return species


    def delete(self, db: Session, *, species_name: str) -> DetailSpecies:
        obj = db.query(self.model).get(species_name)
        db.delete(obj)
        db.commit()
        return obj

        
crud_DetailSpecies= CRUDDetailSpecies(DetailSpecies)