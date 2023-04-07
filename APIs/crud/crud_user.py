from typing import Any, Dict, Optional, Union, TypeVar, Generic, Optional

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.user import UserList
from schemas.user_sch import UserListSCHCreate, UserListSCHUpdate, UserShowSCH
from core.security import get_password_hash, verify_password



class CRUDUser(CRUDBase[UserList, UserListSCHCreate, UserListSCHUpdate]):
    def is_superuser(self, user: UserList) -> bool:
        return UserList.Is_Superuser

    #C
    def create(self, db: Session, *, obj_in: UserListSCHCreate) -> UserList:
        db_obj = UserList(
            User_id = obj_in.User_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    #R
    def get_by_nickname(self, db: Session, *, nickname: str
        ) -> UserList:
        user = db.query(UserList).filter(UserList.User_nickname == nickname).first()
        return user

    #U
    def update(
        self, db: Session, *, db_obj: UserList, obj_in: Union[UserListSCHUpdate, Dict[str, Any]]
    ) -> UserList:
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

    #사용자 비밀번호 인증
    def authenticate(self, db: Session, *, nickname: str, password: str) -> Optional[UserList]:
        user = self.get_by_nickname(db, nickname=nickname)
        if(user):
            print("유저 확인 비번 체크 시작!")
        if not user:
            return None
        if not verify_password(password, user.User_password): #DB 속 유저 pwd와 입력 pwd를 비교
            return None
        return user
    



user = CRUDUser(UserList)

