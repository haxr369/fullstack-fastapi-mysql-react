from typing import Optional,TypeVar, Dict

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

# Shared properties
class UserListSCHBase(BaseModel):
    User_id : Optional[int] = None
    Createtime : Optional[datetime] = None
    Access_count : Optional[int] = 0
    Is_superuser: bool = False


# Properties to receive via API on creation
class UserListSCHCreate(UserListSCHBase):
    User_id : int = None
    createtime : datetime = None
    Access_count : int = 0
    Is_superuser: bool = False

# Properties to receive via API on update
class UserListSCHUpdate(UserListSCHBase):
    Access_count : int = 0



class UserInDBBase(UserListSCHBase):
    User_id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass

"""

T = TypeVar('T')


class Parameter(BaseModel):
    data: Dict[str, str] = None


class RequestSchema(BaseModel):
    parameter: Parameter = Field(...)


class ResponseSchema(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None

class TokenResponse(BaseModel) :
    access_token : str
    token_type :str


class JwtUserBase(BaseModel):
    id: Optional[str] = None
    access : Optional[int] = 0
    createtime: Optional[datetime] = None

class JwtUser(JwtUserBase):
    id: str = None

class JwtUserUpdate(JwtUserBase):
    access : int

# Properties to receive via API on creation
class JwtUserCreate(JwtUserBase):
    pass
"""