import csv


def LocalCopy():
    list_copy = []
    with open('users.csv', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            list_copy.append(row)  
    return list_copy