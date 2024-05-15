import pygame
import random

# Настройки экрана
WIDTH = 800
HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Функция для рисования случайной формы
def draw_random_shape(x, y):
    shape_type = random.randint(0, 3)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if shape_type == 0:
        pygame.draw.rect(screen, color, (x, y, 50, 50))
    elif shape_type == 1:
        pygame.draw.circle(screen, color, (x, y), 25)
    elif shape_type == 2:
        pygame.draw.polygon(screen, color, [(x, y), (x + 50, y + 25), (x + 25, y + 75)])
    else:
        pygame.draw.line(screen, color, (x, y), (x + 50, y + 50), 5)

# Цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана
    screen.fill(WHITE)

    # Рисование случайных форм
    for i in range(100):
        x = random.randint(0, WIDTH - 50)
        y = random.randint(0, HEIGHT - 50)
        draw_random_shape(x, y)

    # Отображение экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(FPS)

# Завершение Pygame
pygame.quit()
