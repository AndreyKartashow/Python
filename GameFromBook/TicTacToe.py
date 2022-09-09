import random
from shutil import move
from time import sleep


def drawBoard(board):
    # Эта функция отрисовывает игровое поле
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-') 
    print(board[1] + '|' + board[2] + '|' + board[3])


def inputPlayerLetter():
    # Выбор пользователем игровой стороны
    letter = ''
    while not (letter == 'X' or letter == '0'):
        print("\nВы выбираете X или 0")
        letter = input().upper()

    if letter == 'X':
        return ['X', '0']
    else:
        return ['0', 'X']


def whoGoesFirst():
    # Случайный выбор игрока, которой ходит первым
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    # Перечисляем все условия победы
    # Используем "bo" вместо "board" и "le" вместо "letter"
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
            (bo[4] == le and bo[5] == le and bo[6] == le) or 
            (bo[1] == le and bo[2] == le and bo[3] == le) or 
            (bo[7] == le and bo[4] == le and bo[1] == le) or 
            (bo[8] == le and bo[5] == le and bo[2] == le) or 
            (bo[9] == le and bo[6] == le and bo[3] == le) or 
            (bo[7] == le and bo[5] == le and bo[3] == le) or 
            (bo[9] == le and bo[5] == le and bo[1] == le)) 

        
def getBoardCopy(board):
    # Метод воспроизведения игрового поля
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


def isSpaseFree(board, move):
    # Возвращает истину, если ход сделан
    return board[move] == ' '


def getPlayerMove(board):
    # Разрешение игроку сделать ход
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaseFree(board, int(move)):
        print('\nВаш следующий ход? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, moveList):
    # Возвращает допустимый ход, учитывая список сделанных ходов и список заполненных клеток.
    # Возвращает None если больше нет допустимых ходов
    posibleMove = []
    for i in moveList:
        if isSpaseFree(board, i):
            posibleMove.append(i)

    if len(posibleMove) != 0:
        return random.choice(posibleMove)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Учитывая заполнение поля и инициалы компьютера, определяем допустимый ход
    if computerLetter == 'X':
        playerLetter = '0'
    else:
        playerLetter = 'X'

    # Это алгоритм для ИИ
    # Сначала проверяем - победим ли мы, сделав следующий ход
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaseFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Проверяем - победит ли игрок, сделав следующий ход, и блокируем его
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaseFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Пробуем занять один из углов, если он свободен
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Пробуем занять центр, если он свободен
    if isSpaseFree(board, 5):
        return 5

    # Делаем ход по одной стороне
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Возращаем истину, если ячейка поля занята. иначе возвращаем ложь
    for i in range(1, 10):
        if isSpaseFree(board, i):
            return False
    return True


print('Игра "Крестики-нолики"')

while True:
    # Обновление игрового поля
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('\n' + turn + ' ходит первым.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'Человек':
            # Ход игрока
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('\nВы выйграли!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('\nНичья!')
                    break
                else:
                    turn = 'Компьютер'

        
        else:
            # Ход компьютера
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('\nКомпьютер победил! Вы проиграли.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('\nНичья!')
                    break
                else:
                    turn = 'Человек'
            sleep(2)

    print('\nСыграем еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break

