from fastapi import APIRouter, Depends
from schemas import user_sch
from sqlalchemy.orm import Session
from core.config import settings  #ACCESS_TOKEN_EXPIRE_MINUTES
from crud import crud_user
from models import user #jwtUser 사용.
from datetime import datetime, timedelta #datetime의 연산은 timedelta 클래스 객체로 반환됨.
import random
from api import deps

router = APIRouter()


#클라이언트에게 JWT 토큰을 제공한다.
@router.post('/login')
async def login( db: Session = Depends(deps.get_db)):
    try:
        crud = crud_user.jwtuser
        #DB에 username이 있는지 확인
        
        while(1):
            username =  random.randrange(1,100000)      
            exis = crud.get_datetime_by_username(db=db, username=username)
            if(not exis): break # 없는 경우에 while문 탈출
        createtime = datetime.now()

        #새로운 유저 정보를 저장
        userinfo = user_sch.JwtUserCreate({"username":username, "createtime":createtime})
        
        
        jwtUser = crud.create_with_ip(db=db, obj_in=userinfo)

        token = crud.JWTRepo.generate_token(jwtUser)
        return user_sch.ResponseSchema(code="200", 
                                status="OK", 
                                message="success login!", 
                                result=user_sch.TokenResponse(access_token=token, 
                                                        token_type="Bearer")).dict(exclude_none=True)
    except Exception as error:
        error_message = str(error.args)
        print(error_message)
        return user_sch.ResponseSchema(code="500", status="Internal Server Error", message="Internal Server Error").dict(exclude_none=True)
