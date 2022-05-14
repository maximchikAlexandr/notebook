from  handlers import *

def get_user_input() -> str:
    return input('Для регистрации нажмите «1», для авторизации - «2», для выхода - «0»\n')

def main():
    create_folders()
    user_input = get_user_input()

    while user_input != '0':

        if user_input == '1':
            registarion_new_user()
            user_input = get_user_input()
        elif user_input == '2':
            if authorization_user():
                work_with_notebook()
            user_input = get_user_input()
        else:
            print('Неверный ввод!')
            user_input = get_user_input()

    print('Good bye!')


if __name__ == '__main__':
    main()
