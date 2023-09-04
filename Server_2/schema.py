import typing
import strawberry

"""
Un esquema de Strawberry es una colección de tipos de objeto que representan los datos disponibles en la API.
Corresponde a el request de GraphQL
"""

# Esto es un esquema de Strawberry 
# El decorador type declara un tipo de objeto
@strawberry.type
class Book: 
    title: str
    author: str


@strawberry.type
class Query: # Query es un tipo de objeto que representa la raíz de la API
    books: typing.List[Book]
# Otro objeto de raíz podría ser Mutation o Subscription

"""
Objeto de raíz o en ingles Root Object es un tipo de objeto que representa el punto de entrada de la API.

Query: Es similar a un GET en REST y se utiliza para leer datos.
Mutation: Es similar a un POST/PUT/PATCH en REST y se utiliza para escribir datos.
Subscription: Es similar a un WebSocket en REST y se utiliza para recibir actualizaciones en tiempo real.
"""