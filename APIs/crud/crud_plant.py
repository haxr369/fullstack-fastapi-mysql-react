from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.plant import Species, Genus_family, Lifecycle
from schemas.plant_sch import SpeciesCreate, Genus_familyCreate, LifeCycleCreate

#누가 넣었는지 알 필요가 있을까?...
class CRUDSpecies(CRUDBase[Species, SpeciesCreate, SpeciesCreate]):
    def create_with_species(
        self, db: Session, *, obj_in: SpeciesCreate
    ) -> Species:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_plantno(
        self, db: Session,*, species : str
    ) -> Species:
        species = db.query(Species).filter(Species.species == species).first()
        return species

class CRUDGenus_family(CRUDBase[Genus_family, Genus_familyCreate, Genus_familyCreate]):
    def create_with_genus(
        self, db: Session, *, obj_in: Genus_familyCreate
    ) -> Genus_family:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
        
crud_genus_family = CRUDGenus_family(Genus_family)

class CRUDLifecycle(CRUDBase[Lifecycle, LifeCycleCreate, LifeCycleCreate]):
    def create_with_lifecycle(
        self, db: Session, *, obj_in: LifeCycleCreate
    ) -> Lifecycle:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    

crud_lifecycle= CRUDLifecycle(Lifecycle)