from db_config.config import Base # Base es una clase de la que heredarán nuestras clases modelo
from sqlalchemy import (  # Columnas de la base de datos
    Boolean, # Boolean es un tipo de dato que permite definir un valor booleano (True o False)
    Column, # Column es un tipo de dato que permite definir una columna de la base de datos
    Date, # Date es un tipo de dato que permite definir una fecha
    Enum, # Enum es un tipo de dato que permite definir un conjunto de valores posibles
    Float, # Float es un tipo de dato que permite definir un valor decimal
    ForeignKey, # ForeignKey es un tipo de dato que permite definir una llave foranea
    Integer, # Integer es un tipo de dato que permite definir un valor entero
    String, # String es un tipo de dato que permite definir un valor de tipo cadena de caracteres
    Time, # Time es un tipo de dato que permite definir una hora
)
from sqlalchemy.orm import relationship # Relaciones entre tablas de la base de datos (1 a 1, 1 a muchos, muchos a muchos)


class Users(Base): # Clase modelo de la tabla users de la base de datos que hereda de Base para poder ser mapeada a la base de datos por sqlalchemy
    __tablename__ = "users"
    id_users = Column(Integer, primary_key=True) # primary_key=True indica que es la llave primaria de la tabla y no puede repetirse
    name = Column(String(50), nullable=False) # nullable=False indica que el campo no puede ser nulo
    last_name = Column(String(50), nullable=False) 
    password = Column(String(50), nullable=False)
    # token = Column(String(100))
    # last_session = Column(Date) # last_session es la fecha de la ultima sesion del usuario

    # Es necesario definir un constructor para poder añadir datos a la base de datos
    def __init__(self, name, last_name, password): # Constructor de la clase Users que recibe los parametros de la clase y los asigna a los atributos de la clase
        self.name = name
        self.last_name = last_name
        self.password = password
        # self.token = token