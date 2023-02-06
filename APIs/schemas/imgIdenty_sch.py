from typing import Optional

from pydantic import BaseModel, validator


# Shared properties
class ImgIdentyBase(BaseModel):
    Family: str
    Genus: str
    Species: str
    Percent: float
    PlantNo : str
    PlantImgs: list
   
    @validator("PlantImgs", pre=True)
    def check_images_path(cls, value):
        for path in value:
            if not path.endswith(('.jpeg', '.jpg', '.png')):
                raise ValueError(f"Invalid image path: {path}")
        return value

#aa = {"Family":"가사리","Genus": "이건뭐", "Species":"기지니", "percent":83.2}
#base= ImgIdentyBase(**aa)
#aa_sh = base(aa)
#print(base)

class TopModel(BaseModel):
    top1 : ImgIdentyBase
    top2 : ImgIdentyBase
    top3 : ImgIdentyBase

#top123 = {"top1":aa, "top2":aa,"top3":aa }
#print(top123)
#tops = TopModel(**top123)
#print(tops)

# Properties to receive via API on creation
class ImgIdentyCreate(ImgIdentyBase):
    pass

class TopModelCreate(TopModel):
    pass

