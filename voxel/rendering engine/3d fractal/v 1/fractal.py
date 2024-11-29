from grid import Grid
from config import calculate_distance, size_grid
from math import log


class Fractal_serpinsk(object):
    def __init__(self, size, position=(0, 0, 0), depth=1):
        self.size = size
        self.position = position
        self.grid = ''
        self.depth = depth

    def create(self, grid: Grid):
        self.grid = grid
        # n = int(log(self.size, 3))
        n = self.depth
        a = [int(i) for i in range(self.size)]
        c = [int(i) for i in range(self.size)]
        for i in range(n):
            t = 3 ** (i + 1)
            for j in a:
                if t // 3 - 1 < j % t < 2 * t // 3:
                    if j in c:
                        c.pop(c.index(j))
        for x in range(self.position[0], self.size + self.position[0]):
            for y in range(self.position[1], self.size + self.position[1]):
                for z in range(self.position[2], self.size + self.position[2]):
                    if (x in c and y in c) or (x in c and z in c) or (z in c and y in c):
                        grid.add((x, y, z))

    def create_2(self, grid: Grid):
        self.grid = grid
        for x in range(self.position[0], self.size + self.position[0]):
            for y in range(self.position[1], self.size + self.position[1]):
                for z in range(self.position[2], self.size + self.position[2]):
                    grid.add((x, y, z))
        for d in range(self.depth):
            self.delete_element(d + 1, grid)

    def delete_element(self, depth, grid: Grid):
        a = [int(i) for i in range(1, self.size + 1)]
        c = [int(i) for i in range(1, self.size + 1)]
        n = int(log(self.size, 3))
        t = 3 ** depth
        h = 3 ** (n + 1 - depth)
        for j in a:
            if int(self.size / t) < j % h < int(self.size * 2 / t + 1):
                if j in c:
                    c.pop(c.index(j))
        for x in range(self.position[0], self.size + self.position[0]):
            for y in range(self.position[1], self.size + self.position[1]):
                for z in range(self.position[2], self.size + self.position[2]):
                    if (x + 1 not in c and y + 1 not in c) or (x + 1 not in c and z + 1 not in c) or (z + 1 not in c and y + 1 not in c):
                        grid.delete((x, y, z))


    def generate_polygon(self, grid: Grid):
        polygon_list = list()
        x_polygon = self.position[0]
        s_x = 1
        flag = 0
        for x in range(self.position[0], self.size + self.position[0]):
            s_y = 0
            for y in range(self.position[1], self.size + self.position[1]):
                if grid.grid[(x, y, self.position[2])]:
                    s_y += 1
            print(s_y, self.size, s_x)
            if s_y != self.size:
                if [[x_polygon, self.position[1]],
                    [x_polygon, self.position[1] + self.size],
                    [x_polygon + self.size - s_x + 1, self.position[1]]] \
                        not in polygon_list:
                    polygon_list.append([[x_polygon, self.position[1]],
                                         [x_polygon, self.position[1] + self.size],
                                         [x_polygon + self.size - s_x + 1, self.position[1]]])
                if [[x_polygon + self.size - s_x + 1, self.position[1]],
                    [x_polygon, self.position[1] + self.size],
                    [x_polygon + self.size - s_x + 1, self.position[1] + self.size]] \
                        not in polygon_list:
                    polygon_list.append([[x_polygon + self.size - s_x + 1, self.position[1]],
                                         [x_polygon, self.position[1] + self.size],
                                         [x_polygon + self.size - s_x + 1,
                                          self.position[1] + self.size]])  # search window

                s_x = 0

            s_x = +1
        return polygon_list
