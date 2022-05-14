from handlers.utlites import *

def is_existing_login(login: str) -> bool:
    """Возвращает True если login уже занят дургими пользователями,
    False - в обратном случае"""
    users_data = json_file_to_dict(path_of_json_file=get_path_of_user_data())
    return login in users_data.keys()


def is_true_password(password: str) -> bool:
    """Возвращает True если password верен для данного пользователя,
    False  - в обратном случае"""
    current_login = get_login_of_current_session()
    users_data = json_file_to_dict(path_of_json_file=get_path_of_user_data())
    true_password = users_data[current_login]['password']
    return password == true_password


@validation_of_input(is_existing_login)
def get_login_for_authorization() -> str:
    """Возвращает логин введенный пользователем.
    Декоратор validation_of_input повторяет вызов
    данной функции пока is_existing_login не вернет
    False"""
    user_login = input('Введите логин:\n')
    return user_login


@validation_of_input(is_true_password)
@set_limit_of_inputs(3)
def get_password_for_authorization() -> str:
    """Возвращает пароль введенный пользователем.
    Декоратор validation_of_input повторяет вызов
    данной функции пока is_true_password не вернет True.
    Декоратор set_limit_of_inputs органичивает
    количество вызовов данной функции"""
    user_password = input('Введите пароль:\n')
    return user_password


def authorization_user() -> bool:
    """
    :return: True - если пользователь авторизовался,
    False - в обратном случае
    Логин и роль авторизованного пользователя сохраняются
    в json файле
    """
    current_login = get_login_for_authorization()
    users_data = json_file_to_dict(path_of_json_file=get_path_of_user_data())
    user_role = users_data[current_login]['role']
    dict_to_json_file(dict_to_json = {'login' : current_login, 'role' : user_role},
                    path_of_json_file = get_path_of_current_session())

    if current_login and get_password_for_authorization():
        print(f'Здравствуйте, {current_login}!')
        return True
    return False
