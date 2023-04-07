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


def get_compare(db: Session, Compare_id: int):
    return db.query(PlantCompare).get(Compare_id)


def delete_compare(db: Session, db_compare: PlantCompare):
    db.delete(db_compare)
    db.commit()


def get_comments(db: Session, Compare_id: int):
    return db.query(CompareComment).join(PlantCompare)\
        .filter(PlantCompare.Compare_id == Compare_id)\
        .order_by(CompareComment.Write_time.desc())\
        .all()
        