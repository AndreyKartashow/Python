from ast import While
from gettext import find
from itertools import count
import random
from time import sleep
from numpy.polynomial import Polynomial
from numpy.polynomial import polynomial


print('''
Задание 1.
Вычислить число c заданной точностью d.''')

sleep(2)
print('\nРешение')
print('Введите число, которое хотите округлить.')
print('Дробная часть отделяется точкой < . >')
number = float(input('n = '))
print('Укажите точность округления (0.1, 0.01, 0.001 и тд)')
accuracy = input('точность округления: ')

index_point = accuracy.find('.') 
accuracy_number = int(len(accuracy[index_point:]) - 1)    
print(f'Ваше число было округлено до значения: {round(number, accuracy_number)}')
print('___________________________________________________________________________________')


sleep(2)
print('''
Задание 2.
Задайте натуральное число N. Напишите программу, 
которая составит список простых множителей числа N.''')

sleep(2)
print('\nРешение')
number_N = int(input('Введите число: '))
list_simple_def = []

it = 2
while it <= number_N:
    if (number_N % it == 0):
        list_simple_def.append(it)
        number_N /= it
        it = 2
    else:
        it += 1 

print(f'Список простых множителей: {list_simple_def}')
print('___________________________________________________________________________________')


sleep(2)
print('''
Задание 3.
Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.''')

sleep(2)
print('\nРешение') 
numbers = [1, 2, 2, 3, 3, 4, 5]
print(f'Список чисел: {numbers}')
unique_numbers = list(set(numbers))
print(f'Список уникальных чисел: {unique_numbers}')
print('___________________________________________________________________________________')


sleep(2)
print('''
Задание 4.
Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.''')

sleep(2)
print('\nРешение') 
sqr_k = int(input("Введите степень уравнения k < 10: "))
str_equation = ''
list_sqr_ch = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
while sqr_k > 0:
    random_num = random.randint(1, 100)
    equation_current = f'{random_num}x{list_sqr_ch[sqr_k]}'

    num_ch = random.randint(0, 1)
    if num_ch == 0:
        ch = '-'
    else:
        ch = '+'

    str_equation += equation_current + ch
    sqr_k -= 1

    if sqr_k == 0:
        random_num = str(random.randint(1, 10))
        str_equation += random_num + '=0'
print(f'Ваше уравнение сформированно: {str_equation}')

with open("equation.txt", "w", encoding='utf-8') as data:
        data.writelines(str_equation)
print("Уравнение записанно в файл equation.txt")
print('___________________________________________________________________________________')
'''
list_poly = [num_k for num_k in range(random.randint(5, 10))]
p = Polynomial(list_poly)
print(p)
'''

# Данную задачу можно было решить с использованием методов, но пока что пусть будет так
sleep(2)
print('''
Задание 5.
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.''')

sleep(2)
print('\nРешение') 
# Создаем файл и заполняем его рандомными значениями
with open("text1.txt", "w") as data:
    for index_random in range(0, 4):
        index_random = random.randint(0, 5)
        data.writelines(f"{index_random}\n")
print("Индексы находятся в файле text1.txt")

# Создаем второй файл и заполняем его рандомными значениями
with open("text2.txt", "w") as data:
    for index_random in range(0, 4):
        index_random = random.randint(0, 5)
        data.writelines(f"{index_random}\n")
print("Индексы находятся в файле text2.txt")

# Считываем значения списка 1 из файла 
list_one = []
data_file = open("text1.txt", "r")
for line in data_file:
    list_one.append(int(line))
poly_one = Polynomial(list_one)
print(f"   Многочлен №1 сформирован: {poly_one}")

# Считываем значения списка 2 из файла 
list_two = []
data_file = open("text2.txt", "r")
for line in data_file:
    list_two.append(int(line))
poly_two = Polynomial(list_two)    
print(f"   Многочлен №2 сформирован: {poly_two}")

sum_poly = polynomial.polyadd(poly_one, poly_two)
print(f'Сумма многочленов: {sum_poly}')