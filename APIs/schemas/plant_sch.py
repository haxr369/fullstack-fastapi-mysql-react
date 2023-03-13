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
    Species_name : str = None
    Genus_name : str = None
    Family_name : str = None

class SimpleSpeciesSCHCreate(SimpleSpeciesSCH):
    pass


class SearchSCH(SimpleSpeciesSCHBase):
    Plant_sample : str


class DetailSpeciesSCHBase(BaseModel):
    Plant_id : Optional[int] = None
    #Species_name : Optional[str] = None
    Describe : Optional[str] = None
    Blossom : Optional[str] = None
    Flowers_fail : Optional[str] = None
    Bear_fruit : Optional[str] = None
    Bear_fail : Optional[str] = None

class DetailSpeciesSCH(DetailSpeciesSCHBase):
    Describe : str = None
    #Species_name : str = None
    Blossom : str = None
    Flowers_fail : str = None
    Bear_fruit : str = None
    Bear_fail : str = None


class DetailSpeciesSCHCreate(DetailSpeciesSCH):
    pass


