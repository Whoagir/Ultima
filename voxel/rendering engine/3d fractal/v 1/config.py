from math import pi


def calculate_distance(x1, y1, z1, x2, y2, z2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** (1 / 2)
    return distance

WIDTH = 1000
HEIGHT = 1000
FPS = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pos_zero = 300, 300
size_grid = 30
center_1 = [size_grid / 2, size_grid / 2, size_grid / 2]
WIDTH_GRID = 360
HEIGHT_GRID = 480

d_a = pi / 12

point_distance = (-3, -3, -3)
max_length_pos = calculate_distance(point_distance[0], point_distance[1], point_distance[2], (32 / 30 * size_grid),
                                    (32 / 30 * size_grid), (32 / 30 * size_grid))
min_length_pos = calculate_distance(point_distance[0], point_distance[1], point_distance[2], -2, -2, -2)
