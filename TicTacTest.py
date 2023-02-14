import random
import sys
from time import sleep
from turtle import color
import pygame
from pygame.locals import *


pygame.init()


size_block = 100
margin = 15
width = height = size_block*3+margin*4


blue = (0,0,255)
white = (255,255,255)
red = (255,0,0)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tic tac toe')

mas = [[0]*3 for i in range(3)]
query=0
exitFlag=False


def check_win(mas):
    if mas[0][0]=='x' and mas[0][1]=='x' and mas[0][2]=='x':
        print('Крестики выиграли')
    if mas[1][0]=='x' and mas[1][1]=='x' and mas[1][2]=='x':
        print('Крестики выиграли')
    if mas[2][0]=='x' and mas[2][1]=='x' and mas[2][2]=='x':
        print('Крестики выиграли')
    if mas[0][0]=='x' and mas[1][0]=='x' and mas[2][0]=='x':
        print('Крестики выиграли')
    if mas[0][1]=='x' and mas[1][1]=='x' and mas[2][1]=='x':
        print('Крестики выиграли')
    if mas[0][2]=='x' and mas[1][2]=='x' and mas[2][2]=='x':
        print('Крестики выиграли')
    if mas[0][0]=='x' and mas[1][1]=='x' and mas[2][2]=='x':
        print('Крестики выиграли')
    if mas[0][2]=='x' and mas[1][1]=='x' and mas[2][0]=='x':
        print('Крестики выиграли')
    if mas[0][0]=='o' and mas[0][1]=='o' and mas[0][2]=='o':
        print('Нолики выиграли')
    if mas[1][0]=='o' and mas[1][1]=='o' and mas[1][2]=='o':
        print('Нолики выиграли')
    if mas[2][0]=='o' and mas[2][1]=='o' and mas[2][2]=='o':
        print('Нолики выиграли')
    if mas[0][0]=='o' and mas[1][0]=='o' and mas[2][0]=='o':
        print('Нолики выиграли')
    if mas[0][1]=='o' and mas[1][1]=='o' and mas[2][1]=='o':
        print('Нолики выиграли')
    if mas[0][2]=='o' and mas[1][2]=='o' and mas[2][2]=='o':
        print('Нолики выиграли')
    if mas[0][0]=='o' and mas[1][1]=='o' and mas[2][2]=='o':
        print('Нолики выиграли')
    if mas[0][2]=='o' and mas[1][1]=='o' and mas[2][0]=='o':
        print('Нолики выиграли')



def xod_comp(mas,query):
    for row_ in range(3):
        for col_ in range(3):
            x = col_*size_block+(col_+1)*margin
            y = row_*size_block+(row_+1)*margin

            if mas[row_][col_]==0:
                print('circle')
                pygame.draw.circle(screen,red,(x+size_block//2,y+size_block//2),size_block//2-3,8)
                mas[row_][col_]='o'
                query+=1
                return

for row in range(3):
        for col in range(3):
            x = col*size_block+(col+1)*margin
            y = row*size_block+(row+1)*margin
            pygame.draw.rect(screen,blue,(x,y,size_block,size_block))

    

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        elif event.type==pygame.MOUSEBUTTONDOWN:
            x_mouse,y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block+margin)
            row = y_mouse // (size_block+margin)
            if mas[row][col] == 0:
                mas[row][col]='x'
                x = col*size_block+(col+1)*margin
                y = row*size_block+(row+1)*margin

                if mas[row][col]=='x':
                    print('x')
                    pygame.draw.line(screen,red,(x+5,y+5),(x+size_block-5,y+size_block-5),8)
                    pygame.draw.line(screen,red,(x+size_block-5,y+5),(x+5,y+size_block-5),8)
                    xod_comp(mas,query)

            query+=1     
    check_win(mas)        
    if query == 5:
        print('Piece')
    pygame.display.update()