from typing import Any

from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr

from APIs.models import user
from APIs.schemas import msg_sch
from APIs.api import deps
from APIs.core.celery_app import celery_app
from APIs.utils import send_test_email

router = APIRouter()


@router.post("/test-celery/", response_model=msg_sch.Msg, status_code=201)
def test_celery(
    msg: msg_sch.Msg,
    current_user: user.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Test Celery worker.
    """
    celery_app.send_task("app.worker.test_celery", args=[msg.msg])
    return {"msg": "Word received"}


@router.post("/test-email/", response_model=msg_sch.Msg, status_code=201)
def test_email(
    email_to: EmailStr,
    current_user: user.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Test emails.
    """
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}