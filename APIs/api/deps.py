from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
#from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from jose import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from models import user
from schemas import token_sch
from crud import crud_user
from core.config import settings
from core import security
from db.session import SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"http://192.168.0.203:8005{settings.API_V1_STR}/login/access-token"
)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        
        yield db
    finally:
        db.close()

#get_current_user를 할 때마다 새로운 토큰을 부여받는다???
"""
def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) :
    try:
        print("현재 받은 토큰은? ",token)
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[security.ALGORITHM]
        )
        
        #options={"verify_exp": True},
        print("해독한 결과? ",payload)
        token_data = token_sch.TokenPayload(**payload)
        #print("완성!")
    
    except (jwt.JWTError,  ValidationError, ExpiredSignatureError): #유효기간을 초과한 토큰을 받은 경우.
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    
    except (jwt.JWTError,ExpiredSignatureError):
        print("유효기간 만료")
        return None
    
    #int 형의 payload가 DB에 없으면 404가 뜬다.
    user = crud_user.user.get_by_id(db, id=token_data.sub)
    print("완성!!!!!!!!!",user)
    if not user:
        print("존재하지 않는 유저 "+token_data )
        raise HTTPException(status_code=404, detail="User not found")
    return user
"""
def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> user.UserList:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        print(payload['exp'],type(payload['exp']) )
        token_data = token_sch.TokenPayload(exp = payload['exp'],
                                            sub = payload['sub'])

    except (InvalidSignatureError):
        print("토큰 서명에 문제가 발견.")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    except (ExpiredSignatureError):
        print("토큰 유효기간 만료")
        return None

    except (jwt.JWTError):
        print("JWT Error")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    except (ValidationError):
        print("기타 에러 발생")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud_user.user.get_by_nickname(db, nickname=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
