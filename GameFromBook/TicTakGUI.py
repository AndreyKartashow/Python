import random
import sys
from time import sleep
import pygame
from pygame.locals import *


pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 300
WINDOWHEIGHT = 300
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Крестики-нолики')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# нанесение на поверхность черного фона
windowSurface.fill(BLACK)


# структура поля
b1 = {'rect' : pygame.Rect(0, 202, 98, 98), 'color' : WHITE, 'pos' : 1}
b2 = {'rect' : pygame.Rect(102, 202, 96, 98), 'color' : WHITE, 'pos' : 2}
b3 = {'rect' : pygame.Rect(202, 202, 98, 98), 'color' : WHITE, 'pos' : 3}

b4 = {'rect' : pygame.Rect(0, 102, 98, 96), 'color' : WHITE, 'pos' : 4}
b5 = {'rect' : pygame.Rect(102, 102, 96, 96), 'color' : WHITE, 'pos' : 5}
b6 = {'rect' : pygame.Rect(202, 102, 98, 96), 'color' : WHITE, 'pos' : 6}

b7 = {'rect' : pygame.Rect(0, 0, 98, 98), 'color' : WHITE, 'pos' : 7}
b8 = {'rect' : pygame.Rect(102, 0, 96, 98), 'color' : WHITE, 'pos' : 8}
b9 = {'rect' : pygame.Rect(202, 0, 98, 98), 'color' : WHITE, 'pos' : 9}

boxes = [b1, b2, b3, b4, b5, b6, b7, b8, b9]


def inputPlayerLetter():
    return ['X', '0']


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


event_list = [K_KP1, K_KP2, K_KP3, K_KP4, K_KP5, K_KP6, K_KP7, K_KP8]

theBoard = [' '] * 10
playerLetter, computerLetter = inputPlayerLetter()
turn = whoGoesFirst()
gameIsPlaying = True
    
for b in boxes:
    pygame.draw.rect(windowSurface, b['color'], b['rect'])

    
while gameIsPlaying:
    if turn == 'Человек':

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key in event_list:
                    i = event_list.index(event.key)
                    boxes[i]['color'] = GREEN
                    makeMove(theBoard, playerLetter, boxes[i]['pos'])

            if isWinner(theBoard, playerLetter):
                print('\nВы выйграли!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    print('\nНичья!')
                    break
                else:
                    turn = 'Компьютер'

    else:
        # Ход компьютера
        move = getComputerMove(theBoard, computerLetter)
        boxes[move-1]['color'] = RED
        makeMove(theBoard, computerLetter, move)


        if isWinner(theBoard, computerLetter):
            print('\nКомпьютер победил! Вы проиграли.')
            gameIsPlaying = False
        else:
            if isBoardFull(theBoard):
                print('\nНичья!')
                break
            else:
                turn = 'Человек'
        sleep(2)

    for b in boxes:
        pygame.draw.rect(windowSurface, b['color'], b['rect'])
    pygame.display.update()
   

'''
    print('\nСыграем еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break

'''

