from datetime import datetime, timedelta 
from typing import Any,Union

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
def give_access_token(
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
    crud = crud_user.user
    #DB에 username이 있는지 확인
    print("계정 생성 중")
    while(1):
        id =  random.randrange(1,100000)      
        exis = crud.get_by_id(db=db, id=id)
        if(not exis): break # 없는 경우에 while문 탈출
    createtime = datetime.now()

    #새로운 유저 정보를 저장
    userinfo = user_sch.UserListSCHCreate(user_id=id)
    
    userinfo = crud.create(db=db, obj_in=userinfo)
    print(userinfo)
    
    return {
        "access_token": security.create_access_token(
            userinfo["User_id"]
        ),
        "token_type": "bearer",
    }

@router.post("/usetoken", response_model=user_sch.User)
def use_token(db: Session = Depends(deps.get_db), current_user: Union[user.UserList, None] = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    print("testing... ", current_user)
    if(current_user): #정상적인 토큰을 가진 user인 경우
        crud = crud_user.user

        #info = crud.get(db=db, id=current_user.id)

        jwtUser = crud.update(db=db, db_obj = current_user ,obj_in= {"access_count": current_user.access+1})

        response = user_sch.User(user_id=jwtUser.id, 
                                access_count=jwtUser.access, 
                                createtime=jwtUser.createtime)
        print(response)
        
        return response
        
    else: #만료된 토큰을 가진 user인 경우
        response = user_sch.User(user_id=-1, 
                                access=0)
        print(response)
        
        return response




@router.get("/testToken", response_model=user_sch.User)
def test_token(current_user: Union[user.User, None] = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    if(current_user):
        response = user_sch.User(id=current_user.id, 
                                access=current_user.access, 
                                createtime=current_user.createtime)
        print(response)
        
        return response
    else: #만료된 토큰을 가진 user인 경우
        response = user_sch.User(id=-1, 
                                access=0)
        print(response)
        
        return response

