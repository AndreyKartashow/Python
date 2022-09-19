from operator import index
import random
from time import sleep  


print('''
Задание 1.
Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на нечётной позиции.''')

sleep(2)
print('\nРешение')
list_random = [(random.randint(2, 7)) for number in range(random.randint(5, 10))]
#list_random = []
#lenght_list = random.randint(5, 10)
#for number in range(lenght_list):
#    list_random.append(random.randint(2, 7))
print('Список сформирован: ', end =' ')
print(list_random)

summ = 0
for index in range(len(list_random)):
    if (index % 2):
        summ += list_random[index]
print(f'Сумма нечетных элементов: sum = [{summ}]')
print('___________________________________________________________________________________')

sleep(2)
print('''
Задание 2.
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.''')

sleep(2)
print('\nРешение')
func = lambda n: random.randint(2, 7)
list_random = [func(n) for n in range(5)]
#list_random = []
#lenght_list = random.randint(5, 10)
#for number in range(lenght_list):
#    list_random.append(random.randint(2, 7))
print('Список сформирован: ', end =' ')
print(list_random)

list_mult = []
index_first = 0
index_last = len(list_random) - 1

while True:
    list_mult.append(list_random[index_first] * list_random[index_last])

    index_first += 1
    index_last -= 1

    if index_last - index_first == -1:
        break
    elif index_first == index_last:
        list_mult.append(list_random[index_first] ** 2)
        break

print(f'Список произведений парных элементов {list_mult}')
print('___________________________________________________________________________________')

sleep(2)
print('''
Задание 3.
Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным 
значением дробной части элементов.''')

sleep(2)
print('\nРешение')
f = lambda x: round(random.random()*10, 2)
rand = random.randint(5, 10)
list_float = [f(n) for n in range(rand)]
#list_float = []
#lenght_list = random.randint(5, 10)
#for counter in range(lenght_list):
#    list_float.append(round(random.random()*10, 2))

''' 
    Конкотация строк
    number_string = str(random.randint(0, 10)) + '.' + str(random.randint(0, 99))
    list_float.append(number_string)
'''

print(f'Список сформирован: {list_float}')

list_slice_float = []
for number in range(len(list_float)):
    str_number = str(list_float[number])
    index_point = str_number.find('.')
    slice_float = int(str_number[index_point + 1:])
    list_slice_float.append(slice_float)
print(f'Список срезов дробной части: {list_slice_float}')
print(f'Максимальный срез: {max(list_slice_float)}. Минимальный срез: {min(list_slice_float)}.')
diff = max(list_slice_float) - min(list_slice_float)
print(f'Разница максимальной и минимальной дробных частей равна: {diff}')
print('___________________________________________________________________________________')


sleep(2)
print('''
Задание 4.
Напишите программу, которая будет преобразовывать десятичное число в двоичное.''')

sleep(2)
print('\nРешение')
print(f'Десятичное число 45 в двоичной системе счисления соответствует значению {bin(45)[2:]}')
print(f'Десятичное число 3 в двоичной системе счисления соответствует значению {bin(3)[2:]}')
print(f'Десятичное число 2 в двоичной системе счисления соответствует значению {bin(2)[2:]}')
print('___________________________________________________________________________________')


sleep(2)
print('''
Задание 5.
Задайте число и составьте для список чисел Фибоначчи, 
в том числе для отрицательных индексов.''')

sleep(2)
print('\nРешение')
count_Fb = 8
print(f'Заданое число для последовательности равно: {count_Fb} не включая 0')

list_Fb = [0, 1]
for i in range(count_Fb - 1):
    number_pos_Fb = list_Fb[i] + list_Fb[i + 1]
    list_Fb.append(number_pos_Fb)
print(f'Прямая последовательность Фибоначи {list_Fb}')

list_nigativ = [0, 1]
for i in range(count_Fb - 1):
    number_pos_Fb = list_nigativ[i] - list_nigativ[i + 1]
    list_nigativ.append(number_pos_Fb)
list_nigativ.reverse()
print(f'Обратная последовательность Фибоначи {list_nigativ}')

list_nFb = list_nigativ[:-1] + list_Fb
print(f'Общий список {list_nFb}\n')