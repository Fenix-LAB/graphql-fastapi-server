import strawberry
from fastapi import FastAPI
from schemas import queries, mutation
import uvicorn
from db_config.config import Base, engine

from strawberry.fastapi import GraphQLRouter


schema = strawberry.Schema(query=queries.Query, mutation=mutation.Mutation) # Create a schema
# El esquema se utiliza para crear un GraphQLRouter
# En este caso se ve asi:
# schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)

graphql_app = GraphQLRouter(schema=schema) # Create a GraphQL app

app = FastAPI() # Create a FastAPI app
app.include_router(graphql_app, prefix="/graphql") # Include the GraphQL app

if __name__ == "__main__":
    Base.metadata.create_all(engine) # Creamos las tablas de la base de datos
    uvicorn.run(app, host="127.0.0.1", port=8080)



