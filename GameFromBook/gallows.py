import random

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
    ===''']
words = "аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица".split(' ')


def getRandonWord(wordList):
    # Эта функция возвращает случайное слово из списка
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


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
            blanks = blanks[:1] + secretWord[i] + blanks[i + 1:]

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
missedLetters = ''
correctLetters = ''
secretWord = getRandonWord(words)
gameIsDone = False

while True:
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
        print("Вы исчерпали все попытки! \nНе угаданно букв: " + str(len(missedLetters)) + "угаданно букв: " + str(len(correctLetters)) + ". Было загаданно слово: " + secretWord + ".")
        gameIsDone = True

    # Спросим хочет ли игрок сыграть еще раз.
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandonWord(words)
        else:
            break
        