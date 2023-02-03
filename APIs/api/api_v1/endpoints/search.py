from typing import Any, List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os
import shutil
from crud.base import CRUDBase
from models import plant
from schemas import plant_sch
from api import deps
from core.config import settings
import json
router = APIRouter()



@router.get("/search/{plantspecies}") #, response_model= item_sch.Item)
def read_hierarchy(
    *,
    db: Session = Depends(deps.get_db),
    plantspecies : str,
) -> Any:
    """
    식물 종을 입력
    여러 정보를 출력
    """
    
    return 0

@router.get("/info/{species}")
def get_plant_dictionary(
    *,
    db: Session = Depends(deps.get_db),
    species : str
) -> Any:
    """
    1. 종으로 속과 plantNo를 얻음.
    2. 속으로 과를 얻음.
    3. plantNo로 samples, overview, lifetime, 그리고 micros를 얻음.
    """
    print(species," 검색!!!")
    result = db.query(plant.Species).filter(plant.Species.species == species).first()
    print(result.plantno, result.genus)

    return 0

@router.post("/info/species")
def get_plant_dictionary(
    *,
    db: Session = Depends(deps.get_db),
    species : str,
    obj : plant_sch.PlantSpecies
) -> Any:
    """
    1. 종으로 속과 plantNo를 얻음.
    2. 속으로 과를 얻음.
    3. plantNo로 samples, overview, lifetime, 그리고 micros를 얻음.
    """
    crud = CRUDBase(plant.Species)
    db_obj = crud.create(db=db, obj_in=obj)
    
    return db_obj





