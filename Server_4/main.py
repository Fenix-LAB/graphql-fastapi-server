# from graphql.core.config import settings
import asyncio
import uvicorn
from populate import create_tables
from src.graphql.db.session import engine
from app import create_app

application = create_app()

if __name__ == "__main__":
    print("Populating database...")
    asyncio.run(create_tables(engine))
    print("Database populated.")

    print("Starting server...")
    uvicorn.run("main:application", host= "127.0.0.1", port=8080, reload=True)