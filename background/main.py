import pygame
import sys


def draw_gradient(surface, width, height, whiteness=0.5):
    for y in range(height):
        for x in range(width):
            # Вычисляем цвет пикселя на основе его позиции
            r = int(255 * x / width)
            g = int(255 * y / height)
            b = int(255 * (1 - x / width) * (1 - y / height))

            # Добавляем белый цвет (смешиваем с белым)
            r = int(r + (255 - r) * whiteness)
            g = int(g + (255 - g) * whiteness)
            b = int(b + (255 - b) * whiteness)

            # Ограничиваем значения цвета, чтобы они не превышали 255
            r = min(255, r)
            g = min(255, g)
            b = min(255, b)

            surface.set_at((x, y), (r, g, b))


def generate(output_path="gradient.png", width=1920, height=1080, whiteness=0.5):
    """Создает PNG-картинку с градиентом."""
    pygame.init()
    surface = pygame.Surface((width, height))  # Создаем поверхность вместо экрана
    draw_gradient(surface, width, height, whiteness)  # Рисуем градиент
    pygame.image.save(surface, output_path)  # Сохраняем изображение
    print(f"Градиент сохранен в {output_path}")


def main():
    pygame.init()

    # Размеры окна
    width, height = 1920, 1080
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Градиентный фон")

    # Рисуем градиент с добавлением белого
    draw_gradient(screen, width, height, whiteness=0.3)  # Увеличьте whiteness для большей "белизны"

    # Основной цикл
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


if __name__ == "__main__":
    # Генерация изображения
    generate(output_path="gradient_image.png", width=1920, height=1080, whiteness=0.3)

    # Запуск приложения
    main()
