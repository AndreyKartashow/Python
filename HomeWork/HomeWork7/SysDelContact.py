import csv, os


def CopyAll():
    list_copy = []
    with open('users.csv', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        i = 1
        for row in reader:
            list_copy.append(row)
            print(f"{i}. {' '.join(row)} ")
            i += 1
    return list_copy



def DelContact():
    os.system('cls')
    list_copy = CopyAll()

    #for i in list_copy:
    #    print(sti)

    numberContact = 0
    while True:
        numberContact = input('Введите номер контакта, который хотите удалить: ')
        if numberContact.isdigit() and int(numberContact) in range(len(list_copy) + 1):
            break
        
    os.system('cls')
    print(f'Вы действительно хотите удалить контакт?')
    choice = input('Введите 1 для подтверждения или любую другую клавишу для отмены: ')
    if choice == '1':
        list_copy.remove(list_copy[int(numberContact) - 1])
    
    with open('users.csv', 'w',  encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in list_copy:
            writer.writerow(row)

    print('\nКонтакт успешно удален.')
    input('Введите "Enter" для выхода в главное меню ')