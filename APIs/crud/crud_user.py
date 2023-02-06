from typing import Any, Dict, Optional, Union, TypeVar, Generic, Optional

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.user import User
from schemas.user_sch import UserCreate, UserUpdate


"""
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

"""

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def is_superuser(self, user: User) -> bool:
        return user.is_superuser
    #C
    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            id = obj_in.id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return {"id":obj_in.id}

    #R
    def get_by_id(self, db: Session, *, id: str) -> Optional[User]:
        return db.query(User).filter(User.id == id).first()

    #U
    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        updated = super().update(db, db_obj=db_obj, obj_in=update_data)
        return updated

    #D
    def delete(self, db: Session, *, obj_in: str):
        db.delete(obj_in.id)
        db.commit()



user = CRUDUser(User)


T = TypeVar('T')

"""
class JWTRepo():

    def generate_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)  #토큰이 15분 후 삭제된다.
        to_encode.update({"exp": expire})
        token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        
        return token

    def decode_token(token: str):
        try:
            print("토큰 해독 중")
            decode_token = jwt.decode(token, settings.SECRET_KEY, algorithm=[settings.ALGORITHM])
            print("토큰 해독 완료", decode_token)
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
        return isTokenValid"""