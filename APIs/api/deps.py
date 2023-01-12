from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
#from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

import crud, schemas
from models import user
from core.config import settings
from db.session import SessionLocal



def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


