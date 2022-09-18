from time import sleep


# алгоритм сжатия
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: 
        return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


# алгоритм растяжения
def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


print('''
Задание 1.
Напишите программу, удаляющую из текста все слова, содержащие "абв"''')

sleep(2)
print('\nРешение')
text = 'апельсин абривиатура мандарин ананас кокос тыква карлосон алабай букварь'
print(f'Исходный текст: {text}')

textToList = text.split()
index = 0
length = len(textToList)
del_list = []
while index < length:
    if 'а' in textToList[index] and 'б' in textToList[index] and 'в' in textToList[index]:
        del_list.append(textToList[index])
        textToList.remove(textToList[index])
        length -= 1
    else:
        index += 1
text = ' '.join(textToList)
print(f'Результат: {text}')
print(f'Удалены слова: {del_list}')
print('___________________________________________________________________________________')



sleep(2)
print('''
Задание 2.
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"''')

sleep(2)
print('\nРешение')
print('Решение представленно в файле Candies.py в папке GameFromBook')
print('___________________________________________________________________________________')


sleep(2)
print('''
Задание 3.
Создайте программу для игры в "Крестики-нолики".''')

sleep(2)
print('\nРешение')
print('Решение представленно в файле TicTacToe.py в папке GameFromBook')
print('___________________________________________________________________________________')


sleep(2)
print('''
Задание 4.
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.''')

sleep(2)
print('\nРешение')
# Создаем файл textBase.txt с исходным текстом
textBase = 'аааабббббббббввввггггггаааааааггггггггггггddddddddddddyyyyyyyyyyy'

with open("textBase.txt", "w", encoding = 'utf-8' ) as data:
    data.writelines(f"{textBase}")
print("Исходный текст находятся в файле textBase.txt")

# Считываем значения из файла textBase.txt
list_text = []
data_file = open("textBase.txt", "r", encoding = 'utf-8')
for char in data_file:
    list_text.append(char)
text_enc = ' '.join(list_text)
print(f"Текст считан из файла textBase.txt: {text_enc}")

# Сжимаем данные из файла textBase.txt
encode_val = rle_encode(text_enc)

# Сохраняем сжатый файл textEncod.txt
with open("textEncod.txt", "w", encoding = 'utf-8' ) as data:
    data.writelines(f"{encode_val}")
print("Сжатый файл создан: textEncod.txt")


# Читаем сжатый файл textEncod.txt
list_text = []
data_file = open("textEncod.txt", "r", encoding = 'utf-8')
for char in data_file:
    list_text.append(char)
text_enc = ' '.join(list_text)
print(f"Текст считан из файла textEncod.txt: {text_enc}")

decode_val = rle_decode(text_enc)
print(f"Сжатые данные прочитаны {decode_val}")
print('___________________________________________________________________________________')