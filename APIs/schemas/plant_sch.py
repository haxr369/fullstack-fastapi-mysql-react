from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field
from schemas.img_sch import ImageSchema



# Shared properties
class SpeciesBase(BaseModel):
    plantno :  Optional[int] = None
    species : Optional[str] = None
    overview : Optional[str] = None
    genus_id : Optional[int] = None

class Species(SpeciesBase):
    pass

class Genus_familyBase(BaseModel):
    id : Optional[int] = None
    genus : Optional[str] = None
    family : Optional[str] = None

class Genus_family(Genus_familyBase):
    pass

class LifeCycleBase(BaseModel):
    id : Optional[int] = None
    plantno : Optional[int] = None
    describe : Optional[str] = None
    start : Optional[datetime] = None
    end : Optional[datetime] = None

class LifeCycle(LifeCycleBase):
    pass



