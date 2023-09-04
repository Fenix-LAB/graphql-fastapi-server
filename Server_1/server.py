import strawberry
from fastapi import FastAPI

from strawberry.fastapi import GraphQLRouter

# Esto es un esquema de Strawberry
@strawberry.type # El decorador type declara un tipo de objeto
class Query: # Query es un tipo de objeto que representa la raíz de la API 
    @strawberry.field # El decorador field declara un campo en el tipo de objeto
    def hello(self) -> str: # La función hello es un resolver para el campo hello 
        return "Hello, world!" # El resolver devuelve el valor del campo

schema = strawberry.Schema(query=Query) # Create a schema
# El esquema se utiliza para crear un GraphQLRouter
# En este caso se ve asi:
# schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)

graphql_app = GraphQLRouter(schema=schema) # Create a GraphQL app

app = FastAPI() # Create a FastAPI app
app.include_router(graphql_app, prefix="/graphql") # Include the GraphQL app

"""
for run server:
uvicorn server:app --reload 

for documentation:
http://127.0.0.1:8000/graphql

for query:
{
    hello
}

the result is:
{
  "data": {
    "hello": "Hello, world!"
  }
}
"""