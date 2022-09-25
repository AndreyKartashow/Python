import csv, os, time


def FindAll():
    os.system('cls')
    print()
    with open('users.csv', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print(' '.join(row))
            time.sleep(0.2)
    input('\nВведите "Enter" для выхода в главное меню ')
