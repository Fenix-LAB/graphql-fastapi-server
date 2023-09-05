from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

host = "localhost"
port = "5432"
user = "postgres"
password = "password"
db_name = "db_gq"

POSTGRES_SQL_CONNECTION = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
# print(POSTGRES_SQL_CONNECTION) # postgresql://postgres:password@localhost:5432/db_myapp

try:
    # Conexión a la base de datos
    engine = create_engine(POSTGRES_SQL_CONNECTION, echo=True) # echo=True para ver las consultas SQL
    print("Conection succesfully")
except Exception as ex:
    print("Could Not connect to Database %s", ex)

meta = MetaData() # MetaData es un objeto que contiene toda la información sobre las tablas

Base = declarative_base() # Base es una clase de la que heredarán nuestras clases modelo

Session = sessionmaker(bind=engine) # Session es una clase que nos servirá para crear sesiones con la base de datos

print("Ready to work")