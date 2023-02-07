from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator
from fastapi import File, UploadFile


class PlantImg(BaseModel):
    id: Optional[int] = None
    path : Optional[str] =None
    plantno : int = None

class UserImg(BaseModel):
    id: Optional[int] = None
    path : Optional[str] =None
    user_id : int = None

# Properties to receive on item update
class PlantImgCreate(PlantImg):
    pass
# Properties to receive on item update
class PlantImgUpdate(PlantImg):
    pass

# Properties to receive on item update
class UserImgCreate(UserImg):
    pass
# Properties to receive on item update
class UserImgUpdate(UserImg):
    pass

class ImageSchema(BaseModel):
    plantImgs: list
   
    @validator("plantImgs", pre=True)
    def check_images_path(cls, value):
        for path in value:
            if not path.endswith(('.jpeg', '.jpg', '.png')):
                raise ValueError(f"Invalid image path: {path}")
        return value

class ImagesModel(BaseModel):
    top1 : ImageSchema
    top2 : ImageSchema
    top3 : ImageSchema