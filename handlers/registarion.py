from handlers.utlites import *
from datetime import datetime

def register_new_account(login: str, password: str, role: str, users_data: dict) -> dict:
    """
    :param login: - логин нового пользователя,
    :param password: - пароль нового пользователя,
    :param role: - роль нового пользователя - user или admin,
    :param users_data: - dict с информацией о всех пользовтелях
    :return: users_data с добавленными данными о новом пользователе
    """
    user_data = {'login': login,
                 'password': password,
                 'role': role,
                 'date_of_registarion': datetime.now().strftime('%d/%m/%y %H:%M:%S')}
    key = user_data['login']
    users_data[key] = user_data
    return users_data


def is_valid_password(password: str) -> bool:
    """
    Проверяет пароль на валидность
    :param password: password of a user
    :return: return True if password is valid, False otherwise
    """
    num_list = [ch for ch in password if ch in '0123456789']
    check_list = (len(password) > 3,
                  len(num_list) > 3,
                  password != password.lower(),
                  password != password.upper(),
                  password.isascii())
    return all(check_list)


def is_valid_login(login: str) -> bool:
    """
    Проверяет логин на валидность
    :param password: login of a user
    :return: return True if login is valid, False otherwise
    """
    users_data = json_file_to_dict(path_of_json_file=get_path_of_user_data())
    check_list = (len(login) > 3,
                  login not in users_data.keys(),
                  login.isascii())
    return all(check_list)


@validation_of_input(is_valid_login)
def get_input_login() -> str:
    """
    :return: логин введенный пользователем.
    Декторатор validation_of_input вызвает данную
    функцию пока is_valid_login не вернет True.
    """
    user_login = input('''Требования к логину:
 - длина более 3 символов
 - только латиница;
 - должен быть не занятым.
Введите логин:
''')
    return user_login


@validation_of_input(is_valid_password)
def get_input_password() -> str:
    """
    :return: пароль введенный пользователем.
    Декторатор validation_of_input вызвает данную
    функцию пока is_valid_login не вернет True.
    """
    user_password = input('''Требования к паролю:
 - длина более 8 символов;
 - только латиница;
 - более 3 цифр;
 - заглавные и сточные буквы.
Введите пароль:
''')
    return user_password


def registarion_new_user() -> None:
    """Регистрирует нового пользователя"""
    users_data = json_file_to_dict(path_of_json_file=get_path_of_user_data())
    user_login = get_input_login()
    user_password = get_input_password()
    users_data = register_new_account(login=user_login,
                                   password=user_password,
                                   role = 'user',
                                   users_data=users_data)
    dict_to_json_file(dict_to_json=users_data,
                      path_of_json_file=get_path_of_user_data())
