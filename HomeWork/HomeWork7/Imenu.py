import os, sys
from SysNewContact import NewContact
from SysFindContact import FindContact
from SysPrintAll import PrintAll
from SysDelContact import DelContact

def printMenu():
    print('')
    print('Это ваша телефонная книга.')
    print('''Вы можете: "1" - Посмотреть все контакты
           "2" - Добавить новый контакт
           "3" - Найти контакт
           "4" - Удалить контакт
           "5" - Выйти из приложения
    ''')


def InputActionInMenu():
    action_menu = '0'
    while action_menu not in '1 2 3 4 5'.split():
        action_menu = input('Введите номер операции (1-5) : ')
    return action_menu


def MainMenu(list_local):
    os.system('cls')
    printMenu()
    action = InputActionInMenu()

    match action:
        case '1':
            PrintAll(list_local)
            input('\nВведите "Enter" для выхода в главное меню ')
        case '2':
            NewContact(list_local)
            input('\nВведите "Enter" для выхода в главное меню ')        
        case '3':
            FindContact(list_local)
            input('\nВведите "Enter" для выхода в главное меню ')
        case '4':
            DelContact(list_local)
        case '5':
            os.system('cls')
            print('Программа закрыта.')
            sys.exit()



