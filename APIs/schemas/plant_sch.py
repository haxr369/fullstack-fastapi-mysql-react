from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field
from schemas.img_sch import ImageSchema



# Shared properties
class SimpleSpeciesSCHBase(BaseModel):
    Plant_id :  Optional[int] = None
    Species_name : Optional[str] = None
    Genus_name : Optional[str] = None
    Family_name : Optional[str] = None

class SimpleSpeciesSCH(SimpleSpeciesSCHBase):
    pass

class SimpleSpeciesSCHCreate(SimpleSpeciesSCHBase):
    pass


class DetailSpeciesSCHBase(BaseModel):
    Plant_id : Optional[int] = None
    Describe : Optional[str] = None
    Blossom : Optional[str] = None
    Flowers_fail : Optional[str] = None
    Bear_fruit : Optional[str] = None
    Bear_fail : Optional[str] = None

class DetailSpeciesSCH(DetailSpeciesSCHBase):
    pass
class DetailSpeciesSCHCreate(DetailSpeciesSCHBase):
    pass


