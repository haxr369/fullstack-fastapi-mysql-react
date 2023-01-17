from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from fastapi import File, UploadFile

# Shared properties
class ImgBase(BaseModel):
    ip_name: str = None
    file_name: str = None

# Properties to receive on item update
class ImgCreate(ImgBase):
    pass


# Properties to receive on item update
class ImgUpdate(ImgBase):
    pass

# Properties shared by models stored in DB
class ImgInDBBase(ImgBase):
    ip_name : int
    file_name : str
    send_time: datetime = Field(default_factory=datetime.now)
    
# Properties to return to client
class Img(ImgInDBBase):
    pass

# Properties properties stored in DB
class ImgInDB(ImgInDBBase):
    pass