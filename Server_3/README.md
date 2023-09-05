# Firs Full GraphQL API

## Folder Structure

```bash
API GraphQL/
│
├── app/
│ ├── db_config/
│ │ ├── db_config.py
│ │ ├── session.py
│ │ └── ...
│ │
│ ├── db_models/
│ │ ├── models.py
│ │ ├── responses_models.py
│ │ └── ...
│ │
│ ├── routes/
│ │ ├── router
│ │ │ ├── router1.py
│ │ │ ├── router2.py
│ │ │ └── ...
│ │ ├── api.py
│ │ └── ...
│ │
│ ├── schemas/
│ │ ├── types.py
│ │ ├── queries.py
│ │ ├── mutations.py
│ │ ├── subscriptions.py
│ │ └── ...
│ │
│ ├── resolvers/
│ │ ├── query.py
│ │ ├── mutation.py
│ │ ├── subscription.py
│ │ └── ...
│ │
│ ├── services/
│ │ ├── service1.py
│ │ ├── service2.py
│ │ └── ...
│ │
│ └── server.py
│
├── database/
│ ├── Dockerfile
│ ├── init_db.sh
│ └── ...
│
├── README.md
└── ...
```