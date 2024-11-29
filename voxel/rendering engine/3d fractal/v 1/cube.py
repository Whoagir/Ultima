from grid import Grid


class Cube(object):
    def __init__(self, size, position=(0, 0, 0)):
        self.size = size
        self.position = position

    def create(self, grid: Grid):
        for x in range(self.position[0], self.size + self.position[0]):
            for y in range(self.position[1], self.size + self.position[1]):
                for z in range(self.position[2], self.size + self.position[2]):
                    grid.add((x, y, z))

    def generate_polygon(self, grid: Grid):
        polygon_list = list()
        x_window = self.position[0]
        s_x = 0
        for x in range(self.position[0], self.size + self.position[0]):
            s_y = 0
            for y in range(self.position[1], self.size + self.position[1]):
                if grid.grid[(x, y, self.position[2])]:
                    s_y += 1

            if s_y != self.size or x == self.size + self.position[0] - 1:
                polygon_list.append([[self.position[0],self.position[1]],
                                     [self.position[0] , self.position[1] + self.size],
                                     [self.position[0] + self.size - s_x + 1 ,self.position[1]]])
                polygon_list.append([[self.position[0] + self.size - s_x + 1 ,self.position[1]],
                                     [self.position[0], self.position[1] + self.size],
                                     [self.position[0] + self.size - s_x + 1, self.position[1] + self.size]])  # search window
                s_x = 0

            s_x = +1
        return polygon_list
