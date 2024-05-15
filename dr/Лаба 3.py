import pygame

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)
GRAY = (128, 128, 128)

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Отрисовка кота
def draw_cat(screen, x, y):
    # Тело кота
    pygame.draw.ellipse(screen, ORANGE, (x, y), (100, 50))
    # Уши кота
    pygame.draw.polygon(screen, ORANGE, [(x - 20, y - 10), (x, y - 30), (x + 20, y - 10)])
    # Глаза кота
    pygame.draw.circle(screen, GREEN, (x - 15, y - 5), 5)
    pygame.draw.circle(screen, GREEN, (x + 15, y - 5), 5)
    # Нос кота
    pygame.draw.circle(screen, BLACK, (x, y), 3)
    # Рот кота
    pygame.draw.arc(screen, BLACK, (x, y + 5), 10, 0, 180)
    # Лапы кота
    pygame.draw.line(screen, BLACK, (x - 30, y + 25), (x - 50, y + 50))
    pygame.draw.line(screen, BLACK, (x + 30, y + 25), (x + 50, y + 50))

# Отрисовка клубка ниток
def draw_yarn(screen, x, y):
    pygame.draw.circle(screen, GRAY, (x, y), 25)
    pygame.draw.arc(screen, BLACK, (x, y), 25, 0, 180)

# Цикл игры
while True:

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Заполнение экрана
    screen.fill(WHITE)

    # Отрисовка кота и клубка ниток
    draw_cat(screen, 300, 200)
    draw_yarn(screen, 500, 300)

    # Обновление экрана
    pygame.display.update()
Задание № 4:
Нарисовать картинку по заданию
Выполнение:
import pygame

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (165, 42, 42)
LIGHT_BROWN = (222, 184, 135)
TAN = (240, 230, 140)
GRAY = (128, 128, 128)

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Загрузка картинок
cat_image = pygame.image.load("[Image URL cat]")
yarn_image = pygame.image.load("[Image URL yarn]")

# Масштабирование картинок
cat_image = pygame.transform.scale(cat_image, (200, 200))
yarn_image = pygame.transform.scale(yarn_image, (50, 50))

# Позиции картинок
cat_x = 300
cat_y = 200
yarn_x = 500
yarn_y = 300

# Отрисовка кота
def draw_cat(screen, x, y):
    # Тело кота
    pygame.draw.ellipse(screen, BROWN, (x, y), (100, 50))
    # Уши кота
    pygame.draw.polygon(screen, BROWN, [(x - 20, y - 10), (x, y - 30), (x + 20, y - 10)])
    # Глаза кота
    pygame.draw.circle(screen, LIGHT_BROWN, (x - 15, y - 5), 5)
    pygame.draw.circle(screen, LIGHT_BROWN, (x + 15, y - 5), 5)
    # Нос кота
    pygame.draw.circle(screen, BLACK, (x, y), 3)
    # Рот кота
    pygame.draw.arc(screen, BLACK, (x, y + 5), 10, 0, 180)
    # Лапы кота
    pygame.draw.line(screen, BLACK, (x - 30, y + 25), (x - 50, y + 50))
    pygame.draw.line(screen, BLACK, (x + 30, y + 25), (x + 50, y + 50))

# Отрисовка клубка ниток
def draw_yarn(screen, x, y):
    pygame.draw.circle(screen, TAN, (x, y), 25)
    pygame.draw.arc(screen, BLACK, (x, y), 25, 0, 180)

# Цикл игры
while True:

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Заполнение экрана
    screen.fill(WHITE)

    # Отрисовка кота и клубка ниток
    draw_cat(screen, 300, 200)
    draw_yarn(screen, 500, 300)

    # Обновление экрана
    pygame.display.update()

