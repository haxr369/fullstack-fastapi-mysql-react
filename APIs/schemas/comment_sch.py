from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator
"""
댓글 데이터를 위한 api 스키마 구축
"""



"""
@validator('content')
def not_empty(cls, v):
    if not v or not v.strip():
        raise ValueError('빈 값은 허용되지 않습니다.')
    return v
"""

class CommentSCH(BaseModel):
    Comment_id: Optional[int] = None
    Compare_id: Optional[int] = None
    User_id: Optional[int] = None
    Content: Optional[str] = None
    Write_time: Optional[datetime] = None

    class Config:
        orm_mode = True

class CommentCreateSCH(CommentSCH):
    Compare_id: int
    User_id: int = None
    Contents: str

class CommentDeleteSCH(BaseModel):
    Comment_id: int
    User_id : int 


class CommentClearSCH(BaseModel):
    Compare_id: int
