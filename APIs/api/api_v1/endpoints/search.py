from typing import Any, List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException
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



@router.get("/search/{query}" , response_model= List[SimpleSpeciesSCH])
def search_with_query(
    *,
    db: Session = Depends(deps.get_db),
    query : str):

    """
    검색어를 입력
    -> 연관 식물들을 리스트로 전송.

    plants = crud.get_plants_by_query(db, query=query)
    if not plants:
        raise HTTPException(status_code=404, detail="검색 결과가 없습니다.")
    return plants
    """
    crud  = crud_plant.crud_SimpleSpecies

    results = crud.get_plants_by_query(query = query)

    print(results)
    
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

    return result

@router.get("/detailinfo/{species}")
def get_plant_detail(
    *,
    db: Session = Depends(deps.get_db),
    species : str
)->Any:
    """
    식물 종 입력
    -> 식물의 구체적 정보 전송.
    """
    print(species," 검색!!!")
    results = db.query(SimpleSpecies, DetailSpecies).filter(SimpleSpecies.Species_name == species_name, 
                            SimpleSpecies.Plant_id == DetailSpecies.Plant_id).all()

    for result in results:
        simple_species = result[0]
        detail_species = result[1]
        print(simple_species.Plant_id, simple_species.Genus_name)

    return results

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




