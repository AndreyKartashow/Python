from atexit import _clear
from distutils.command import clean
from logging.config import valid_ident
import string
import random
from time import sleep
from turtle import clear
from wsgiref import validate
from xml.etree.ElementTree import tostring


'''
Задача 1.
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
'''

print("\nЭто программа предназначенна для определения суммы цифр в числе")
# Первый уровень валидации
number = float(input("Введите пожалуйста число n = "))
str_number = str(number)
summ = 0
# Второй уровень валидации и вывод суммы цифр в числе
list_validation = ['+','-','.', ',']
for char in str_number:
    if char not in list_validation:
        summ += int(char)
print(f"Сумма цифр в числе составляет summ = {summ}")
print('___________________________________________________________________________________')



'''
Задача 2.
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
'''

print("\nЭто программа вычисляет факториал числа N и показывает промежуточные произведения")
number_N = int(input("Введите число N: "))
current_value_factorial = 1
for number in range(1, number_N + 1):
    current_value_factorial *= number
    print(current_value_factorial, end=" ")
print('\n___________________________________________________________________________________')



'''
Задание 3.
Задайте список из n чисел последовательности (1+(1/n))^n и выведите на экран их сумму
'''

print('''\nЭта программа предназначенна для расчета суммы чисел, 
определяемых по закону (1+(1/n))^n при n > 0''')
number_n = int(input("Введите целое число n > 0: "))
list_number = []
for n in range(1, number_n + 1):
    current_n = round((1+(1/n))**n, 3)
    list_number.append(current_n)
print(list_number)
print(sum(list_number))
print('___________________________________________________________________________________')


'''
Задание 5.
Реализовать алгоритм перемешивания списка
'''

print("\nПервоначальный список заполнен числами от 0 до N")
first_list = []
for number in range(0, 10):
    first_list.append(number)
print(first_list)
print("\nЗатем список перемешали:")
first_list.reverse()
print(first_list)
print('___________________________________________________________________________________')


'''
Задание 4.
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
'''

sleep(5)
print('''\nЭта программа предназначенна для записи индексов в отдельный файл, 
их чтения и определения произведения чисел для соответствующих позиций''')
# Создаем список и заполняем рандомными числами
list_random_number = []
for number_random in range(6):
    number_random = random.randint(1, 10)
    list_random_number.append(number_random)
print(f"Ваш список: {list_random_number}")


# Создаем файл и заполняем его рандомными индексами
with open("text.txt", "w") as data:
    for index_random in range(0, 4):
        index_random = random.randint(0, 5)
        data.writelines(f"{index_random}\n")
print("Индексы находятся в файле text.txt")

# Считываем индексы списка из файла и вычисляем произведение соот. элементов
multiplication = 1
data_file = open("text.txt", "r")
for line in data_file:
    multiplication *= list_random_number[int(line)]
print(f"   Произведение соответствующих чисел = {multiplication}")


