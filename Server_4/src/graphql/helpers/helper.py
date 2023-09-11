from sqlalchemy.inspection import inspect
import re

def convert_camel_case(name):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    name = pattern.sub('_', name).lower()
    return name

def get_only_selected_fields(db_baseclass_name,info):
    db_relations_fields = inspect(db_baseclass_name).relationships.keys()
    print(f'db_relations_fields: {db_relations_fields}')
    # elected_fields = [convert_camel_case(field.name)  for field in info.selected_fields[0].selections if field.name not in db_relations_fields]
    # Seleccione solo los campos que no son relaciones
    selected_fields = []
    for field in info.selected_fields[0].selections:
        field_name = field.name  # Nombre del campo seleccionado
        
        # Verificar si el campo se basa en la entidad User
        if field_name in db_baseclass_name.__table__.columns:
            full_field_name = f"user_model.User.{field_name}"
            print(f'field: {full_field_name}')
            selected_fields.append(full_field_name)
        else:
            # Si no es un campo de User, simplemente imprímelo tal como está
            print(f'field: {field_name}')
    # for field in info.selected_fields[0].selections:
    #     print(f'field: {field}')
    #     selected_fields.append(convert_camel_case(field.name))
    #     if field.name not in db_relations_fields:
    #         print(f'convert_camel_case(field.name): {convert_camel_case(field.name)}')
    # selected_fields = [for field in info.selected_fields[0].selections if field.name not in db_relations_fields]
    print(f'selected_fields: {selected_fields}')
    return selected_fields
    
def get_valid_data(model_data_object, model_class):
    data_dict = {}
    for column in model_class.__table__.columns:
        try:
            data_dict[column.name] = getattr(model_data_object,column.name)
        except:
            pass
    return data_dict