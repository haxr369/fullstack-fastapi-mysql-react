from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field
from schemas.img_sch import ImageSchema

class LifeBase(BaseModel):
    describe : str = None
    start : datetime = None
    end : datetime = None

class Life(LifeBase):
    pass

# Shared properties
class PlantBase(BaseModel):
    plantNo :  Optional[int] = None
    species : Optional[str] = None
    genus : Optional[str] = None
    family : Optional[str] = None
    samples :  Optional[ImageSchema] = None
    overview : Optional[str] = None
    lifetime : Optional[List[Life]] = None
    micros :  Optional[ImageSchema] = None

class PlantUpdate(PlantBase):
    pass

class PlantCreate(PlantBase):
    pass
class Plant(PlantBase):
    pass

class PlantGenus(BaseModel):
    genus : str 
    family : str

class PlantSpecies(BaseModel):
    plantno : int 
    species : str
    genus : str 

class PlantSamples(BaseModel):
    plantno : int
    samples : ImageSchema

class PlantOverview(BaseModel):
    plantno : int
    overview : str

class PlantLifetime(PlantBase):
    plantno : int
    lifetime : List[Life]


class PlantMicros(PlantBase):
    plantno : int
    micros : ImageSchema

