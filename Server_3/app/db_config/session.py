from db_config.config import Session 

# function to connect to db
def get_db_connect():
    """start connect db"""
    db_session = Session() # Session es una clase que nos servirá para crear sesiones con la base de datos
    try:
        yield db_session # yield es como un return pero no finaliza la función y permite continuarla en el mismo punto
    finally:
        db_session.close() # close session db