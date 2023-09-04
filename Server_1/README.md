# First Server

En este primer ejemplo se usa el siguiente esquema:

```python
@strawberry.type # El decorador type declara un tipo de objeto
class Query: # Query es un tipo de objeto que representa la raíz de la API 
    @strawberry.field # El decorador field declara un campo en el tipo de objeto
    def hello(self) -> str: # La función hello es un resolver para el campo hello 
        return "Hello, world!" # El resolver devuelve el valor del campo
```

Este esquema sirve para consumir una consulta de graphql de tipo query, es decir, una consulta que no modifica el estado de la base de datos, sino que solo obtiene información de la misma.

Cualquier consulta de graphql debe tener un tipo de objeto raíz, en este caso el tipo de objeto raíz es Query, el cual tiene un campo llamado hello, que devuelve un string.

Cuando se ejecuta la consulta, el servidor ejecuta el resolver de la consulta, en este caso la función hello, y devuelve el valor que esta función devuelve.

El ejecutar una consulta con el siguiente cuerpo:

```graphql
query {
    hello
}
```

Devuelve el siguiente resultado:

```json
{
    "data": {
        "hello": "Hello, world!"
    }
}
```