# import pygame
# import sys
#
# # Инициализация Pygame
# pygame.init()
#
# # Задаем размеры экрана
# size = width, height = 800, 800
#
# # Создаем экран
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Sierpinski Square")
#
# # Задаем цвета
# white = (255, 255, 255)
# black = (0, 0, 0)
#
# # Задаем начальные вершины квадрата
# vertices = [(200, 200), (600, 200), (600, 600), (200, 600)]
#
# # Задаем стартовую точку
# current_point = (400, 400)
#
# # Задаем глубину рекурсии
# depth = 4
#
#
# # Функция для построения квадрата Серпинского
# def draw_sierpinski_square(vertices, current_point, depth):
#     pygame.draw.polygon(screen, white, vertices, 1)
#     if depth > 0:
#         depth -= 1
#         # Проходим по каждой стороне квадрата
#         for i in range(len(vertices)):
#             # Находим середину отрезка стороны
#             mid_x = (vertices[i][0] + vertices[(i + 1) % len(vertices)][0]) // 2
#             mid_y = (vertices[i][1] + vertices[(i + 1) % len(vertices)][1]) // 2
#             # Задаем новую вершину для квадрата
#             new_vertices = [vertices[i], (mid_x, mid_y), vertices[(i + 1) % len(vertices)]]
#             # Рекурсивно строим новый квадрат
#             draw_sierpinski_square(new_vertices, current_point, depth)
#
#
# # Главный цикл программы
# while True:
#     # Отслеживаем события
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#     # Заполняем экран черным цветом
#     screen.fill(black)
#
#     # Рисуем квадрат Серпинского
#     draw_sierpinski_square(vertices, current_point, depth)
#
#     # Обновляем экран
#     pygame.display.update()

from turtle import *

for i in range(12):
    forward(100)
    right(30)

exitonclick()