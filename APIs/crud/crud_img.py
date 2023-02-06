from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.img import User_imgs, Sample_imgs, Micro_imgs
from schemas.img_sch import PlantImgCreate, UserImgCreate


class CRUDUserImg(CRUDBase[User_imgs, UserImgCreate, UserImgCreate]):
    def create(
        self, db: Session, *, obj_in: UserImgCreate
    ) -> User_imgs:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

crud_user_img = CRUDUserImg()

class CRUDSampleImg(CRUDBase[Sample_imgs, PlantImgCreate, PlantImgCreate]):
    def create(
        self, db: Session, *, obj_in: PlantImgCreate
    ) -> Sample_imgs:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
crud_sample_img = CRUDSampleImg()    
class CRUDMicroImg(CRUDBase[Micro_imgs, PlantImgCreate, PlantImgCreate]):
    def create(
        self, db: Session, *, obj_in: PlantImgCreate
    ) -> Micro_imgs:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
crud_micro_img = CRUDMicroImg()   
   


