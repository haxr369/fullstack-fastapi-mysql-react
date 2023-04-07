
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

#from database import get_db
#from domain.plantcompare import plantcompare_crud, plantcompare_schema
from models.compare import PlantCompare
from schemas.plantcompare_sch import PlantCompareCreateSCH, PlantCompareDeleteSCH,PlantCompareSCH
from crud import crud_plantcompare
#from domain.comment.comment_schema import Comment
from typing import List
from api.deps import get_db

router = APIRouter()

#두 식물을 비교하는 팁을 Create <관리자용>
@router.post("/create", response_model=PlantCompareSCH)
def create_compare(_PlantCompare_create: PlantCompareCreateSCH,
                   db: Session = Depends(get_db)):

    compare = crud_plantcompare.create_compare(
        db, PlantCompare_create=_PlantCompare_create)  # user는 일단 제외했음

    #model과 schema가 동일하기 때문에 response model이 스키마지만 모델 객체를 출력할 수 있다.
    return compare

#식물 비교 리스트
@router.get("/list", response_model=List[PlantCompareSCH])
def read_compare_list(db: Session = Depends(get_db)):
    _compare_list = crud_plantcompare.get_compare_list(db)
    return _compare_list

#두 식물을 비교하는 팁을 Read
@router.get("/detail/{Compare_id}", response_model=PlantCompareSCH)
def read_compare(Compare_id: int, 
                db: Session = Depends(get_db)):

    compare = crud_plantcompare.get_compare(db, Compare_id=Compare_id)
    return compare


#두 식물을 비교하는 팁 삭제 <관리자용>
"""
@router.delete("/delete/", status_code=status.HTTP_204_NO_CONTENT)
def delete_compare(_Compare_delete: PlantCompareDeleteSCH,
                   db: Session = Depends(get_db)):
    db_compare = crud_plantcompare.get_compare(
        db, Compare_id=_Compare_delete.Compare_id)
    if not db_compare:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")

    crud_plantcompare.delete_compare(db=db, db_compare=db_compare)
"""
# Compare와 연결된 모든 Comment 데이터를 가져오는 API 라우터

# #두 식물을 비교하는 팁과 관련한 댓글을 Read
# 일반 비교 팁만 테스트
"""
@router.get("/{Compare_id}/comments", response_model=List[CommentSCH])
def read_comments_by_compare_id(Compare_id: int, db: Session = Depends(get_db)):
    db_compare = crud_plantcompare.get_compare(db, Compare_id=Compare_id)
    if not db_compare:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="해당 Compare를 찾을 수 없습니다.")

    return crud_plantcompare.get_comments(db, Compare_id)
"""