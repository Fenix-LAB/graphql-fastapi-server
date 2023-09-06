import typing
import strawberry

# schema para interactuar con la base de datos
@strawberry.type
class Users:
    name: str
    last_name: str
    password: str

