from time import sleep
import random


print('''
Задание 1.
Напишите программу вычисления арифметического выражения заданного строкой.  
Используйте операции +,-,/,*. приоритет операций стандартный.''')

sleep(2)
print('\nРешение')
expression = input('Введите выражение, например 4+5*3: ')
staples = ''
result = 0

# Все операции умножения
while '*' in expression:
    for i in range(len(expression)):
        # Поиск умножения
        if expression[i] == '*':

            # Проверка левой позиции
            curent_left = i - 1
            left = ''
            while curent_left != -1:
                if expression[curent_left] != '*' and expression[curent_left] != '/' and expression[curent_left] != '+' and expression[curent_left] != '-':
                    left = expression[curent_left] + left
                    curent_left -= 1
                else:
                    break
            left_n = float(left)

            # Проверка правой позиции
            curent_right = i + 1
            right = ''
            while curent_right != len(expression):
                if expression[curent_right] != '*' and expression[curent_right] != '/' and expression[curent_right] != '+' and expression[curent_right] != '-':
                    right = right + expression[curent_right]
                    curent_right += 1
                else:
                    break
            right_n = float(right)

            # результирующая подвыражения
            result += left_n * right_n
            expression = expression[:curent_left+1] + str(result) + expression[curent_right:]
            result = 0
            print(expression)
            break

# Все операции деления
while '/' in expression:
    for i in range(len(expression)):
        # Поиск умножения
        if expression[i] == '/':

            # Проверка левой позиции
            curent_left = i - 1
            left = ''
            while curent_left != -1:
                if expression[curent_left] != '*' and expression[curent_left] != '/' and expression[curent_left] != '+' and expression[curent_left] != '-':
                    left = expression[curent_left] + left
                    curent_left -= 1
                else:
                    break
            left_n = float(left)

            # Проверка правой позиции
            curent_right = i + 1
            right = ''
            while curent_right != len(expression):
                if expression[curent_right] != '*' and expression[curent_right] != '/' and expression[curent_right] != '+' and expression[curent_right] != '-':
                    right = right + expression[curent_right]
                    curent_right += 1
                else:
                    break
            right_n = float(right)

            # результирующая подвыражения
            result += left_n / right_n
            expression = expression[:curent_left+1] + str(result) + expression[curent_right:]
            result = 0
            print(expression)
            break

# Все операции сложения
while '+' in expression:
    for i in range(len(expression)):
        # Поиск сложения
        if expression[i] == '+':

            # Проверка левой позиции
            curent_left = i - 1
            left = ''
            while curent_left != -1:
                if expression[curent_left] != '*' and expression[curent_left] != '/' and expression[curent_left] != '+' and expression[curent_left] != '-':
                    left = expression[curent_left] + left
                    curent_left -= 1
                else:
                    break
            left_n = float(left)

            # Проверка правой позиции
            curent_right = i + 1
            right = ''
            while curent_right != len(expression):
                if expression[curent_right] != '*' and expression[curent_right] != '/' and expression[curent_right] != '+' and expression[curent_right] != '-':
                    right = right + expression[curent_right]
                    curent_right += 1
                else:
                    break
            right_n = float(right)

            # результирующая подвыражения
            result += left_n + right_n
            expression = expression[:curent_left+1] + str(result) + expression[curent_right:]
            result = 0
            print(expression)
            break

# Все операции вычитания
while '-' in expression:
    for i in range(len(expression)):
        # Поиск сложения
        if expression[i] == '-':

            # Проверка левой позиции
            curent_left = i - 1
            left = ''
            while curent_left != -1:
                if expression[curent_left] != '*' and expression[curent_left] != '/' and expression[curent_left] != '+' and expression[curent_left] != '-':
                    left = expression[curent_left] + left
                    curent_left -= 1
                else:
                    break
            left_n = float(left)

            # Проверка правой позиции
            curent_right = i + 1
            right = ''
            while curent_right != len(expression):
                if expression[curent_right] != '*' and expression[curent_right] != '/' and expression[curent_right] != '+' and expression[curent_right] != '-':
                    right = right + expression[curent_right]
                    curent_right += 1
                else:
                    break
            right_n = float(right)

            # результирующая подвыражения
            result += left_n - right_n
            expression = expression[:curent_left+1] + str(result) + expression[curent_right:]
            result = 0
            print(expression)
            break

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


