# Import all the models, so that Base has them before being
# imported by Alembic
from APIs.db.base_class import Base  # noqa
from APIs.models.item import Item  # noqa
from APIs.models.user import User  # noqa