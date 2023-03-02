from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field
from schemas.img_sch import ImageSchema



# Shared properties
class SimpleSpeciesSCHBase(BaseModel):
    plant_id :  Optional[int] = None
    species_name : Optional[str] = None
    genus_name : Optional[str] = None
    family_name : Optional[str] = None

class SimpleSpeciesSCH(SimpleSpeciesSCHBase):
    pass

class SimpleSpeciesSCHCreate(SimpleSpeciesSCHBase):
    pass


class DetailSpeciesSCHBase(BaseModel):
    plant_id : Optional[int] = None
    describe : Optional[str] = None
    blossom : Optional[str] = None
    flowers_fail : Optional[str] = None
    Bear_fruit : Optional[str] = None
    Bear_fail : Optional[str] = None

class DetailSpeciesSCH(DetailSpeciesSCHBase):
    pass
class DetailSpeciesSCHCreate(DetailSpeciesSCHBase):
    pass


