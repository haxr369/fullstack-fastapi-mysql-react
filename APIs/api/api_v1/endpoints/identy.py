from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import crud
from models import user
from schemas import user_sch
from api import deps
from core.config import settings

router = APIRouter()

#사용자 이미지 url file system에 저장하고, DB에 url 저장.
"""
필요한 것.
1. image url 스키마  [사용자ID, imgUrl, 시간]
2. image DB model
3. CRUD.img 객체
""" 
@router.post("/", response_model= user_sch.User)   
def upload_image(
    *,
    db: Session = Depends(deps.get_db),
    user_in: user_sch.UserCreate,       #이메일과 패스워드를 쿼리객체로 받는다.
    
) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:    #이미 DB에 이메일이 존재할 경우
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in) #user DB에 입력한 이메일과 패스워드를 저장한다.
    
    return user