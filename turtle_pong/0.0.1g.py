import random
from turtle import Screen, Turtle

# CONST
BALL_RADIUS = 10
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 100

# GAME_SPEED
BALL_SPEED = 30
PLAYER1_SPEED = 30
PLAYER2_SPEED = 10

# COLOR_CONST
COLOR_WHITE = "white"
COLOR_CYAN = "cyan"
COLOR_BLACK = "black"
COLOR_YELLOW = "yellow"
COLOR_GREEN = "green"


class GameObject:
    def __init__(self, start_point: tuple[float, float], end_point: tuple[float, float], velocity: tuple[float, float],
                 speed_: int, color_: str = COLOR_CYAN):
        self.rect = [start_point, end_point]
        self.velocity = velocity
        self.color = color_
        self.speed = speed_
        self.update_position()

    def update_position(self) -> None:
        self.rect[0] = (self.rect[0][0] + self.velocity[0] * (self.speed / 100),
                        self.rect[0][1] + self.velocity[1] * (self.speed / 100))
        self.rect[1] = (self.rect[1][0] + self.velocity[0] * (self.speed / 100),
                        self.rect[1][1] + self.velocity[1] * (self.speed / 100))
        self.center = ((self.rect[0][0] + self.rect[1][0]) / 2, (self.rect[0][1] + self.rect[1][1]) / 2)

    def set_velocity(self, new_velocity: tuple[int, int]) -> None:
        self.velocity = new_velocity

    def update_velocity(self, addition: tuple[int, int]) -> None:
        self.velocity = (self.velocity[0] + addition[0], self.velocity[1] + addition[1])


class BallObject(GameObject):
    def __init__(self, start_point: tuple[float, float], end_point: tuple[float, float], velocity: tuple[float, float],
                 speed_: int):
        super().__init__(start_point, end_point, velocity, speed_)
        self.radius = BALL_RADIUS

    def draw(self, turtle: Turtle) -> None:
        turtle.penup()
        turtle.goto(self.center)
        turtle.pendown()
        turtle.dot(self.radius)


class Player(GameObject):
    def __init__(self, start_point: tuple[float, float], end_point: tuple[float, float], velocity: tuple[float, float],
                 speed_: int, color_: str):
        super().__init__(start_point, end_point, velocity, speed_, color_)
        self.velocity = (0, self.velocity[1])

    def draw(self, turtle: Turtle) -> None:
        turtle.penup()
        turtle.goto(self.rect[0][0], self.rect[0][1])
        turtle.pendown()
        turtle.color(self.color)
        for _ in range(2):
            turtle.goto(self.rect[1][0], self.rect[0][1])
            turtle.goto(self.rect[1][0], self.rect[1][1])
            turtle.goto(self.rect[0][0], self.rect[1][1])
            turtle.goto(self.rect[0][0], self.rect[0][1])

    def set_velocity_up(self) -> None:
        self.set_velocity((0, 1))

    def set_velocity_down(self) -> None:
        self.set_velocity((0, -1))


class UIObject:
    def __init__(self):
        pass

    def draw(self, turtle: Turtle) -> None:
        turtle.color(COLOR_WHITE)
        turtle.penup()

    def update_position(self):
        pass


class Border(UIObject):
    def __init__(self,
                 coords: tuple[tuple[float, float], tuple[float, float], tuple[float, float], tuple[float, float]]):
        super().__init__()
        self.coords = coords

    def draw(self, turtle: Turtle) -> None:
        super().draw(turtle)
        turtle.goto(self.coords[0])
        turtle.pendown()
        for coord in self.coords[1:]:
            turtle.goto(coord)
        turtle.goto(self.coords[0])


class Score(UIObject):
    def __init__(self, score: tuple[int, int], position: tuple[float, float] = (0, 350)):
        super().__init__()
        self.score = score
        self.position = position

    def draw(self, turtle: Turtle) -> None:
        super().draw(turtle)
        score_p1, score_p2 = self.score
        turtle.goto(self.position)
        turtle.setheading(180)
        turtle.up()
        turtle.forward(10)
        turtle.color(COLOR_YELLOW)

        # Drawing Player 1's score
        for _ in range(score_p1):
            turtle.down()
            for _ in range(2):
                turtle.forward(10)
                turtle.right(90)
                turtle.forward(50)
                turtle.right(90)
            turtle.up()
            turtle.forward(20)

        turtle.up()
        turtle.goto(self.position)
        turtle.setheading(0)
        turtle.color(COLOR_GREEN)
        turtle.forward(10)

        # Drawing Player 2's score
        for _ in range(score_p2):
            turtle.down()
            for _ in range(2):
                turtle.forward(10)
                turtle.right(-90)
                turtle.forward(50)
                turtle.right(-90)
            turtle.up()
            turtle.forward(20)

        turtle.color(COLOR_CYAN)


class Game:
    def __init__(self):
        # Инициализация других атрибутов
        self.BALL_SPEED = 30  # Добавляем BALL_SPEED как атрибут класса
        self.i = 0
        self.player1 = Player((-330, 0), (player_width - 330, player_height), (0, 0), speed_p1,
                               color_=color_yellow)
        self.player2 = Player((330, 0), (player_width + 330, player_height), (0, 1), speed_p2, color_=color_green)
        self.border = Border(((-400, 300), (400, 300), (400, -300), (-400, -300)))
        self.score = Score((0, 0))
        self.screen = Screen()
        self.turtle = Turtle()
        self.window = True
        self.objects = (self.ball, self.player2, self.player1, self.border, self.score)

    def start_game(self) -> None:
        self.screen.bgcolor(COLOR_BLACK)
        self.screen.tracer(0)
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.update_objects()
        self.screen.listen()

    def update_objects(self) -> None:
        self.objects = (self.ball, self.player2, self.player1, self.border, self.score)

    def spawn_new_ball(self) -> None:

        self.BALL_SPEED = 30
        self.i = 0
        vx = random.choice([x for x in range(-1, 2) if x != 0])
        vy = random.random() * random.randint(-2, 2)
        self.ball = BallObject((BALL_RADIUS * -1, 0), (BALL_RADIUS, BALL_RADIUS * 2), (vx, vy), self.BALL_SPEED)
        self.update_objects()

    def run(self) -> None:
        while self.window:
            if max(self.score.score) >= 9:
                self.turtle.clear()
                self.turtle.up()
                self.turtle.goto((0, 0))
                self.turtle.down()
                if self.score.score[0] == 9:
                    self.turtle.write("Player 2 wins!", align="center", font=("Arial", 60, "normal"))
                else:
                    self.turtle.write("Player 1 wins!", align="center", font=("Arial", 60, "normal"))
            else:
                self.i += 1
                if self.i % 50 == 0:
                    self.BALL_SPEED += 1

                self.turtle.clear()
                self.check_collisions()
                self.player2_move()
                self.screen.onkey(self.player1.set_velocity_up, "Up")
                self.screen.onkey(self.player1.set_velocity_down, "Down")

                for obj in self.objects:
                    obj.update_position()
                    obj.draw(self.turtle)

                self.screen.update()

    def check_collisions(self) -> None:
        self.check_collision_ball_and_border()
        self.check_collision_player_1_and_ball()
        self.check_collision_player_2_and_ball()
        self.check_collision_player_and_border(self.player1)
        self.check_collision_player_and_border(self.player2)

    def check_collision_player_1_and_ball(self) -> None:
        if self.is_collision(self.player1):
            self.ball.set_velocity((-self.ball.velocity[0], self.ball.velocity[1]))

    def check_collision_player_2_and_ball(self) -> None:
        if self.is_collision(self.player2):
            self.ball.set_velocity((-self.ball.velocity[0], self.ball.velocity[1]))

    def check_collision_ball_and_border(self) -> None:
        if self.ball.rect[1][1] > 300 or self.ball.rect[0][1] < -300:
            self.ball.set_velocity((self.ball.velocity[0], -self.ball.velocity[1]))

        if self.ball.rect[1][0] > 400:
            self.score.score = (self.score.score[0], self.score.score[1] + 1)
            self.spawn_new_ball()

        if self.ball.rect[0][0] < -400:
            self.score.score = (self.score.score[0] + 1, self.score.score[1])
            self.spawn_new_ball()

    def check_collision_player_and_border(self, player: Player) -> None:
        if player.rect[1][1] > 300:
            player.set_velocity((0, -1))

        if player.rect[0][1] < -300:
            player.set_velocity((0, 1))

    def player2_move(self) -> None:
        if self.ball.center[1] > self.player2.center[1] + 10:
            self.player2.set_velocity_up()
        elif self.ball.center[1] < self.player2.center[1] - 10:
            self.player2.set_velocity_down()

    def is_collision(self, player: Player) -> bool:
        """
        Проверяет столкновение мяча с игроком.
        Столкновение происходит, если мяч находится внутри вертикальных и горизонтальных границ игрока.
        """
        ball_left, ball_right = self.ball.rect[0][0], self.ball.rect[1][0]
        ball_top, ball_bottom = self.ball.rect[1][1], self.ball.rect[0][1]

        player_left, player_right = player.rect[0][0], player.rect[1][0]
        player_top, player_bottom = player.rect[1][1], player.rect[0][1]

        # Проверка на пересечение горизонтальных и вертикальных границ
        if (ball_right > player_left and ball_left < player_right and
                ball_bottom < player_top and ball_top > player_bottom):
            return True
        return False


game = Game()
game.start_game()
game.run()
