from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator
from fastapi import File, UploadFile
from datetime import datetime

class PlantImg(BaseModel):
    image_id: Optional[int] = None
    image_url : Optional[str] =None
    plant_id : Optional[int] = None

class UserImg(BaseModel):
    user_id: Optional[int] = None
    image_id : Optional[int] = None
    image_url : Optional[str] =None
    createtime : Optional[datetime] = None

# Properties to receive on item update
class PlantImgCreate(PlantImg):
    image_id: int = None
    image_url : str =None
    plant_id : int = None
    

# Properties to receive on item update
class PlantImgUpdate(PlantImgCreate):
    pass

# Properties to receive on item update
class UserImgCreate(UserImg):
    user_id: int = None
    image_id : int = None
    image_url : str =None

    

# Properties to receive on item update
class UserImgUpdate(UserImg):
    pass

class ImageSchema(BaseModel):
    plantImgs: list
   
    @validator("plantImgs", pre=True)
    def check_images_path(cls, value):
        for path in value:
            if not path.endswith(('.jpeg', '.jpg', '.png','.JPG','JPEG','PNG')):
                raise ValueError(f"Invalid image path: {path}")
        return value

class ImagesModel(BaseModel):
    top1 : ImageSchema
    top2 : ImageSchema
    top3 : ImageSchema