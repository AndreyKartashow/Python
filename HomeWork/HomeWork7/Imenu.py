import os, sys
from SysNewContact import NewContact
from SysFindContact import FindContact
from SysFindAll import FindAll
from SysDelContact import DelContact

def printMenu():
    print('')
    print('Это ваша телефонная книга.')
    print('Вы можете:')
    print('''
    "1" - Посмотреть все контакты
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


def MainMenu():
    os.system('cls')
    printMenu()
    action = InputActionInMenu()

    match action:
        case '1':
            FindAll()
        case '2':
            NewContact()        
        case '3':
            FindContact()
        case '4':
            DelContact()
        case '5':
            os.system('cls')
            print('Программа закрыта.')
            sys.exit()

while True:
    MainMenu()

