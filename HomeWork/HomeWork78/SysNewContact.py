import csv, os, time, sys


def NewContact(list_local):
    inputData = True
    
    while inputData:
        os.system('cls')
        titleContact = {'Фамилия': '', 'Имя': '', 'Место работы': '', 'Номер': ''}
        user_list = []
        print('Введите данные контакта.')
            
        for iKey in titleContact.keys():
            user_list.append(input(f'{iKey}: '))
    
        print('''Проверьте данные и введите: "1" - для подтвержнения ввода;
                            "2" - для повторного ввода;
                            "3" - для выхода в главное меню
            ''')
    
        key = '0'
        while key not in '1 2 3'.split():
            key = input()

        if key == '1':
            with open('users.csv', 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(user_list)
            list_local.append(user_list)

            inputData = False
            os.system('cls')
            print('Контакт успешно добавлен')
            time.sleep(0.2)
                
        if key == '2':
            continue

        if key == '3':
            inputData = False


def FirstUser(list_local):
    inputData = True
    
    while inputData:
        os.system('cls')
        print('Это ваша телефонная книга и пока что она пуста.')
        print('Добавьте свой первый телефонный контакт!')
        titleContact = {'Фамилия': '', 'Имя': '', 'Место работы': '', 'Номер': ''}
        user_list = []
        print('Введите данные.')
            
        for iKey in titleContact.keys():
            user_list.append(input(f'{iKey}: '))
    
        print('''Проверьте данные и введите: "1" - для подтвержнения ввода;
                            "2" - для повторного ввода;
                            "3" - для выхода из программы
            ''')
    
        key = '0'
        while key not in '1 2 3'.split():
            key = input()

        if key == '1':
            with open('users.csv', 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(user_list)
            list_local.append(user_list)

            inputData = False
            os.system('cls')
            print('Контакт успешно добавлен')
            time.sleep(0.2)
                
        if key == '2':
            continue

        if key == '3':
            print('Программа закрыта.')
            sys.exit()




    



