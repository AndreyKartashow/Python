from email import message


SYMBOLS = 'АБВГДЕЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеежзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)


def getMode():
    while True:
        print('Вы хотите зашифровать текст, расшифровать или взломать?')
        mode = input().lower()
        if mode in ['зашифровать', 'расшифровать', 'взломать']:
            return mode
        else:
            print('Введите правильный ключ')


def getMessage():
    print('Введите текст: ')
    return input()


def getKey():
    key = 0
    while True:
        print('Введите ключ шифрования (1 - %s)' %(MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def getTranslateMessage(mode, message, key):
    if mode[0] == 'р':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: # Символ не найден в SYMBOLS
            # Просто добавить этот символ без изменений
            translated += symbol
        else:
            # Зашифровать или расшифровать
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated


mode = getMode()
newMessage = getMessage()
if mode[0] != 'в':
    key = getKey()
    print('Преобразованный текст: ')
    print(getTranslateMessage(mode, newMessage, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslateMessage('расшифровать', newMessage, key))
