from typing import Any, List

from fastapi import APIRouter,Form, Body, Depends, HTTPException,File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy.orm import Session
import os
from crud import crud_img, crud_plant, crud_user
import models.user
from schemas import item_sch, img_sch
from api import deps
from core.config import settings
import json
router = APIRouter()

"""
사용자 입력 사진이 1Mbyte가 넘는 경우 header 사이즈가 제한돼기 때문에 서버가 클라이언트의 요청을 받을 수 없다.
따라서 아래 설정으로 요청 헤더의 제한 크기를 4Mbyte로 늘릴 수 있다.
"""
MAX_SIZE = 5 * 1024 * 1024  # 5MB

@router.get("/apitest")
def read_items() -> Any:
    """
    Retrieve items.
    """
    items = {'good_job':"아리가토고자이마스!!!!!"}
    print(items)
    return items

@router.post('/uploadImg')            #이미지를 받아서 저장소에 저장
async def create_upload_file(
    *,
    file: UploadFile = File(...),
    UserNickName: str,
    db: Session = Depends(deps.get_db)
):
    try:
        contents = await file.read()
        #print(file.filename)
        filename = file.filename
        with open(os.path.join(settings.UPLOAD_DIRECTORY, filename), "wb") as fp:
            fp.write(contents)
        user_id = crud_user.user.get_by_nickname(db = db, nickname = UserNickName).User_id
        img_info = img_sch.UserImg(Image_url=filename, User_id=user_id)
        item = crud_img.user_img.create(db=db, obj_in=img_info)

        # 이미지 정보를 DB에 저장 
        # metadata에 유저 id를 포함하도록 수정 요청 일단은 999로 하드코딩.
        print("User_nickname : ",UserNickName)
        return item
        
    except Exception as e:
        print(f"Failed to read file: {e}")
        return None

    
    

    

#사용자 사진을 전송하는 api
@router.get('/userImg/{file_name}')
async def get_image_with_name(file_name: str) -> Any:

    std_url = os.path.join("/code/app/Uploaded_images/",file_name)
    #print(os.path.isfile(std_url))
    if os.path.isfile(std_url):
        return FileResponse(std_url, media_type="image/*")
    else:
        # FileNotFoundError
        return JSONResponse(content={"error": "Image not found."},  status_code=404)

#식물 샘플 사진을 전송하는 api
@router.get('/sampleImg/{Species}/{file_name}')
async def get_image_with_url(Species:str, file_name: str) -> Any:

    std_url = settings.SAMPLES_V1
    
    file_url = os.path.join(std_url,Species, file_name)
    print(file_url)
    print(os.path.isfile(file_url))
    if os.path.isfile(file_url):
        return FileResponse(file_url, media_type="image/*")
    else:
        FileNotFoundError
        return JSONResponse(content={"error": "Image not found."},  status_code=404)



"""@router.post("/", response_model=item_sch.Item)
def create_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: item_sch.ItemCreate,
) -> Any:
    
    #Create new item.
    
    item = crud_plant.create_with_owner(db=db, obj_in=item_in)
    return item"""


"""@router.put("/{id}", response_model=item_sch.Item)
def update_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: item_sch.ItemUpdate,
) -> Any:
    
    #Update an item.
    
    item = crud_plant.get(db=db, id=id)

    item = crud_plant.update(db=db, db_obj=item, obj_in=item_in)
    return item"""


"""@router.get("/{id}", response_model= item_sch.Item)
def read_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    
    #Get item by ID.
    
    item = crud_plant.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item"""


"""@router.delete("/{id}", response_model= item_sch.Item)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    
    #Delete an item.
    
    item = crud_plant.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item = crud_plant.remove(db=db, id=id)
    return item"""