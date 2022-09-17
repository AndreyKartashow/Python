import pygame, sys 
from pygame.locals import *


# настройка PyGame
pygame.init()

# настройка окна
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Привет мир')

# назначение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# назначение шрифтов
basicFont = pygame.font.SysFont(None, 48)

# настройка текста
text = basicFont.render('Привет мир!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# нанесение на поверхность белого фона
windowSurface.fill(WHITE)

# нанесение на поверхность зеленого многоуголиника
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# нанесение на поверхность синих линий
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# нанесение на поверхность красного круга
pygame.draw.ellipse(windowSurface, RED, (325, 300, 60, 80), 1)
pygame.draw.ellipse(windowSurface, RED, (375, 275, 60, 80), 1)
pygame.draw.ellipse(windowSurface, RED, (425, 250, 60, 80), 1)

# нанесение на поверхность фонового прямоугольника для текста
pygame.draw.rect(windowSurface, RED, (textRect.left - 10, textRect.top - 30, textRect.width + 40, textRect.height + 40))

# получение массива пикселей поверхности
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# нанесение текста на поверхность
windowSurface.blit(text, textRect)

# отображение окна на экране
pygame.display.update()

# запуск игрового цикла
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()