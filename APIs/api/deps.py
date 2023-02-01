from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
#from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from jose import jwt
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

def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> user.JwtUser:
    try:
        print("현재 받은 토큰은? ",token)
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        print("해독한 결과? ",payload)
        token_data = token_sch.TokenPayload(**payload)
        print("완성!")
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    #int 형의 payload가 DB에 없으면 404가 뜬다.
    user = crud_user.jwtuser.get(db, id=token_data.sub)
    print("완성!!!!!!!!!",user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
