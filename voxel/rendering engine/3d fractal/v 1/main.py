# губка Менгера
import pygame
from config import *
from grid import Grid
from cube import Cube
from logic import *
from sphere import Sphere
from fractal import Fractal_serpinsk
import math
from random import random

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
clock = pygame.time.Clock()

grid = Grid()
grid.generate()

# cube = Cube(40, (0, 0, 0))
# cube.create(grid=grid)
# polygon_l = cube.generate_polygon(grid=grid)
# print(polygon_l)

#
# sphere = Sphere(10, (20, 20, 20))
# sphere.create(grid=grid)

fractal = Fractal_serpinsk(27, depth=3)
fractal.create_2(grid)
# fractal.create(grid)
polygon_l = fractal.generate_polygon(grid=grid)
print(polygon_l)



alfa = [0, 0]  # left/right top/bot
running = True #
speed = 0

nu = int(random() * 255)
ku = int(random() * 255)
cu = int(random() * 255)

while running:
    screen.fill(BLACK)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                alfa[0] -= d_a
            if event.key == pygame.K_d:
                alfa[0] += d_a
            if event.key == pygame.K_w:
                alfa[1] -= d_a
            if event.key == pygame.K_s:
                alfa[1] += d_a
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                speed = d_a / 6
            if event.button == 2:
                speed = 0

    alfa[0] += speed
    delta = 0.01

    for x in range(size_grid):
        for y in range(size_grid):
            for z in range(size_grid):
                if grid.grid[(x, y, z)]:

                    x1, z1 = transform_visual((x + delta, z + delta), alfa[0] + delta)
                    y1, z1 = transform_visual((y + delta, z + delta), alfa[1] + delta)

                    pos_2 = (x1, y1, z1)

                    l = calculate_distance(x1, y1, z1, point_distance[0], point_distance[1], point_distance[2])
                    intensiv = (l - min_length_pos) / (max_length_pos - min_length_pos)
                    cord = (pos_2[0] / size_grid) * WIDTH_GRID * (354 / 267), (pos_2[1] / size_grid) * HEIGHT_GRID
                    pygame.draw.circle(screen, ((nu * intensiv) % 255, (ku * intensiv) % 255, (cu * intensiv) % 255),
                                       (cord[0] + pos_zero[0], cord[1] + pos_zero[1]), 8)

    polygon_l_n = list()
    for i in polygon_l:
        polygon_n = list()
        for j in i:
            x = j[0]
            y = j[1]
            z = 0
            x1, z1 = transform_visual((x + delta, 0 + delta), alfa[0] + delta)
            y1, z1 = transform_visual((y + delta, 0 + delta), alfa[1] + delta)
            pos_2 = (x1, y1, z1)
            cord = [(pos_2[0] / size_grid) * WIDTH_GRID * (354 / 267) + pos_zero[0], (pos_2[1] / size_grid) * HEIGHT_GRID + pos_zero[1]]
            polygon_n.append(cord)
        polygon_l_n.append(polygon_n)
    for i in polygon_l_n:
        pygame.draw.polygon(screen, WHITE, i)

    cord = (center_1[0] / size_grid) * WIDTH_GRID, (center_1[1] / size_grid) * HEIGHT_GRID
    pygame.draw.circle(screen, RED, (cord[0] + pos_zero[0], cord[1] + pos_zero[1]), 4)
    pygame.display.update()


pygame.quit()
