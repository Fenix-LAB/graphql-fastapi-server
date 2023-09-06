import typing
import strawberry
# from conn.db import conn
# from models.index import users
from strawberry.types import Info
from db_config.config import Session
from db_models.models import Users
from .types import Users as UsersType


@strawberry.type
class Query:
    # Query para obtener todos los usuarios
    @strawberry.field
    def get_all_users(self) -> typing.List[UsersType]:
        session = Session()
        users = session.query(Users).all()
        session.close()
        return users