from config import size_grid


class Grid(object):
    def __init__(self):
        self.grid = dict()

    def generate(self):
        for x in range(size_grid):
            for y in range(size_grid):
                for z in range(size_grid):
                    self.grid[(x, y, z)] = 0

    def add(self, point):
        self.grid[point] = 1

    def delete(self, point):
        self.grid[point] = 0
