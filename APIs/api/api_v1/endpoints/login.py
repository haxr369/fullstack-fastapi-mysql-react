from datetime import datetime, timedelta 
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from schemas import token_sch, user_sch
from api import deps
from core.config import settings
from core import security
from crud import crud_user
import random
from models import user
from fastapi.encoders import jsonable_encoder


router = APIRouter()

#사용자에게 access token을 준다.
@router.post("/access-token", response_model=token_sch.Token)
def login_access_token(
    db: Session = Depends(deps.get_db) , form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """

    OAuth2 compatible token login, get an access token for future requests
    로그인하는 부분
    user = crud.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    """
    print("로그인 user 이름: ",{"grant_type":form_data.grant_type,
                                "username":form_data.username,
                                "password":form_data.password})
    crud = crud_user.jwtuser
    #DB에 username이 있는지 확인
    print("계정 생성 중")
    while(1):
        id =  random.randrange(1,100000)      
        exis = crud.get_datetime_by_username(db=db, id=id)
        if(not exis): break # 없는 경우에 while문 탈출

    createtime = datetime.now()

    #새로운 유저 정보를 저장
    userinfo = user_sch.JwtUserCreate(id=id, access=0 , createtime=createtime)
    print(userinfo)
    jwtUser = crud.create(db=db, obj_in=userinfo)

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            jwtUser["id"], expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

@router.post("/usetoken", response_model=user_sch.JwtUser)
def use_token(db: Session = Depends(deps.get_db), current_user: user.JwtUser = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    print("testing... ", current_user)
    
    crud = crud_user.jwtuser

    info = crud.get(db=db, id=current_user.id)

    jwtUser = crud.update(db=db, db_obj = info ,obj_in= {"access": current_user.access+1})

    response = user_sch.JwtUser(id=jwtUser.id, 
                            access=jwtUser.access, 
                            createtime=jwtUser.createtime)
    print(response)
    
    return response



@router.post("/test-token", response_model=user_sch.JwtUser)
def test_token(current_user: user.JwtUser = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    response = user_sch.JwtUser(id=current_user.id, 
                            access=current_user.access, 
                            createtime=current_user.createtime)
    print(response)
    
    return response

