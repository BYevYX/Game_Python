import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Example")

# Загрузка изображения
image = pygame.image.load('image/Heros/water_princess/07_1_atk/1_atk_1.png')
image_rect = image.get_rect()

# Центрирование изображения
image_rect.center = (screen_width // 2, screen_height // 2)

# Создание маленького rect в середине изображения
small_rect_size = (50, 50)  # Размер маленького rect
small_rect = pygame.Rect(0, 0, *small_rect_size)
small_rect.center = image_rect.center

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отображение белого фона
    screen.fill((255, 255, 255))

    # Отображение изображения
    screen.blit(image, image_rect)

    # Отображение маленького rect
    pygame.draw.rect(screen, (255, 0, 0), small_rect, 2)  # Рисуем обводку маленького rect красным цветом

    # Обновление дисплея
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
sys.exit()