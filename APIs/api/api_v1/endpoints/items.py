from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models.user
from schemas import item_sch
from api import deps

router = APIRouter()

@router.get("/plant")
async def root():
    return "plant 에서 사용자관리"

@router.get("/", response_model=List[item_sch.Item])
def read_items(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve items.
    """
    items = crud.item.get_multi(db, skip=skip, limit=limit)

    return items


@router.post("/", response_model=item_sch.Item)
def create_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: item_sch.ItemCreate,
) -> Any:
    """
    Create new item.
    """
    item = crud.item.create_with_owner(db=db, obj_in=item_in)
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
    item = crud.item.get(db=db, id=id)

    item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
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
    item = crud.item.get(db=db, id=id)
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
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item = crud.item.remove(db=db, id=id)
    return item