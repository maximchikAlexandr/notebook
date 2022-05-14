from handlers.utlites import *
from datetime import datetime

def get_user_input_in_notebook() -> str:
    return input('''Для добавления записи нажмите «1», для просмотра записей - «2»,
для удаления записи - «3», для выхода - «0»\n''')


def add_note_to_notebook_dict(text_of_note: str, notebook: dict) -> dict:
    """
    Добавляет новую запись в записную книгу dict
    :param text_of_note: text of new note,
    :param notebook: dict,
    :return: notebook with new note
    """
    current_login = get_login_of_current_session()

    if notebook.get(current_login) == None:
        notebook[current_login] = {}
        
    note = {'date_of_note': datetime.now().strftime('%d/%m/%y %H:%M:%S'),
            'text_of_note': text_of_note}
    key = str(len(notebook[current_login]) + 1)
    notebook[current_login][key] = note
    return notebook


def add_note_to_notebook_json() -> None:
    """Добавляет новую запись в записную книгу в файле json """
    notebook = json_file_to_dict(path_of_json_file=get_path_of_notebook())
    note_from_input = input('Введите текст:\n')
    notebook = add_note_to_notebook_dict(note_from_input, notebook)
    dict_to_json_file(dict_to_json=notebook,
                    path_of_json_file=get_path_of_notebook())
    print('Запись сохранена!')


def print_all_notes() -> None:
    """
    Выводит записи в консоль.
    Для пользователей с ролью user - выводит только их записи.
    Для пользователей с ролью admin - выводит все записи.
    """
    current_login = get_login_of_current_session()
    user_role = get_role_of_current_session()

    notebook = json_file_to_dict(path_of_json_file=get_path_of_notebook())

    if user_role == 'user':

        user_notebook = notebook[current_login]
        for key, value in user_notebook.items():
            print(f"#{key} {value['date_of_note']}\n{value['text_of_note']}\n")
            
    elif user_role == 'admin':

        for user, user_notebook in notebook.items():
            print(f"Пользователь «{user}»\n")
            for key, note in user_notebook.items():
                print(f"n#{key} {note['date_of_note']}\n{note['text_of_note']}\n")
            print('=' * 25)

def del_note() -> None:
    """Удаляет запись авторизованного пользователя"""
    current_login = get_login_of_current_session()
    notebook = json_file_to_dict(path_of_json_file=get_path_of_notebook())
    key_note = input('Введите номер удаляемой записи:\n')
    del notebook[current_login][key_note]
    dict_to_json_file(dict_to_json=notebook,
                    path_of_json_file=get_path_of_notebook())
    print('Запись удалена!')
    
def work_with_notebook() -> None:
    """Обеспечивает работу авторизованного пользователя с записной книгой"""
    user_input = get_user_input_in_notebook()

    while user_input != '0':
        if user_input == '1':
            add_note_to_notebook_json()
            user_input = get_user_input_in_notebook()
        elif user_input == '2':
            print_all_notes()
            user_input = get_user_input_in_notebook()
        elif user_input == '3':
            del_note()
            user_input = get_user_input_in_notebook()
        else:
            print('Неверный ввод!')
            user_input = get_user_input_in_notebook()
