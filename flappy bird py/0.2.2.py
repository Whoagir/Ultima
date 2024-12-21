import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH = 400
HEIGHT = 600
FPS = 60
WALL_SPEED = -5
WALL_FREQUENCY = 1500  # Частота появления труб в миллисекундах
GRAVITY = 0.5
JUMP_STRENGTH = -10
SHOW_DEBUG = False  # Отображение ректов: True - показывать, False - скрывать

# Загрузка изображений
background_img = pygame.image.load("res/background.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))  # Масштабируем фон
bird_img = pygame.image.load("res/bird.png")
pipe_img = pygame.image.load("res/pipe.png")

# Инициализация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird со спрайтами")
clock = pygame.time.Clock()


# Игрок (птица)
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(bird_img, (50, 50))  # Масштабируем птицу

        # Размер rектангла меньше по сравнению со спрайтом
        self.original_rect = self.image.get_rect()  # Получаем полный rект спрайта
        self.rect = pygame.Rect(10, 10, 50, 40)  # Новый размер rect (уменьшаем до 400 на 400 относительно спрайта)
        self.rect.center = self.original_rect.center  # Сохраняем центр

        self.rect.center = (WIDTH // 4, HEIGHT // 2)
        self.speed_y = 0

    def jump(self):
        self.speed_y = JUMP_STRENGTH

    def update(self):
        self.speed_y += GRAVITY
        self.rect.y += self.speed_y

        # Не даём птице вылететь за границы экрана
        if self.rect.top <= 0:
            self.rect.top = 0
            self.speed_y = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def draw_debug(self, screen):
        if SHOW_DEBUG:
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)  # Красный прямоугольник для отладки


# Трубы
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, is_top):
        super().__init__()
        self.image = pygame.transform.scale(pipe_img, (80, 400))  # Масштабируем трубы
        if is_top:
            # Переворачиваем верхнюю трубу
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(bottomleft=(x, y))
        else:
            self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = WALL_SPEED
        self.counted = False  # Флаг для подсчёта очков

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()  # Удаляем трубу после её выхода за пределы экрана

    def draw_debug(self, screen):
        if SHOW_DEBUG:
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)  # Зелёный прямоугольник для отладки


# Счетчик
class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 36)

    def increase(self):
        self.value += 1

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.value // 2}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))


# Основной цикл игры
def game():
    global SHOW_DEBUG  # Чтобы переключать режим отладки

    all_sprites = pygame.sprite.Group()
    pipe_sprites = pygame.sprite.Group()

    bird = Bird()
    all_sprites.add(bird)

    score = Score()
    pipe_timer = pygame.time.get_ticks()  # Таймер для генерации труб

    running = True
    while running:
        clock.tick(FPS)

        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
                if event.key == pygame.K_d:  # Нажатие "D" — переключение отладки
                    SHOW_DEBUG = not SHOW_DEBUG

        # Логика
        all_sprites.update()

        # Генерация труб
        if pygame.time.get_ticks() - pipe_timer > WALL_FREQUENCY:
            gap_y = random.randint(150, HEIGHT - 200)
            gap_size = 150
            top_pipe = Pipe(WIDTH, gap_y, is_top=True)
            bottom_pipe = Pipe(WIDTH, gap_y + gap_size, is_top=False)

            pipe_sprites.add(top_pipe, bottom_pipe)
            all_sprites.add(top_pipe, bottom_pipe)
            pipe_timer = pygame.time.get_ticks()

        # Проверка столкновений
        if pygame.sprite.spritecollide(bird, pipe_sprites, False):
            running = False  # Останавливаем игру при столкновении

        # Проверка прохождения трубы для увеличения счёта (только для нижней трубы)
        for pipe in pipe_sprites:
            if not pipe.counted and pipe.rect.right < bird.rect.left:
                pipe.counted = True
                score.increase()

        # Отрисовка
        screen.blit(background_img, (0, 0))  # Отрисовка фона
        all_sprites.draw(screen)
        score.draw(screen)

        # Отладочная отрисовка
        bird.draw_debug(screen)  # Красный прямоугольник вокруг птицы
        for pipe in pipe_sprites:
            pipe.draw_debug(screen)  # Зелёные прямоугольники вокруг труб

        pygame.display.flip()

    pygame.quit()


# Запуск игры
game()
