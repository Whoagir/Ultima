import pygame
import random

# Настройка Pygame
pygame.init()

# Размеры экрана
screen_width, screen_height = 400, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Sand Hourglass")

# Цвета
BACKGROUND = (30, 30, 30)
SAND_COLOR = (194, 178, 128)

# Параметры песчинок
pixel_size = 4  # Размер пикселя песчинки
pixels = []  # Список для падающих песчинок

# Верхний "резервуар" песка
sand_top_rect = pygame.Rect(150, 50, 100, 100)

# Нижний "накопитель" песка
sand_bottom = []

# Функция для создания новой песчинки
def create_sand():
    x = random.randint(sand_top_rect.left, sand_top_rect.right - pixel_size)
    y = sand_top_rect.bottom  # Песчинка падает из низа верхнего резервуара
    pixels.append([x, y])

# Основной игровой цикл
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка фона
    screen.fill(BACKGROUND)

    # Рисуем верхнюю часть песка
    pygame.draw.rect(screen, SAND_COLOR, sand_top_rect)

    # Добавляем песчинки с постепенной скоростью
    if sand_top_rect.height > 0:  # Пока есть песок, создаем новые песчинки
        create_sand()
        sand_top_rect.height -= 0.1  # Песок уменьшается сверху

    # Обновляем позицию песчинок
    for pixel in pixels[:]:  # Копируем список, чтобы безопасно удалять элементы
        pixel[1] += 2  # Падение песчинки вниз
        # Если песчинка достигла "земли", добавляем ее в нижний контейнер
        if pixel[1] >= screen_height - 100:  # Условие "достижения дна"
            sand_bottom.append(pixel)
            pixels.remove(pixel)

    # Ограничение длины нижнего песка
    if len(sand_bottom) > (screen_width // pixel_size) * (100 // pixel_size):
        sand_bottom = sand_bottom[-(screen_width // pixel_size) * (100 // pixel_size):]

    # Рисуем песчинки
    for pixel in pixels:
        pygame.draw.rect(screen, SAND_COLOR, (pixel[0], pixel[1], pixel_size, pixel_size))

    # Рисуем накопившийся песок внизу
    for sand in sand_bottom:
        pygame.draw.rect(screen, SAND_COLOR, (sand[0], sand[1], pixel_size, pixel_size))

    # Обновляем экран
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
