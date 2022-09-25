import csv, os, time


def FindContact():
    search = True
    
    while search:
        os.system('cls')
        item = input('Введите один из параметров поиска: ')
        print()
        with open('users.csv', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if item in row:
                    print(' '.join(row))
                    time.sleep(0.5)
            if item not in reader:    
                print('Контакты по такому параметру не найдены')

        searchKey = input('\nВведите 1 для выхода в меню или любую другую для продолжение поиска: ')
        if searchKey == '1':
            search = False
    
    

