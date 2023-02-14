import random
import sys


WIDTH = 8 # ширина игрового поля
HEIGHT = 8 # высота игрового поля


def drawBoard(board):
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' %(y + 1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' %(y + 1))
    print(' +--------+')
    print('  12345678')


def getNewBoard():
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board


def isValidMove(board, tile, xstart, ystart):
    # Возвращает ложь, если ход не возможен
    # Иначе дает список ходов
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'
    
    tilesTopFlip = []
    for xdiriction, ydiriction in  [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdiriction # первый шаг в сторону х
        y += ydiriction # первый шаг в сторону у
        while isOnBoard(x, y) and board[x][y] == otherTile:
            # продолжать двигаться в этом направлении
            x += xdiriction
            y += ydiriction
            if isOnBoard(x, y) and board[x][y] == tile:
                # если есть фишки, которые можно перевернуть
                while True:
                    x -= xdiriction
                    y -= ydiriction
                    if x == xstart and y == ystart:
                        break
                    tilesTopFlip.append([x ,y])
            if len(tilesTopFlip) == 0: # Если ни одна фишка не перевернулась, это недопустимо
                return False
    return tilesTopFlip


def isOnBoard(x, y):
    # вернет истину если координаты есть
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1


def getBoardWithValidMoves(board, tile):
    # вернуть новое поле с допустимыми ходами
    boardCopy = getBoardCopy(board)
    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy


def getValidMoves(board, tile):
    # возвращает список с допустимыми ходами
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def GetScoreOfBoard(board):
    # определение количества очков
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}


def enterPlayerTile():
    # выбор фишки игроком
    tile = ''
    while not (tile == 'X' or tile == 'Y'):
        print('Вы играете за X или O?')
        tile = input().upper()

    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # кто ходит первым
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'


def makeMove(board, tile, xstart, ystart):
    # возвращает истину если можно сделать ход и перевернуть фишку, иначе лож
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True


def getBoardCopy(board):
    # возвращает копию игрового поля
    boardCopy = getNewBoard()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]
    return boardCopy


def isOnCorner(x, y):
    # возвращает истину если позиция находится в угле
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)


def getPlayerMove(board, playerTile):
    # Позволить игроку сделать ход
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Сделайте ход, или напишите "выход" для выхода из игры или "подсказка" для вывода подсказки')
        move = input().lower()
        if move == 'выход' or move == 'подсказка':
            return move

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('Это недопустимый ход. Введите номер столбца (1-8) и номер ряда (1-8).')
            print('К примеру значение 81 перемещает в верхний правый угол.')

    return [x, y]


def getComputerMove(board, computerTile):
    # компьютер определяет куда сделать ход
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves) # сделать случайный порядок ходов

    # всегда делать ход в угол, если это возможно
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # найти ход с наибольшим возможным количеством очков
    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = GetScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove


def printScore(board, playerTile, computerTile):
    scores = GetScoreOfBoard(board)
    print('Ваш счет: %s. Счет компьютера: %s.' %(scores[playerTile], scores[computerTile]))


def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print(f'{turn} ходит первым.')

    # очистка игрового поля
    board = getNewBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return board # ходов нет ни у одного из игроков
            
        elif turn == 'Человек':
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardWithValidMoves(board, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, playerTile, computerTile)

                move = getPlayerMove(board, playerTile)
                if move == 'выход':
                    print('Благодарим за игру!')
                    sys.exit()
                elif move == 'подсказка':
                    showHints = not showHints
                    continue
                else:
                    makeMove(board, playerTile, move[0], move[1])
            turn = 'Компьютер'

        elif turn == 'Компьютер':
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, playerTile, computerTile)

                input('Нажмите клавишу Enter для просмотра хода компьютера.')
                move = getComputerMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
            turn = 'Человек'

print('Приветствуем в игре "Риверси"!')
playerTile, computerTile = enterPlayerTile()

while True:
    finalBoard = playGame(playerTile, computerTile)
    drawBoard(finalBoard)
    scores = GetScoreOfBoard(finalBoard)
    print('X набрал %s очков. O набрал %s очков.' %(scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('Вы победили компьютер, обогнав его на %s очков! Поздравляем!' %(scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('Вы проиграли. Компьютер победил вас, обогнав на %s очков.' %(scores[computerTile] - scores[playerTile]))
    else:
        print('Ничья!')
    
    print('Хотите сыграть еще раз? (да/нет)')
    if not input().lower().startswith('д'):
        break


