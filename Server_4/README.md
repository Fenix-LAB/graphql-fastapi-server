# Full Api GraphQL

actualmente se esta trabajando en la implementacion de un servidor GraphQL con FastAPI

## Requerimientos
strawberry-graphql[fastapi]
sqlalchemy
asyncpg

aaahhh necesito subir un update para que github me deje subir el proyecto
otra ves necesito subir un update para que github me deje subir el proyecto

```bash

app/
│
├── src/
│   │
│   ├── graphql/
│   │   │
│   │   ├── core/
│   │   │  └── config.py
│   │   │
│   │   ├── db/
│   │   │  └── session.py
│   │   │
│   │   ├── schemas/
│   │   │  ├── query_schema.py
│   │   │  ├── mutation_schema.py
│   │   │  └── subscription_schema.py
│   │   │
│   │   ├── models/
│   │   │  ├── x_model.py
│   │   │  ├── y_model.py
│   │   │  └── ...
│   │   │
│   │   ├── resolvers/
│   │   │  ├── x_resolver.py
│   │   │  ├── y_resolver.py
│   │   │  └── ...
│   │   │
│   │   ├── scalars/
│   │   │  ├── x_scalar.py
│   │   │  ├── y_scalar.py
│   │   │  └── ...
│   │   │
│   │   ├── fragments/
│   │   │  ├── x_fragment.py
│   │   │  ├── y_fragment.py
│   │   │  └── ...
│   │   │
│   │   └── helpers/
│   │      └── helper.py
│   │   
│   │
│   ├── rest/
│       │
│       ├── utils/
│       │  ├── utils.py
│       │  └── ...
│       │
│       ├── server.py
│       
│
├── main.py
│
├── README.md
```
