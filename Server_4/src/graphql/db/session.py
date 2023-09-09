from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# from graphql.core.config import settings

# engine = create_async_engine(
#     f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
# )

host = "localhost"
port = "5432"
user = "postgres"
password = "password"
db_name = "db_gq"

POSTGRES_SQL_CONNECTION = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}"
# print(POSTGRES_SQL_CONNECTION) # postgresql://postgres:password@localhost:5432/db_myapp

try:
    # Conexión a la base de datos
    engine = create_async_engine(POSTGRES_SQL_CONNECTION, echo=True) # echo=True para ver las consultas SQL
    print("Conection succesfully")
except Exception as ex:
    print("Could Not connect to Database %s", ex)


async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
            finally:
                await session.close()