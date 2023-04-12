
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from typing import List, Union, Any
from models import user
from models.compare import PlantCompare
from schemas.comment_sch import CommentCreateSCH,CommentSCH,CommentDeleteSCH,CommentClearSCH
from schemas.user_sch import UserShowSCH
from crud.crud_comment import comment_crud
from api import deps

router = APIRouter()

#식물 비교 팁에대한 댓글을 Create <일반용>
@router.post("/create", response_model = CommentSCH)
def create_comment(_Comment_create: CommentCreateSCH,
        db: Session = Depends(deps.get_db),
        current_user: Union[user.UserList, None] = Depends(deps.get_current_user) ):

    if (current_user==None):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="you are not our user",
        )
    else:
        rep = comment_crud.create_comment(
            db = db, Comment_create=_Comment_create, User_id = current_user.User_id )  # user는 일단 제외했음
        return rep

"""
단순히 댓글만 리스트로 출력하는 건 의미 없음.
@router.get("/list", response_model=List[CommentSCH])
def read_comment_list(db: Session = Depends(get_db)):
    _comment_list = crud_comment.get_comment_list(db)
    return _comment_list
"""

#비교 페이지에 맞는 댓글 리스트를 불러옴.
@router.get("/list/{Compare_id}", response_model=List[CommentSCH])
def read_comment_list(Compare_id: int, db: Session = Depends(deps.get_db)):
    _comment_list = comment_crud.get_comments_by_compare(db= db, Compare_id = Compare_id)
    return _comment_list

"""
댓글 하나만 가져오는 건 없어도 될 것 같다.
@router.get("/detail/{Comment_id}", response_model=CommentSCH)
def read_comment(Comment_id: int, db: Session = Depends(deps.get_db)):
    comment = comment_crud.get_comment(db, Comment_id=Comment_id)
    return comment
"""

#삭제 API는 사용자 인증등 추가할 부분이 있다. 일단 주석처리
@router.delete("/delete")
def delete_comment(_Comment_delete: CommentDeleteSCH,
                  db: Session = Depends(deps.get_db),
                  current_user: Union[user.UserList, None] = Depends(deps.get_current_user)
                  )-> dict:
    #현재 유저가 정상적인 유저인지 확인
    if (current_user==None):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="you are not our user",
        )
    #현재 유저가 댓글의 주인인 경우.
    if(current_user.User_id == _Comment_delete.User_id) :
        rep = comment_crud.delete_comment(db=db, Comment_id = _Comment_delete.Comment_id)
        return rep

    else:   #현재 유저가 댓글의 주인이 아닌 경우
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="you are not owner the comment",
        )

    

# @router.delete("/delete/{compare_id}", status_code=status.HTTP_204_NO_CONTENT)
# def clear_comments(Comment_clear: comment_schema.CommentClear, db: Session = Depends(get_db)):
#     # if not get_comment(db, comment_id=comment_delete.comment_id):
#     #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터를 찾을 수 없습니다.")

#     comment_crud.delete_all(db, compare_id=Comment_clear.compare_id)

#     return {"message": "삭제 완료"}
