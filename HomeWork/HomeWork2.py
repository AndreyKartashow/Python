from logging.config import valid_ident
import string
from wsgiref import validate
from xml.etree.ElementTree import tostring


'''
Задача 1.
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
'''
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
print('____________________________________________________________________')
'''


'''
Задача 2.
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
'''
'''
print("\nЭто программа вычисляет факториал числа N и показывает промежуточные произведения")
number_N = int(input("Введите число N: "))
current_value_factorial = 1
for number in range(1, number_N + 1):
    current_value_factorial *= number
    print(current_value_factorial, end=" ")
print('____________________________________________________________________')
'''


'''
Задание 3.
Задайте список из n чисел последовательности (1+(1/n))^n и выведите на экран их сумму
'''
'''
print("\nЭта программа предназначенна для расчета суммы чисел, определяемых по закону (1+(1/n))^n при n > 0")
number_n = int(input("Введите целое число n > 0: "))
list_number = []
for n in range(1, number_n + 1):
    current_n = round((1+(1/n))**n, 3)
    list_number.append(current_n)
print(list_number)
print(sum(list_number))
print('____________________________________________________________________')
'''

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
