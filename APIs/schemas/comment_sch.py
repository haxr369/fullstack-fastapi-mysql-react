import datetime
from typing import Optional
from pydantic import BaseModel, validator
"""
댓글 데이터를 위한 api 스키마 구축
"""


class CommentCreateSCH(BaseModel):
    Content: str
    Compare_id: int

    @validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class CommentSCH(BaseModel):
    Comment_id: int
    Compare_id: int
    User_id: Optional[int] = None
    Content: str
    Create_date: datetime.datetime

    class Config:
        orm_mode = True


class CommentDeleteSCH(BaseModel):
    Comment_id: int


class CommentClearSCH(BaseModel):
    Compare_id: int
