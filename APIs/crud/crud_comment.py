from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.compare import PlantCompare, CompareComment
from schemas.comment_sch import CommentCreateSCH, CommentSCH, CommentDeleteSCH, CommentClearSCH
from schemas.user_sch import UserShowSCH

class  CRUDComment(CRUDBase[CompareComment, CommentCreateSCH, CommentDeleteSCH]):

    def get_comments_by_compare(self, db: Session, *, Compare_id: int
        )-> List[CompareComment]:
        comment_list = db.query(CompareComment)\
            .filter(CompareComment.Compare_id == Compare_id)\
            .order_by(CompareComment.Write_time.desc())\
            .all()  # 데베 안만들어졌는데 고를라고 하니까 문제생김
        return comment_list


    def create_comment(self, db: Session, *, 
        Comment_create: CommentCreateSCH, User_id: int) -> CompareComment:
        db_comment = CompareComment(Contents=Comment_create.Content,
                            Compare_id=Comment_create.Compare_id,
                            User_id = User_id)
        db.add(db_comment)
        db.commit()
        return db_comment


    def get_comment(self, db: Session, *, Comment_id: int):
        comment = db.query(Comment).get(Comment_id)
        return comment

comment_crud = CRUDComment(CompareComment)

"""
def delete_comment(db: Session, db_comment: Comment):
    db.delete(db_comment)
    db.commit()

"""
# def delete_all(db: Session, compare_id: int):
#     subquery = db.query(Comment).join(PlantCompare)\
#         .filter(PlantCompare.compare_id == compare_id)\
#         .subquery()
#     db.query(Comment.comment_id).filter(Comment.comment_id.in_(
#         subquery)).delete(synchronize_session=False)
#     db.commit()
