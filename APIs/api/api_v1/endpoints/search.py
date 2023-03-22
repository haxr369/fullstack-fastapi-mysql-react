from typing import Any, List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os
import shutil
from crud import crud_plant
from crud.base import CRUDBase
from models.plant import SimpleSpecies, DetailSpecies
from schemas.plant_sch import SimpleSpeciesSCH, DetailSpeciesSCH
from api import deps
from core.config import settings
import json
router = APIRouter()


@router.get("/searchquery" , response_model= List[SimpleSpeciesSCH])
def search_with_query(
    *,
    db: Session = Depends(deps.get_db),
    query: str):

    crud  = crud_plant.crud_SimpleSpecies

    results = crud.get_plants_by_query(db=db, query = query)

    for i in results:
        print(i.Species_name)
        
    return results

@router.get("/simpleinfo/{species}", response_model = SimpleSpeciesSCH)
def get_plant_simple(
    *,
    db: Session = Depends(deps.get_db),
    species : str
) :
    """
    식물 종 입력
    -> 식물의 간단 정보 전송.
    """
    print(species," 검색!!!")
    result = db.query(SimpleSpecies).filter(SimpleSpecies.Species_name == species).first()
    print(result.Plant_id, result.Genus_name)

    resultSCH = SimpleSpeciesSCH(
        Plant_id = result.Plant_id,
        Species_name = result.Species_name,
        Genus_name = result.Genus_name,
        Family_name = result.Family_name
    )
    return resultSCH

@router.get("/detailinfo", response_model = DetailSpeciesSCH)
def get_plant_detail(
    *,
    db: Session = Depends(deps.get_db),
    species : str
):
    """
    식물 종 입력
    -> 식물의 구체적 정보 전송.
    """
    print(species," 상세 검색!!!")
    try:
        crud  = crud_plant.crud_DetailSpecies

        results = crud.get_by_plant_species(db=db, species = species)
        return results
    except:
        raise HTTPException(status_code=404, detail="Plant Detail not found")

    

"""
@router.post("/info/species")
def get_plant_dictionary(
    *,
    db: Session = Depends(deps.get_db),
    species : str,
    obj : plant_sch.Species
) -> Any:

    crud = CRUDBase(plant.Species)
    db_obj = crud.create(db=db, obj_in=obj)
    
    return db_obj
"""




