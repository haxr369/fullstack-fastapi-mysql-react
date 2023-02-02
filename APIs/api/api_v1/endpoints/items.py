from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException,File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy.orm import Session
import os
from crud import crud_item,crud_img
import models.user
from schemas import item_sch, img_sch
from api import deps
from core.config import settings
import json
router = APIRouter()



@router.get("/apitest")
def read_items() -> Any:
    """
    Retrieve items.
    """
    items = {'good_job':"아리가토고자이마스!!!!!"}
    print(items)
    return items

@router.post('/userImgInfo')       #이미지 정보를 받아서 DB에 저장
async def create_upload_info(
    *,
    db: Session = Depends(deps.get_db),
    file_info : img_sch.ImgCreate
):
    crud = crud_img.img
    item = crud.create_with_ip(db=db, obj_in=file_info)
    return item 

@router.post('/userImg')            #이미지를 받아서 저장소에 저장
async def create_upload_file(
    *,
    file : UploadFile = File(...)
):
    
    contents = await file.read()
    print(file.filename)
    with open(os.path.join(settings.UPLOAD_DIRECTORY, file.filename), "wb") as fp:
        fp.write(contents)

    return 0

#사용자 사진을 전송하는 api
@router.get('/oneImg/{file_name}')
async def get_image_with_name(file_name: str) -> Any:

    std_url = os.path.join("/code/app/Uploaded_images/",file_name)
    #print(os.path.isfile(std_url))
    if os.path.isfile(std_url):
        return FileResponse(std_url, media_type="image/*")
    else:
        # FileNotFoundError
        return JSONResponse(content={"error": "Image not found."},  status_code=404)

#식물 샘플 사진을 전송하는 api
@router.get('/twoImg/{plantNo}/{file_name}')
async def get_image_with_url(plantNo:str, file_name: str) -> Any:

    std_url ="/code/app/Sample_images"
    file_url = os.path.join(std_url,plantNo, file_name)
    print(file_url)
    print(os.path.isfile(file_url))
    if os.path.isfile(file_url):
        return FileResponse(file_url, media_type="image/*")
    #else:
        # FileNotFoundError
    #    return JSONResponse(content={"error": "Image not found."},  status_code=404)



@router.post("/", response_model=item_sch.Item)
def create_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: item_sch.ItemCreate,
) -> Any:
    """
    Create new item.
    """
    item = crud_item.create_with_owner(db=db, obj_in=item_in)
    return item


@router.put("/{id}", response_model=item_sch.Item)
def update_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: item_sch.ItemUpdate,
) -> Any:
    """
    Update an item.
    """
    item = crud_item.get(db=db, id=id)

    item = crud_item.update(db=db, db_obj=item, obj_in=item_in)
    return item


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


@router.delete("/{id}", response_model= item_sch.Item)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an item.
    """
    item = crud_item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item = crud_item.remove(db=db, id=id)
    return item