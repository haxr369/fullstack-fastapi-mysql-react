# Import all the models, so that Base has them before being
# imported by Alembic
from db.base_class import Base  # noqa
from code.app.models.item import Item  # noqa
from models.user import User  # noqa