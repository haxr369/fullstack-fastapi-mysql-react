"""from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import crud
from models import user
from schemas import user_sch
from api import deps
from core.config import settings"""
"""
router = APIRouter()


@router.get("/", response_model=List[user_sch.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    
) -> Any:
    
    #Retrieve users.
    
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model= user_sch.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: user_sch.UserCreate,       #이메일과 패스워드를 쿼리객체로 받는다.
    
) -> Any:
   
    #Create new user.
   
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:    #이미 DB에 이메일이 존재할 경우
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in) #user DB에 입력한 이메일과 패스워드를 저장한다.
    
    return user











@router.get("/{user_id}", response_model= user_sch.User)
def read_user_by_id(
    user_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    
    #Get a specific user by id.
   
    user = crud.user.get(db, id=user_id)

    return user


@router.put("/{user_id}", response_model= user_sch.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: user_sch.UserUpdate,
) -> Any:
    
    #Update a user.
    
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user"""