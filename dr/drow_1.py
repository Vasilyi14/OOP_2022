import pygame
from pygame.draw import *
import pygame
from pygame.locals import *

pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Злой смайлик')

# Цвета
black = (0, 0, 0)
yellow = (255, 255, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(black)

    # Рисуем злой смайлик
    pygame.draw.circle(screen, yellow, (200, 200), 100)  # голова
    pygame.draw.circle(screen, black, (160, 170), 10)     # левый глаз
    pygame.draw.circle(screen, black, (240, 170), 10)     # правый глаз
    pygame.draw.arc(screen, black, (150, 180, 100, 60), 3.14, 6.28, 2)  # рот

    pygame.display.flip()

pygame.quit()
