from handlers.utlites import *
from registarion import register_new_account


def registarion_admin() -> None:
    users_data = json_file_to_dict(path_of_json_file=get_path_of_user_data())
    users_data = register_new_account(login = 'admin',
                                   password = '123',
                                   role = 'admin',
                                   users_data = users_data)
    dict_to_json_file(dict_to_json=users_data,
                    path_of_json_file=get_path_of_user_data())
