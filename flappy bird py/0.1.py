import turtle
import random

xsize = 20
ysize = 60

class Score:
    def __init__(self):
        pass


class Player:
    def __init__(self, position, size):
        self.pos = position
        self.size = size

    def update(self, t):
        global c
        a, b = 1, 10
        y = -a * (t ** 2) + b * t + c
        self.pos = self.pos[0], y

    def draw(self, painting):
        painting.up()
        painting.goto(self.pos)
        painting.down()
        painting.dot(10)

    def jump(self):
        global t, c
        t = 0
        c = self.pos[1]


class Wall:
    def __init__(self, position):
        self.pos = position

    def draw(self, painting):
        xsize1 = xsize
        ysize1 = ysize
        painting.up()
        painting.goto(self.pos)
        p1 = self.pos[0] - xsize1, self.pos[1] - ysize1
        p2 = self.pos[0] - xsize1, self.pos[1] + ysize1
        p3 = self.pos[0] + xsize1, self.pos[1] - ysize1
        p4 = self.pos[0] + xsize1, self.pos[1] + ysize1
        painting.goto(p1[0], p1[1] - 200)
        painting.down()
        painting.goto(p1)
        painting.goto(p3)
        painting.goto(p3[0], p3[1] - 200)
        painting.up()
        painting.goto(p2[0], p2[1] + 200)
        painting.down()
        painting.goto(p2)
        painting.goto(p4)
        painting.goto(p4[0], p4[1] + 200)
        painting.up()

    def update(self, t):
        self.pos = self.pos[0] - t / 10, self.pos[1]

t, c = 0, 0



def game():
    global t
    run = True
    screen = turtle.Screen()
    drawing = turtle.Turtle()
    drawing.pencolor("white")
    screen.bgcolor("black")
    screen.colormode(255)
    screen.tracer(0)  # отключить отрисовку
    drawing.speed(0)
    drawing.hideturtle()
    player = Player((0, 0), 100)
    screen.listen()
    #wall = Wall((100, 100))
    wall_list = [Wall((i, random.randint(100, 200))) for i in range(0, 3000, 100)]

    while run:
        t += 0.005
        drawing.clear()
        screen.onkey(player.jump, "Up")
        for wall in wall_list:
            wall.draw(drawing)
            wall.update(t)
        player.draw(drawing)
        player.update(t)
        screen.update()


if __name__ == '__main__':
    game()
