import typing
import strawberry
# from conn.db import conn
# from models.index import users
from strawberry.types import Info

from db_config.config import Session
from db_models.models import Users
from .types import Users as UsersType


@strawberry.type
class Mutation:
    # Agregar un nuevo usuario
    @strawberry.mutation
    def create_user(self, name: str, last_name: str, password: str) -> typing.List[UsersType]:
        session = Session()
        user = Users(name=name, last_name=last_name, password=password)
        session.add(user)
        session.commit()
        # session.close()
        return [user]
