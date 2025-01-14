import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Ink Rain")

# Цвета
BLACK = (0, 0, 0)
WATER_COLOR = (0, 0, 255)  # Цвет воды
INK_COLOR = (20, 20, 20)   # Цвет чернил

# Поверхность для чернил
ink_surface = pygame.Surface((screen_width, 100), pygame.SRCALPHA)

# Класс капли
class Drop:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(-100, 0)
        self.speed = random.randint(2, 5)
        self.radius = random.randint(2, 4)

    def fall(self):
        self.y += self.speed
        # Если капля достигла воды, нарисуем её на поверхности воды
        if self.y >= screen_height - 100:
            pygame.draw.circle(
                ink_surface,
                (INK_COLOR[0], INK_COLOR[1], INK_COLOR[2], 50),  # Полупрозрачные чернила
                (self.x, self.y - (screen_height - 100)),
                self.radius,
            )
            self.reset()

    def reset(self):
        # Сброс в начальное положение
        self.x = random.randint(0, screen_width)
        self.y = random.randint(-100, 0)
        self.speed = random.randint(2, 5)
        self.radius = random.randint(2, 4)

# Генерация капель
drops = [Drop() for _ in range(100)]

# Основной игровой цикл
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(BLACK)

    # Рисуем уровень воды
    # pygame.draw.rect(screen, WATER_COLOR, (0, screen_height - 100, screen_width, 100))

    # Обновляем движение капель
    for drop in drops:
        drop.fall()
        pygame.draw.circle(screen, INK_COLOR, (drop.x, drop.y), drop.radius)

    # Накладываем поверхность чернил на уровень воды
    screen.blit(ink_surface, (0, screen_height - 100))  # Корректное смешивание

    # Обновляем экран
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
