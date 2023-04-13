import datetime
from typing import Optional
from pydantic import BaseModel, validator
"""
식물 비교 페이지를 위한 api 스키마 구축
"""


class PlantCompareCreateSCH(BaseModel):
    Tip: str
    Left_Species_name: str
    Right_Species_name: str
    Title: Optional[str] = None

    @validator('Tip', 'Right_Species_name', 'Left_Species_name')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @validator('Right_Species_name')
    def compare_match(cls, v, values):
        if 'Left_Species_name' in values and v == values['Left_Species_name']:
            raise ValueError('비교할 식물이 똑같습니다')
        return v


class PlantCompareSCH(BaseModel):
    Compare_id: int
    Left_Species_name: str
    Right_Species_name: str
    Title: str
    Tip: str

    class Config:
        orm_mode = True


class PlantCompareDeleteSCH(BaseModel):
    Compare_id: int
