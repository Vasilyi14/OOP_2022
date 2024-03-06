import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка параметров окна
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Кот в доме")

# Загрузка изображения кота
cat_image = pygame.image.load("cat_image.png")
cat_rect = cat_image.get_rect()
cat_rect.center = (window_width // 2, window_height // 2)

# Задаем цвет дома (коричневый)
house_color = (139, 69, 19)

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Заливка экрана цветом дома
    window.fill(house_color)

    # Рисуем три окна
    window.fill((255,255,255), pygame.Rect(100, 100, 50, 50))
    window.fill((255,255,255), pygame.Rect(200, 100, 50, 50))
    window.fill((255,255,255), pygame.Rect(300, 100, 50, 50))

    # Вывод изображения кота на экран
    window.blit(cat_image, cat_rect)

    pygame.display.flip()