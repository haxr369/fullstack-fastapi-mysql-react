from datetime import datetime

from sqlalchemy.orm import Session

from models.compare import PlantCompare, CompareComment
from schemas.comment_sch import CommentCreateSCH, CommentSCH, CommentDeleteSCH, CommentClearSCH


def get_comment_list(db: Session):
    comment_list = db.query(CompareComment)\
        .order_by(CompareComment.create_date.desc())\
        .all()  # 데베 안만들어졌는데 고를라고 하니까 문제생김
    return comment_list


def create_comment(db: Session, Comment_create: CommentCreateSCH):
    db_comment = CompareComment(Contents=Comment_create.Content,
                         Compare_id=Comment_create.Compare_id,
                         Write_time=datetime.now())
    db.add(db_comment)
    db.commit()


def get_comment(db: Session, Comment_id: int):
    return db.query(Comment).get(Comment_id)


def delete_comment(db: Session, db_comment: Comment):
    db.delete(db_comment)
    db.commit()


# def delete_all(db: Session, compare_id: int):
#     subquery = db.query(Comment).join(PlantCompare)\
#         .filter(PlantCompare.compare_id == compare_id)\
#         .subquery()
#     db.query(Comment.comment_id).filter(Comment.comment_id.in_(
#         subquery)).delete(synchronize_session=False)
#     db.commit()
