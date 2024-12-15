import turtle
import random

# Константы
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
WALL_WIDTH = 20
WALL_GAP = 150
GRAVITY = -0.4
JUMP_STRENGTH = 8
WALL_SPEED = 2

# Переменные глобального состояния
game_state = "waiting"  # Возможные значения: "waiting", "playing", "game_over"
walls = []  # Список стен
player = None  # Игрок


# Класс игрока
class Player:
    def __init__(self):
        self.x = -100  # Начальная позиция игрока
        self.y = 0  # Начальная вертикальная позиция
        self.velocity = 0  # Скорость падения игрока

    def update(self):
        self.velocity += GRAVITY  # Применение силы гравитации
        self.y += self.velocity

        # Если игрок падает ниже экрана
        if self.y < -SCREEN_HEIGHT // 2:
            self.y = -SCREEN_HEIGHT // 2
            self.velocity = 0

    def jump(self):
        self.velocity = JUMP_STRENGTH  # Прыжок вверх

    def draw(self, turtle):
        turtle.goto(self.x, self.y)
        turtle.dot(20, "yellow")  # Отображение игрока в виде жёлтого круга


# Класс стены
class Wall:
    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(-SCREEN_HEIGHT // 4, SCREEN_HEIGHT // 4)  # Случайная позиция разрыва

    def update(self):
        self.x -= WALL_SPEED  # Движение стены влево

    def draw(self, turtle):
        # Верхняя часть стены
        turtle.up()
        turtle.goto(self.x - WALL_WIDTH // 2, self.gap_y + WALL_GAP // 2)
        turtle.down()
        turtle.begin_fill()
        turtle.color("green")
        turtle.goto(self.x + WALL_WIDTH // 2, self.gap_y + WALL_GAP // 2)
        turtle.goto(self.x + WALL_WIDTH // 2, SCREEN_HEIGHT // 2)
        turtle.goto(self.x - WALL_WIDTH // 2, SCREEN_HEIGHT // 2)
        turtle.goto(self.x - WALL_WIDTH // 2, self.gap_y + WALL_GAP // 2)
        turtle.end_fill()

        # Нижняя часть стены
        turtle.up()
        turtle.goto(self.x - WALL_WIDTH // 2, self.gap_y - WALL_GAP // 2)
        turtle.down()
        turtle.begin_fill()
        turtle.color("green")
        turtle.goto(self.x + WALL_WIDTH // 2, self.gap_y - WALL_GAP // 2)
        turtle.goto(self.x + WALL_WIDTH // 2, -SCREEN_HEIGHT // 2)
        turtle.goto(self.x - WALL_WIDTH // 2, -SCREEN_HEIGHT // 2)
        turtle.goto(self.x - WALL_WIDTH // 2, self.gap_y - WALL_GAP // 2)
        turtle.end_fill()

    def collide_with(self, player):
        if abs(self.x - player.x) < WALL_WIDTH:  # Проверка горизонтальной коллизии
            if (player.y < self.gap_y - WALL_GAP // 2) or (player.y > self.gap_y + WALL_GAP // 2):
                return True  # Игрок касается стены
        return False


# Начало игры
def start_game():
    global game_state, walls, player
    game_state = "playing"  # Переводим игру в состояние "игра"
    player.y = 0  # Сбрасываем позицию игрока
    player.velocity = 0  # Сбрасываем скорость игрока
    walls.clear()  # Убираем старые стены

    # Создаём стартовые стены
    for i in range(3):
        walls.append(Wall(SCREEN_WIDTH // 2 + i * 200))
    game_loop()


# Игровой цикл
def game_loop():
    global game_state

    if game_state == "playing":
        # Обновление игровых объектов
        player.update()

        for wall in walls:
            wall.update()

        # Убираем отработанные стены и добавляем новые
        if walls and walls[0].x < -SCREEN_WIDTH // 2:
            walls.pop(0)
            walls.append(Wall(SCREEN_WIDTH // 2))

        # Проверка на коллизию
        for wall in walls:
            if wall.collide_with(player):
                game_state = "game_over"

        # Отрисовка обновленного состояния
        drawing.clear()
        player.draw(drawing)
        for wall in walls:
            wall.draw(drawing)
        screen.update()
        screen.ontimer(game_loop, 20)  # Перезапуск игрового цикла через 20 мс

    elif game_state == "game_over":
        drawing.goto(0, 0)
        drawing.color("white")
        drawing.write("Game Over\nНажмите ПРОБЕЛ, чтобы начать заново", align="center", font=("Arial", 24, "normal"))
        screen.update()

# Инициализация
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Flappy Bird")
drawing = turtle.Turtle()
drawing.hideturtle()
drawing.speed(0)
drawing.up()

# Создаём игрока
player = Player()

# Привязка клавиатуры
screen.listen()
screen.onkey(lambda: start_game() if game_state in ["waiting", "game_over"] else player.jump(), "space")

# Экран ожидания начала игры
drawing.goto(0, 0)
drawing.color("white")
drawing.write("Нажмите ПРОБЕЛ, чтобы начать", align="center", font=("Arial", 24, "normal"))

# Запускаем приложение
screen.mainloop()
