import json
import os

def _check_existing_of_file(func):
    '''check existing of file'''
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except FileNotFoundError:
            return {}
        else:
            return func(*args, **kwargs)

    return inner


def dict_to_json_file(dict_to_json: dict, path_of_json_file: str) -> None:
    """convert dict to json file"""
    txt_to_json = json.dumps(dict_to_json)
    with open(path_of_json_file, 'w', encoding='utf-8') as file:
        json.dump(txt_to_json, file)


@_check_existing_of_file
def json_file_to_dict(path_of_json_file: str) -> dict:
    """convert json file to dict"""
    with open(path_of_json_file, 'r') as file:
        return json.loads(json.load(file))


def validation_of_input(is_valid_func):
    """The decorator repeats the call of the "func" while "is_valid_func" returns False """
    def check_valid_input(func):
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            while not is_valid_func(res):
                print('Неверный ввод!')
                res = func(*args, **kwargs)
            return res

        return inner

    return check_valid_input


def set_limit_of_inputs(limit_of_inputs):
    """Декоратор устанавливает количество вызовов функции
    limit_of_inputs - предельное количество вызовов функции func
    """
    def check_count_of_inputs(func):
        count_of_inputs = 0
        def inner(*args, **kwargs):
            nonlocal count_of_inputs
            count_of_inputs += 1
            if count_of_inputs > limit_of_inputs:
                pass
            return func(*args, **kwargs)

        return inner

    return check_count_of_inputs

def create_folders() -> None:
    """Создает все несозданные папки"""

    list_folders = ['data', 'config']
    for folder in list_folders:
        if not os.path.exists(folder):
            os.mkdir(folder)




def get_login_of_current_session() -> str:
    """Передает логин пользователя, авторизованного в текущий момент"""
    temp_dict = json_file_to_dict(path_of_json_file = get_path_of_current_session())
    current_login = temp_dict['login']
    return current_login

def get_role_of_current_session() -> str:
    """Передает роль пользователя, авторизованного в текущий момент"""
    temp_dict = json_file_to_dict(path_of_json_file = get_path_of_current_session())
    user_role = temp_dict['role']
    return user_role


def get_path_of_user_data() -> str:
    """Передает адрес json файла с регистрационными данными пользователей"""
    return 'data/users_data.json'


def get_path_of_notebook() -> str:
    """Передает адрес json файла, содержащего записную книгу пользователей"""
    return 'data/notebook.json'


def get_path_of_current_session() -> str:
    """Передает адрес json файла с логином и ролью авторизованного пользователя"""
    return 'config/temp_file.json'

