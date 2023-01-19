from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os
import shutil
from crud import crud_item,crud_img
import models.user
from schemas import item_sch, imgIdenty_sch
from api import deps
from core.config import settings
import json
router = APIRouter()



@router.get("/identy/{user_fileName}")
async def plant_identy(
    *,
    db: Session = Depends(deps.get_db),
    user_fileName: str,
) -> Any:
    
    """
    식별함수를 사용해야하지만 일단은 더미 파일을 사용한다.
    단, 스키마는 똑같이 사용함.
    식별함수의 결과는 딕셔너리 형식으로 나온다.
    result = inference(user_fileName) 딕셔너리 형식

    """

    result_url = "/code/app/dummy.json"

    with open(result_url, "r") as json_file:
        # Load the JSON data from the file
        result = json.load(json_file)

    top3_results = imgIdenty_sch.TopModel(**result['top3_plants'])
    #print(top3_results)
    top3_images = imgIdenty_sch.ImagesModel(**result['top3_images'])

    return {"user_url": result["Input_url"], "results":top3_results, "images":top3_images }

@router.get("/{id}", response_model= item_sch.Item)
def read_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get item by ID.
    """
    item = crud_item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item