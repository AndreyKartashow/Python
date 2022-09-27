import csv, os
from SysPrintAll import PrintAll
import pandas as pd



def DelContact(list_local):
    os.system('cls')

    PrintAll(list_local)

    numberContact = 0
    while True:
        numberContact = input('Введите номер контакта, который хотите удалить: ')
        if numberContact.isdigit() and int(numberContact) in range(len(list_local) + 1):
            break
        
    os.system('cls')
    print('Вы действительно хотите удалить контакт?')
    choice = input('Введите 1 для подтверждения или любую другую клавишу для отмены: ')
    if choice == '1':
        list_local.remove(list_local[int(numberContact) - 1]) 
    
    with open('users.csv', 'w',  encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in list_local:
            writer.writerow(row)

    print('\nКонтакт успешно удален.')
    input('Введите "Enter" для выхода в главное меню ')