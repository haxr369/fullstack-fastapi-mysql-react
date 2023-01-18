from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.img import Img_Model
from schemas.img_sch import ImgCreate,ImgUpdate


class CRUDImg(CRUDBase[Img_Model, ImgCreate, ImgUpdate]):
    def create_with_ip(
        self, db: Session, *, obj_in: ImgCreate
    ) -> Img_Model:
        obj_in_data = jsonable_encoder(obj_in)
        print(obj_in_data)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

   


img = CRUDImg(Img_Model)