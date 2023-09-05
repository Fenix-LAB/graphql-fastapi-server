import psycopg2

"""
Cada ves que se levante una base de datos podemos intentar conectarnos a ella
con el el siguiuente código.
"""

try:
    # Conexión a la base de datos
    conn = psycopg2.connect(
        dbname='db_gq',
        user='postgres',
        password='password',
        host='localhost',
        port='5432'
    )
    print("Conexión exitosa a la base de datos.")
    conn.close()
except psycopg2.Error as e:
    print("Error al conectar a la base de datos:", e)