from time import sleep
import random


print('''
Задание 1.
Напишите программу вычисления арифметического выражения заданного строкой.  
Используйте операции +,-,/,*. приоритет операций стандартный.''')

sleep(2)
print('\nРешение')
'''
condition = True
while condition == True:
    expression = input('Введите выражение, например 4+5*3: ')
    for element in expression:
        print(element)
        if element not in '0 1 2 3 4 5 6 7 8 9 + - * /'.split():
            break
        else:
            condition == False
'''
            
expression = input('Введите выражение, например 4+5*3: ')
result = 0
index = 0
while '*' in expression:
    for i in range(len(expression)):
        if expression[i] == '*':
            result += int(expression[i - 1]) * int(expression[i + 1])
            expression = expression[:i-1] + str(result) + expression[i+2:]
            result = 0
            print(expression)
            break
while '+' in expression:
    for i in range(len(expression)):
        if expression[i] == '+':
            result += int(expression[i - 1]) + int(expression[i + 1])
            expression = expression[:i-1] + str(result) + expression[i+2:]
            result = 0
            print(expression)
            break


'''
for i in range(len(expression)):
        if expression[i] == '*':
            result += int(expression[i - 1]) * int(expression[i + 1])
            print(result)
            expression = expression[:i-1] + str(result) + expression[i+2:]
            print(expression)
            break
'''


    
    
#print(expression)


print('___________________________________________________________________________________')









print('''
Задание 2.
Дана последовательность чисел. 
Получить список уникальных элементов заданной последовательности.''')

sleep(2)
print('\nРешение')

list_rand = [(random.randint(1, 10)) for n in range(10)]
print(f'Случайный список сформирован {list_rand}')

list_unic = []
for i in range(len(list_rand)):
        if list_rand[i] not in list_rand[i+1:] and list_rand[i] not in list_rand[:i]:
            list_unic.append(list_rand[i])
print(list_unic)
print('___________________________________________________________________________________')


