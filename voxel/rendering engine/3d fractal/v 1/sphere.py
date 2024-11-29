from grid import Grid
from config import calculate_distance, size_grid


class Sphere(object):
    def __init__(self, size, position=(0, 0, 0)):
        self.size = size
        self.position = position

    def create(self, grid: Grid):
        for x in range(size_grid):
            for y in range(size_grid):
                for z in range(size_grid):
                    if calculate_distance(x, y, z, self.position[0], self.position[1], self.position[2]) < self.size:
                        grid.add((x, y, z))