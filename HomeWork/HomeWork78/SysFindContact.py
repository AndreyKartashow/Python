import os
from SysPrintAll import PrintAll


def FindContact(list_local):
    search = True

    while search:
        os.system('cls')
        item = input('Введите один из параметров поиска: ')
        print()
        list_search = []
        for row in list_local:
            if item in row:
                list_search.append(row)

        if len(list_search) == 0:
            print('Контакты по такому параметру не найдены')
            
        else:
            PrintAll(list_search)

        searchKey = input('\nВведите 1 для выхода в меню или любую другую для продолжение поиска: ')
        if searchKey == '1':
            search = False
    
    

