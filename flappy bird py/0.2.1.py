import pygame
import random

# Константы
WIDTH, HEIGHT = 360, 480
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = -10
WALL_SPEED = -5
WALL_FREQUENCY = 1500  # в миллисекундах

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 24)

    def increase(self):
        self.score += 1

    def draw(self, screen):
        text = self.font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(text, (10, 10))


class Player:
    def __init__(self, position):
        self.x, self.y = position
        self.width, self.height = 30, 20
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

        # Ограничение по экрану
        if self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height
            self.velocity = 0

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def jump(self):
        self.velocity = JUMP_STRENGTH


class Wall:
    def __init__(self, x, gap_y, gap_size):
        self.x = x
        self.gap_y = gap_y
        self.gap_size = gap_size
        self.width = 50
        self.color = BLUE

    def update(self):
        self.x += WALL_SPEED

    def draw(self, screen):
        # Верхняя часть стены
        pygame.draw.rect(screen, self.color, (self.x, 0, self.width, self.gap_y))
        # Нижняя часть стены
        pygame.draw.rect(screen, self.color, (self.x, self.gap_y + self.gap_size, self.width, HEIGHT - self.gap_y - self.gap_size))

    def is_off_screen(self):
        return self.x + self.width < 0


def game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()

    # Создаем объекты
    player = Player((50, HEIGHT // 2))
    walls = []
    score = Score()

    # Таймер для появления стен
    wall_timer = pygame.time.get_ticks()

    running = True
    while running:
        clock.tick(FPS)

        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.jump()

        # Логика
        player.update()

        # Управление стенами
        if pygame.time.get_ticks() - wall_timer > WALL_FREQUENCY:
            gap_y = random.randint(100, HEIGHT - 150)
            walls.append(Wall(WIDTH, gap_y, 100))
            wall_timer = pygame.time.get_ticks()

        for wall in walls:
            wall.update()
            # Удаление стен, ушедших за экран
            if wall.is_off_screen():
                walls.remove(wall)
                score.increase()

        # Столкновение с стенами
        for wall in walls:
            if (player.x < wall.x + wall.width and player.x + player.width > wall.x and
               (player.y < wall.gap_y or player.y + player.height > wall.gap_y + wall.gap_size)):
                running = False

        # Рисование
        screen.fill(WHITE)
        player.draw(screen)
        for wall in walls:
            wall.draw(screen)
        score.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    game()
