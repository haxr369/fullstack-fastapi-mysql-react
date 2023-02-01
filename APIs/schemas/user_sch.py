from typing import Optional,TypeVar, Dict

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str




# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str

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

"""class TokenResponse(BaseModel) :
    access_token : str
    token_type :str"""


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
