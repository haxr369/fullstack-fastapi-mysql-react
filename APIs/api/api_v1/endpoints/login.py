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
    """
    print("로그인 시작! ",form_data.username, form_data.password)
    user = crud_user.user.authenticate(
        db, nickname=form_data.username, password=form_data.password
    )
    print(user.User_nickname, user.User_password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    """
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    """
    
    #access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.User_nickname
        ),
        "token_type": "bearer",
    }


@router.post("/usetoken", response_model=user_sch.User)
def use_token(db: Session = Depends(deps.get_db), 
            current_user: Union[user.UserList, None] = Depends(deps.get_current_user)
            ) -> Any:
    """
    유효한 토큰을 가져오면 유저의 Access_count를 늘림.
    """
    print("testing... ", current_user)
    if(current_user): #정상적인 토큰을 가진 user인 경우
        crud = crud_user.user

        #info = crud.get(db=db, id=current_user.id)

        jwtUser = crud.update(db=db, db_obj = current_user ,
                            obj_in= {"Access_count": current_user.Access_count+1})

        response = user_sch.User(User_nickname=jwtUser.User_nickname, 
                                Access_count=jwtUser.Access_count, 
                                Createtime=jwtUser.Createtime)
        print(response)
        return response
        
    else: #만료된 토큰을 가진 user인 경우
        response = user_sch.User(User_id=-1, 
                                Access_count=0)
        print(response)
        return response




@router.get("/testToken", response_model=user_sch.UserShowSCH)
def test_token(current_user: Union[user.UserList, None] = Depends(deps.get_current_user)
            ) -> Any:
    """
    Test access token
    """
    if(current_user):
        response = user_sch.UserShowSCH(User_nickname = current_user.User_nickname, 
                                Access_count = current_user.Access_count)
        print(response)
        
        return response
    else: #만료된 토큰을 가진 user인 경우
        response = user_sch.UserShowSCH(User_nickname=-1, 
                                Access_count=0)
        print(response)
        return response