from utils import C
import pygame
import time


pygame.init()

WIDTH = 1800
HEIGHT = 900
FPS = 100
G = 6.67430 / (10 ** (11))
k = 1_000_000  # метров в пикселе на начало игры
DT = 0.3

DEFAULT_BORDER_COLOR = C('4875a9')
DEFAULT_BORDER_RADIUS_1 = 2
DEFAULT_BORDER_RADIUS_2 = 4
DEFAULT_BACKGROUND_COLOR = C('52a9db')

BUTTON_CLICK_TIME = 0.3
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 70
BUTTON_FONT = pygame.font.SysFont('Arial', 23)
BUTTON_COLOR = C('4efcf9')
BUTTON_BORDER_COLOR = C('48e5df')
BUTTON_TEXT_COLOR = C('000000')
BUTTON_COLOR_HOVER = C('48e5df')
BUTTON_COLOR_CLICKED = C('448db6')
BUTTON_BACKGROUND_COLOR = C('4efcf9')

w_x = -600_000_000  # координаты угла игрового окна
w_y = -450_000_000  # на общей карте

vrem_k = 1  # коэффициент ускорения времени на начало игры

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гравитация")
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 36)
text_FPS = font.render('FPS: ' + str(FPS), True, 'green')
text_vrem_k = font.render('Время: x' + str(vrem_k), True, 'green')

current_object = None


class Button:

    def __init__(self, callback, pos=(0, 0), size=(0, 0), text='Button'):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.text = text
        self.hover = False
        self.clicked = False
        self.callback = callback
        self.timer = BUTTON_CLICK_TIME

    def render(self, surface):
        txt_color = BUTTON_TEXT_COLOR
        btn_color = BUTTON_BACKGROUND_COLOR
        if self.hover:
            txt_color = BUTTON_TEXT_COLOR
            btn_color = BUTTON_COLOR_HOVER
        if self.clicked:
            txt_color = BUTTON_COLOR
            btn_color = BUTTON_COLOR_CLICKED
        pygame.draw.rect(surface, btn_color, self.rect, border_radius=DEFAULT_BORDER_RADIUS_1)
        pygame.draw.rect(surface, DEFAULT_BORDER_COLOR, self.rect, DEFAULT_BORDER_RADIUS_2,
                         border_radius=DEFAULT_BORDER_RADIUS_1)
        txt_surface = BUTTON_FONT.render(self.text, True, txt_color)
        surface.blit(txt_surface, (self.rect.x + 20, self.rect.y + 20))

    def event_handler(self, e):
        self.hover = self.rect.collidepoint(pygame.mouse.get_pos())
        if e.type == pygame.MOUSEBUTTONUP and self.hover:
            self.click()

    def update(self):
        self.timer -= 0.01
        if self.timer <= 0:
            self.clicked = False

    def click(self):
        self.clicked = True
        self.callback(self.text)
        self.timer = BUTTON_CLICK_TIME


class Ball():
    def __init__(self, real_x, real_y, real_r, m, colour):
        self.real_x = real_x
        self.real_y = real_y
        self.real_r = real_r
        self.m = m
        self.colour = colour
        self.speed = [0, 0]
        self.a = [0, 0]
        self.f = [0, 0]
        self.trace_count = 0
        self.trace = []
        self.status = True  # шар ещё существует

    def update(self):
        self.a[0] = (self.f[0] / self.m) * (vrem_k ** 2) / FPS ** 2
        self.a[1] = (self.f[1] / self.m) * (vrem_k ** 2) / FPS ** 2

        self.speed[0] += self.a[0]
        self.speed[1] += self.a[1]

        self.real_x += self.speed[0]
        self.real_y += self.speed[1]

        # траектория:
        self.trace_count += (self.speed[0] ** 2 + self.speed[1] ** 2) ** 0.5
        if self.trace_count / k >= 5:
            self.trace_count = 0
            self.trace.append((self.real_x,
                               self.real_y))
        if len(self.trace) > 1000:
            self.trace.pop(0)

    def draw(self):
        pygame.draw.circle(screen,
                           self.colour,
                           ((self.real_x - w_x) / k,
                            (self.real_y - w_y) / k),
                           self.real_r / k
                           )
        for i in self.trace:
            pygame.draw.circle(screen,
                               self.colour,
                               ((i[0] - w_x) / k,
                                (i[1] - w_y) / k),
                               1)


class Collision():
    def __init__(self):
        ...

    def collision_two_solid_ball(self):
        ...

    def collision_solid_solar_ball(self):
        t1 = balls[i[0]]
        t2 = balls[i[1]]
        if t1.status and t2.status:
            t1.status = False
            t2.status = False
            if t1.real_r > t2.real_r:
                c = t1.colour
            else:
                c = t2.colour

            t = Ball((t1.real_x * t1.m + t2.real_x * t2.m) / (t1.m + t2.m),
                     (t1.real_y * t1.m + t2.real_y * t2.m) / (t1.m + t2.m),
                     (t1.real_r ** 3 + t2.real_r ** 3) ** (1 / 3),
                     t1.m + t2.m,
                     c)
            t.speed[0] = (t1.m * t1.speed[0] + t2.m * t2.speed[0]) / (t1.m + t2.m)
            t.speed[1] = (t1.m * t1.speed[1] + t2.m * t2.speed[1]) / (t1.m + t2.m)
            balls.append(t)


balls = []


p = Ball(0, 0, 6371000, 5.9722 * 10 ** 24, 'blue')
balls.append(p)


p = Ball(-363104000, 0, 1737100, 7.35 * 10 ** 22, 'grey')
balls.append(p)
p.speed[1] = 1080 * vrem_k / FPS


'''p = Ball(0,6_371_000+415_000,45,440_075,'yellow')
balls.append(p)
p.speed[0] = 7700*vrem_k/FPS'''


p = Ball(149.6 * 10 ** 9, 0, 696_000_000, 1.9891 * 10 ** 30, 'red')
balls.append(p)
balls[0].speed[1] += 29782.77 * vrem_k / FPS
balls[1].speed[1] += 29782.77 * vrem_k / FPS

menu_object_list = {
    "Jupiter": {"radius": 71_492_000, "mass": 1.8986 * 10 ** 27, "color": "orange"},
    "Sun": {"radius": 696_000_000, "mass": 1.9891 * 10 ** 30, "color": "red"},
    "BlackHole": {"radius": 10_000_000, "mass": 1.9891 * 10 ** 30 * 4000_000, "color": "pink"},
    "Earth": {"radius": 6_371_000, "mass": 5.9722 * 10 ** 24, "color": "blue"}
}


class ButtonMenu:
    def __init__(self):
        self.items = []
        self.jump_x = 0
        self.jump_y = 0
        self.current_key = list(menu_object_list.keys())[0]
        for c, key in enumerate(menu_object_list):
            self.items.append(Button(self.set_current, pos=(200, 200 + c * 45), size=(100, 40), text=key))

    def update(self):
        for item in self.items:
            item.update()



    def render(self, surface):
        for item in self.items:
            item.render(surface)

    def set_coord(self, x, y):
        self.jump_x = x
        self.jump_y = y

    def set_current(self, key):
        self.current_key = key

    def add_ball(self):
        balls.append(Ball(self.jump_x,
                          self.jump_y,
                          menu_object_list[self.current_key]["radius"],
                          menu_object_list[self.current_key]["mass"],
                          menu_object_list[self.current_key]["color"]
                          ))

    def event_handler(self, e):
        for item in self.items:
            item.event_handler(e)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                self.add_ball()


menu = ButtonMenu()

tick = 0
tm = time.time()
running = True

while running:
    clock.tick(FPS)
    tick += 1
    if tick == 100:
        tick = 0
        text_FPS = font.render('FPS: ' + str(int((100 / (time.time() - tm)))), True,
                               'green')

        tm = time.time()

    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Найдём место на реальной карте,
            # куда хочет попасть игрок:
            xx = event.pos[0]
            yy = event.pos[1]
            jump_x = w_x + xx * k
            jump_y = w_y + yy * k

            menu.set_coord(jump_x, jump_y)

            if event.button == 4:
                k = k * 0.85

                w_x = jump_x - xx * k
                w_y = jump_y - yy * k

            if event.button == 5:
                k = k / 0.85

                w_x = jump_x - xx * k
                w_y = jump_y - yy * k

            if event.button == 2:
                if vrem_k == 100_0000:
                    vrem_k = 1
                    for i in balls:
                        i.speed[0] /= 100_0000
                        i.speed[1] /= 100_0000
                else:
                    vrem_k *= 10
                    for i in balls:
                        i.speed[0] *= 10
                        i.speed[1] *= 10

                text_vrem_k = font.render('Время: x' + str(vrem_k), True, 'green')
        menu.event_handler(event)
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0] == True:
                w_x -= event.rel[0] * k
                w_y -= event.rel[1] * k

    collisions = []
    # считаем действующие силы на каждое тело
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            dx = balls[j].real_x - balls[i].real_x
            dy = balls[j].real_y - balls[i].real_y
            d = (dx ** 2 + dy ** 2) ** 0.5
            if d == 0:
                continue
            ff = G * balls[i].m * balls[j].m / d ** 2

            balls[i].f[0] += dx * ff / d
            balls[i].f[1] += dy * ff / d

            balls[j].f[0] -= dx * ff / d
            balls[j].f[1] -= dy * ff / d

            if balls[i].real_r > d - balls[j].real_r:
                collisions.append((i, j))

    # обработаем столкновения:
    for i in collisions:
        t1 = balls[i[0]]
        t2 = balls[i[1]]
        if t1.status and t2.status:
            t1.status = False
            t2.status = False
            if t1.real_r > t2.real_r:
                c = t1.colour
            else:
                c = t2.colour

            t = Ball((t1.real_x * t1.m + t2.real_x * t2.m) / (t1.m + t2.m),
                     (t1.real_y * t1.m + t2.real_y * t2.m) / (t1.m + t2.m),
                     (t1.real_r ** 3 + t2.real_r ** 3) ** (1 / 3),
                     t1.m + t2.m,
                     c)
            t.speed[0] = (t1.m * t1.speed[0] + t2.m * t2.speed[0]) / (t1.m + t2.m)
            t.speed[1] = (t1.m * t1.speed[1] + t2.m * t2.speed[1]) / (t1.m + t2.m)
            balls.append(t)

    tt = []
    for ball in balls:
        if ball.status:
            tt.append(ball)
    balls = tt

    for ball in balls:
        ball.update()
        ball.f = [0, 0]

    menu.update()

    # рисуем
    screen.fill('black')

    for ball in balls:
        ball.draw()

    menu.render(screen)

    screen.blit(text_FPS, (10, 10))
    screen.blit(text_vrem_k, (10, 50))
    pygame.display.update()
pygame.quit()
