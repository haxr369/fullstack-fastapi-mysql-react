from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os
import shutil
from crud import crud_img, crud_plant
import models.user
from schemas import item_sch, imgIdenty_sch
from api import deps
from core.config import settings
import json
from ML.MAE_serve_v1 import MAE_Model, inference

router = APIRouter()

def convert_size(size_bytes):
    import math
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


@router.get("/identy/{user_fileName}")
async def plant_identy(
    *,
    db: Session = Depends(deps.get_db),
    user_fileName: str,
) -> Any:
    print("들어온 file이름: "+user_fileName)
    """
    식별함수를 사용해야하지만 일단은 더미 파일을 사용한다.
    단, 스키마는 똑같이 사용함.
    식별함수의 결과는 딕셔너리 형식으로 나온다.
    result = inference(user_fileName) 딕셔너리 형식
    result_url = "/code/app/dummy.json"
    
    with open(result_url, "r") as json_file:
        # Load the JSON data from the file
        result = json.load(json_file)
    """
    std_url = os.path.join("/code/app/Uploaded_images/",user_fileName)

    results = inference(MAE_Model, std_url)

    file_size = os.path.getsize(std_url)
    print('File Size:', convert_size(file_size), 'bytes')

    for top , value in results.items():
        PlantNo = value['PlantNo'] #int형
        #PlantNo로 top1~3의 family, genus를 추가
        results[top]['Family'] = top+"의_과"
        results[top]['Genus'] = top+"의_속"
    print("results test '\n",results)
    top3_results = imgIdenty_sch.TopModel(**results)
    return {"results":top3_results}

@router.get("/{id}", response_model= item_sch.Item)
def read_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get item by ID.
    """
    item = crud_plant.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item