from datetime import datetime

from sqlalchemy.orm import Session

from models.compare import PlantCompare
from schemas.plantcompare_sch import PlantCompareCreateSCH, PlantCompareSCH



def get_compare_list(db: Session):
    compare_list = db.query(PlantCompare).all()
    return compare_list


def create_compare(db: Session, PlantCompare_create: PlantCompareCreateSCH):
    db_comment = PlantCompare(Tip=PlantCompare_create.Tip,
                              Left_Species_name=PlantCompare_create.Left_Species_name,
                              Right_Species_name=PlantCompare_create.Right_Species_name,
                              Title=PlantCompare_create.Title)
    db.add(db_comment)
    db.commit()
    return db_comment


def get_compare(db: Session, Compare_id: int):
    return db.query(PlantCompare).get(Compare_id)

"""
삭제와 댓글 불러오기는 추후에 정리할 예정. 먼저 비교 페이지 관련 API만...
def delete_compare(db: Session, db_compare: PlantCompare):
    db.delete(db_compare)
    db.commit()


def get_comments(db: Session, Compare_id: int):
    return db.query(CompareComment).join(PlantCompare)\
        .filter(PlantCompare.Compare_id == Compare_id)\
        .order_by(CompareComment.Write_time.desc())\
        .all()
"""