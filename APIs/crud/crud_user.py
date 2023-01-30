from typing import Any, Dict, Optional, Union, TypeVar, Generic, Optional

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.user import User, jwtUser
from schemas.user_sch import UserCreate, UserUpdate, JwtUserCreate


from datetime import datetime, timedelta
from jose import JWTError, jwt
from core.config import settings #import SECRET_KEY, ALGORITHM

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser(User)


class CRUDJwtUser(CRUDBase[jwtUser, JwtUserCreate, UserUpdate]):
    def get_datetime_by_username(self, db: Session, *, username: str) -> Optional[jwtUser]:
        return db.query(jwtUser).filter(jwtUser.username == username).first()

    def create(self, db: Session, *, obj_in: JwtUserCreate) -> jwtUser:
        db_obj = jwtUser(
            username = obj_in.username,
            createtime = obj_in.createtime
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, obj_in: str):
        db.delete(obj_in.username)
        db.commit()



jwtuser = CRUDJwtUser(User)


T = TypeVar('T')


class JWTRepo():

    def generate_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        
        return encode_jwt

    def decode_token(token: str):
        try:
            decode_token = jwt.decode(token, settings.SECRET_KEY, algorithm=[settings.ALGORITHM])
            return decode_token if decode_token["expires"] >= datetime.time() else None
        except:
            return{}

repository = JWTRepo()

class JWTBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)

        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication sheme.")
            if self.verfity_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expiredd token.")
            return credentials.credentials
        else:
            raise HTTPException(
                status=403, detail="Invalid authorization code.")

    def verfity_jwt(Self, jwttoken: str):
        isTokenValid: bool = False

        try:
            payload = jwt.decode(jwttoken, settings.SECRET_KEY, algorithm=[settings.ALGORITHM])
        except:
            payload = None

        if payload:
            isTokenValid = True
        return isTokenValid