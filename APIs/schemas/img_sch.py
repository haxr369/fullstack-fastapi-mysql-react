from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator
from fastapi import File, UploadFile
from datetime import datetime

class PlantImg(BaseModel):
    Image_id: Optional[int] = None
    Image_url : Optional[str] =None
    Plant_id : Optional[int] = None

class UserImg(BaseModel):
    User_id: Optional[int] = None
    Image_id : Optional[int] = None
    Image_url : Optional[str] =None
    Send_time : Optional[datetime] = None

# Properties to receive on item update
class PlantImgCreate(PlantImg):
    Image_id: int = None
    Image_url : str =None
    Plant_id : int = None
    

# Properties to receive on item update
class PlantImgUpdate(PlantImgCreate):
    pass

# Properties to receive on item update
class UserImgCreate(UserImg):
    User_id: int = None
    Image_id : int = None
    Image_url : str =None

    

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