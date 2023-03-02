from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.img import UserImage, SampleImage, MicroImage
from schemas.img_sch import PlantImgCreate, UserImgCreate


class CRUDUserImg(CRUDBase[UserImage, UserImgCreate, UserImgCreate]):
    def create(
        self, db: Session, *, obj_in: UserImgCreate
    ) -> UserImage:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

user_img = CRUDUserImg(UserImage)

class CRUDSampleImg(CRUDBase[SampleImage, PlantImgCreate, PlantImgCreate]):
    def create(
        self, db: Session, *, obj_in: PlantImgCreate
    ) -> SampleImage:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

sample_img = CRUDSampleImg(SampleImage)   

class CRUDMicroImg(CRUDBase[MicroImage, PlantImgCreate, PlantImgCreate]):
    def create(
        self, db: Session, *, obj_in: PlantImgCreate
    ) -> MicroImage:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
        
micro_img = CRUDMicroImg(MicroImage)   
   


