from sqlalchemy import delete, insert, select, column
from sqlalchemy.orm import subqueryload, Load, load_only, selectinload, deferred, Mapper

from src.graphql.db.session import get_session
from src.graphql.helpers.helper import get_only_selected_fields, get_valid_data
from src.graphql.models import user_model
from src.graphql.scalars.user_scalar import AddUser, User, UserDeleted, UserExists, UserNotFound

async def get_users(info):
    """ Get all users resolver """
    print(f'info users: {info}')
    selected_fields = get_only_selected_fields(user_model.User,info)
    print(f'selected_fields: {selected_fields}')
    async with get_session() as s:
        # sql = select(user_model.User).options(load_only(user_model.User.name, user_model.User.id)).options(subqueryload(user_model.User.stickynotes)) \
        # .order_by(user_model.User.name)
        sql = select(user_model.User).options(subqueryload(user_model.User.stickynotes)) \
        .order_by(user_model.User.name)
        print(f'sql query: {sql}')
        db_users = (await s.execute(sql)).scalars().unique().all()

    users_data_list = []
    for user in db_users:
        user_dict = get_valid_data(user,user_model.User)
        user_dict["stickynotes"] = user.stickynotes
        users_data_list.append(User(**user_dict))
    
    print(f'users_data_list: {users_data_list}')
    return users_data_list

async def get_user(user_id, info):
    """ Get specific user by id resolver """
    print(f'info user: {info}')
    selected_fields = get_only_selected_fields(user_model.User,info)
    print(f'selected_fields: {selected_fields}')
    async with get_session() as s:
        # sql = select(user_model.User).options(load_only(*selected_fields)).options(subqueryload(user_model.User.stickynotes)) \
        # .filter(user_model.User.id == user_id).order_by(user_model.User.name)
        print(f'selected_fields: {selected_fields[0]}')
        # sql = select(user_model.User).options(load_only(user_model.User.name)).options(subqueryload(user_model.User.stickynotes)) \
        # .filter(user_model.User.id == user_id).order_by(user_model.User.name)
        sql = select(user_model.User).options(subqueryload(user_model.User.stickynotes)) \
        .filter(user_model.User.id == user_id).order_by(user_model.User.name)
        print(f'consulta sql: {sql}')

        # Crear una lista de expresiones de columna para seleccionar
        # Crear una lista de expresiones de columna para seleccionar
        # selected_columns = [column(getattr(user_model.User, field)) for field in selected_fields]
        # print(f'selected_columns: {selected_columns}')
        # Construir la consulta dinámicamente
        # sql = select(*selected_columns).options(subqueryload(user_model.User.stickynotes)) \
        #     .filter(user_model.User.id == user_id).order_by(user_model.User.name)
        # sql = select(user_model.User.id, user_model.User.name).options(subqueryload(user_model.User.stickynotes)) \
        #    .filter(user_model.User.id == user_id).order_by(user_model.User.name)
        # print(f'sql query: {sql}')
        db_user = (await s.execute(sql)).scalars().unique().one()

    print(f'db user: {db_user}')
    user_dict = get_valid_data(db_user,user_model.User)
    print(f'user dict: {user_dict}')
    user_dict["stickynotes"] = db_user.stickynotes
    print(f'user_dict: {user_dict}')
    return User(**user_dict)

async def add_user(name):
    """ Add user resolver """
    print(name)
    async with get_session() as s:
        print('get session ok')
        sql = select(user_model.User).options(load_only(user_model.User.name)) \
            .filter(user_model.User.name == name)
        # sql = select(user_model.User.name).filter(user_model.User.name == name)
        print(f'query_sql: {sql}')
        existing_db_user = (await s.execute(sql)).first()
        if existing_db_user is not None:
            return UserExists()
        print('Se puede crear el usuario')
        query = insert(user_model.User).values(name=name)
        print(f'query_sql: {query}')
        await s.execute(query)
        

        print('Se ejecuto el query')
        # sql = select(user_model.User).options(selectinload(user_model.User.name)).filter(user_model.User.name == name)
        sql = select(user_model.User).where(user_model.User.name == name)
        db_user = (await s.execute(sql)).scalars().unique().one()
        # db_user = s.query(user_model.User).filter(user_model.User.name == name).first()
        print(f'Se creo el usuario {db_user}')
        # await s.commit()
        await s.commit()
    db_user_serialize_data = db_user.as_dict()
    return AddUser(**db_user_serialize_data)

async def delete_user(user_id):
    """ Delete user resolver """
    async with get_session() as s:
        sql = select(user_model.User).where(user_model.User.id == user_id)
        existing_db_user = (await s.execute(sql)).first()
        if existing_db_user is None:
            return UserNotFound()

        query = delete(user_model.User).where(user_model.User.id == user_id)
        await s.execute(query)
        await s.commit()
    
    return UserDeleted()