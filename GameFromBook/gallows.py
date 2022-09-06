import random
from typing import List


HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 0   |
 |   |
     |
    ===''', '''
 +---+
 0   |
/|   |
     |
    ===''', '''
 +---+
 0   |
/|\  |
     |
    ===''', '''
 +---+
  0  |
 /|\ |
 /   |
    ===''', '''
 +---+
 0   |
/|\  |
/ \  |
    ===''', '''
 +---+
[O   |
/|\  |
/ \  |
    ===''', '''
 +---+
[O]  |
/|\  |
/ \  |
    ===''']

words = {'Цвета':'красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(),
'Фигуры':'квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник шестиугольник восьмиугольник'.split(),
'Фрукты':'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан нектарин'.split(),
'Животные':'аист бабуин баран барсук бык волк зебра кит коза корова кошка кролик крыса лев лиса лось медведь мул мышь норка носорог обезьяна овца олень осел панда пума скунс собака сова тигр тюлень хорек ящерица'.split()}


def getRandomWord(wordDict):
    # Эта функция возвращает случайную строку из переданного словаря списков строк, а так же ключ
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return wordDict[wordKey][wordIndex], wordKey


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Ошибочные буквы: ", end = " ")
    for letter in missedLetters:
        print(letter, end = " ")
    print()

    blanks = '-' * len(secretWord)

    # Заменим пропуски отгаданными буквами
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    # Покажем секретное слово с пробелами между буквами
    for letter in blanks:
        print(letter, end = " ")
    print()

# Возвращает букву, введеную игроком.
# Эта функция проверяет что игрок ввел только одну букву.
def getGuess(alreadyGuessed):
    while True:
        guess = input("Введите букву: ").lower()
        if len(guess) !=1:
            print("Пожалуйста, введите только одну букву.")
        elif guess in alreadyGuessed:
            print("Вы уже называли эту букву. Назовите другую.")
        elif guess not in "абвгдеежзийклмнопрстуфхцчшщъыьэюя":
            print("Пожалуйста, введите БУКВУ.")
        else:
            return guess

# Эта функция возвращает True, если игрок хочет сыграть заново.
# В противном случае возвращает False.
def playAgain():
    print("Хотите сыграть еще? (Введите да или нет)")
    return input().lower().startswith('д')


print("В И С Е Л И Ц А")

difficulty = ''
difficulty_list = ["Л", "С", "Т"]
while difficulty not in difficulty_list:
    print("Выберите уровень сложности: Л - Легкий, С - Средний, Т - Тяжелый")
    difficulty = input().upper()
if difficulty == 'С':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'Т':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print(f"Секретное слово из набора: {secretSet}")
    displayBoard(missedLetters, correctLetters, secretWord)

    # Ввод буквы игроком.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Проверяем выйграл ли игрок.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Да! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

    # Проверим, превысил ли игрок лимит попыток.
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print("Вы исчерпали все попытки! \nНе угаданно букв: " + str(len(missedLetters)) + "\nУгаданно букв: " + str(len(correctLetters)) + "\nБыло загаданно слово: " + secretWord + ".")
        gameIsDone = True

    # Спросим хочет ли игрок сыграть еще раз.
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
        