import strawberry
from fastapi import FastAPI
from schema import Book
from schema import typing
from resolvers import get_books

from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)

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
  books {
    title
    author
  }
}

the result is:
{
  "data": {
    "books": [
      {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
      }
    ]
  }
}
"""