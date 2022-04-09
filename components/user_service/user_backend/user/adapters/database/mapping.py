from sqlalchemy.orm import registry

from user.application.dataclasses import User
from .tables import user_table

mapper = registry()

mapper.map_imperatively(User, user_table)
