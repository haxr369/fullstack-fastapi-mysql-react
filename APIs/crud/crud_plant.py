from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.plant import SimpleSpecies, DetailSpecies,
from schemas.plant_sch import SimpleSpeciesCreate, DetailSpeciesCreate

#누가 넣었는지 알 필요가 있을까?...
class CRUDSimpleSpecies(CRUDBase[SimpleSpecies, SimpleSpeciesCreate, SimpleSpeciesCreate]):
    def create_with_species(
        self, db: Session, *, obj_in: SpeciesCreate
    ) -> SimpleSpecies:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_Plant_id(
        self, db: Session,*, species : str
    ) -> Species:
        species = db.query(SimpleSpecies).filter(Species.Species_name == species).first()
        return species


crud_SimpleSpecies= CRUDSimpleSpecies(SimpleSpecies)

class CRUDDetailSpecies(CRUDBase[DetailSpecies, DetailSpeciesCreate, DetailSpeciesCreate]):
    def create_with_lifecycle(
        self, db: Session, *, obj_in: LifeCycleCreate
    ) -> DetailSpecies:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

crud_DetailSpecies= CRUDDetailSpecies(DetailSpecies)