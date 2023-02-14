import random
from time import sleep


def whoGoesFirst():
    # Случайный выбор игрока, которой ходит первым
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'


def isWinner(candies):
    return candies <= 0


def getPlayerMove():
    # Разрешение игроку сделать ход
    candiesPlayer = -1
    while candiesPlayer not in range(1, 29):
        candiesPlayer = int(input('\nСколько конфет вы хотите взять? (1-28) '))
    return candiesPlayer


def getComputerMove(candies):
    # Это алгоритм для ИИ
    return int(candies % 29)   


print('\nИгра "Отбери конфеты"')

while True:
    candies = 2021
    print(f'На столе лежит {candies} конфет')
    turn = whoGoesFirst()
    print('\n' + turn + ' ходит первым.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Человек':
            candiesPlayer = getPlayerMove()
            candies -= candiesPlayer
            print(f'Вы взяли {candiesPlayer} конфет, на столе осталось {candies}')

            if isWinner(candies):
                print('\nВы выйграли!')
                gameIsPlaying = False
            else:
                turn = 'Компьютер'
        else:
            #candiesComp = random.randint(1, 28) 
            candiesComp = getComputerMove(candies)
            candies -= candiesComp
            print(f'Опонент взял {candiesComp} конфет, на столе осталось {candies}')

            if isWinner(candies):
                print('\nКомпьютер победил! Вы проиграли.')
                gameIsPlaying = False
            else:
                turn = 'Человек'
            sleep(2)

    print('\nСыграем еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break

