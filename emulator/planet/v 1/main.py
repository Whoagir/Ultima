from __future__ import annotations

import sys
import pygame as pg
import pygame_gui as pgi

from Planet import Planet
from constants import *

planet_list = {
    "Jupiter": {"radius": 71_492_000, "mass": 1.8986 * 10 ** 27, "color": "orange"},
    "Sun": {"radius": 696_000_000, "mass": 1.9891 * 10 ** 30, "color": "red"},
    "BlackHole": {"radius": 10_000_000, "mass": 1.9891 * 10 ** 30 * 4000_000, "color": "pink"},
    "Earth": {"radius": 6_371_000, "mass": 5.9722 * 10 ** 24, "color": "blue"}
}


class Main(object):
    def __init__(self, width=DEFAULT_WINDOW_WIDTH, height=DEFAULT_WINDOW_HEIGHT):
        pg.init()
        self.fps: int = FPS
        self.objects: list[Planet] = []

        self.simulate_speed: int = SIMULATE_SPEED_LIMIT_LOWER
        self.zoom: int = DEFAULT_ZOOM
        self.area_x = DEFAULT_AREA_X
        self.area_y = DEFAULT_AREA_Y

        self.running: bool = True

        self.width: int = width
        self.height: int = height
        self.screen: pg.Surface = pg.display.set_mode((self.width, self.height))
        self.clock: pg.time.Clock = pg.time.Clock()

    def event_handler(self, e):
        if e.type == pg.QUIT:
            self.exit()

        if e.type == pg.MOUSEBUTTONDOWN:
            xx = e.pos[0]
            yy = e.pos[1]
            pos_x = self.area_x + xx * self.zoom
            pos_y = self.area_y + yy * self.zoom

            if e.button == 4:
                self.zoom = self.zoom * 0.85

                self.area_x = pos_x - xx * self.zoom
                self.area_y = pos_y - yy * self.zoom

            if e.button == 5:
                self.zoom = self.zoom / 0.85

                self.area_x = pos_x - xx * self.zoom
                self.area_y = pos_y - yy * self.zoom

            if e.button == 2:
                if self.simulate_speed == 100_0000:
                    self.simulate_speed = 1
                    for i in self.objects:
                        i.speed[0] /= 100_0000
                        i.speed[1] /= 100_0000
                else:
                    self.simulate_speed *= 10
                    for i in self.objects:
                        i.speed[0] *= 10
                        i.speed[1] *= 10

            if e.button == 3:
                self.add_object(pos_x, pos_y)

        if e.type == pg.MOUSEMOTION:
            if pg.mouse.get_pressed()[0]:
                self.area_x -= e.rel[0] * self.zoom
                self.area_y -= e.rel[1] * self.zoom

        for o in self.objects:
            o.event_handler(e)

    def add_object(self, x, y):
        self.objects.append(Planet(x,
                                   y,
                                   planet_list["Earth"]["radius"],
                                   planet_list["Earth"]["mass"],
                                   planet_list["Earth"]["color"]))

    def update(self, dt):
        for o in self.objects:
            o.update(dt, self.simulate_speed)

        collisions = []

        for i in range(len(self.objects)):
            for j in range(i + 1, len(self.objects)):
                dx = self.objects[j].real_x - self.objects[i].real_x
                dy = self.objects[j].real_y - self.objects[i].real_y
                d = (dx ** 2 + dy ** 2) ** 0.5
                if d == 0:
                    continue
                ff = G * self.objects[i].m * self.objects[j].m / d ** 2

                self.objects[i].f[0] += dx * ff / d
                self.objects[i].f[1] += dy * ff / d

                self.objects[j].f[0] -= dx * ff / d
                self.objects[j].f[1] -= dy * ff / d

                if self.objects[i].real_r > d - self.objects[j].real_r:
                    collisions.append((i, j))

        for i in collisions:
            t1 = self.objects[i[0]]
            t2 = self.objects[i[1]]
            if t1.status and t2.status:
                t1.status = False
                t2.status = False
                if t1.real_r > t2.real_r:
                    c = t1.colour
                else:
                    c = t2.colour

                t = Planet((t1.real_x * t1.m + t2.real_x * t2.m) / (t1.m + t2.m),
                           (t1.real_y * t1.m + t2.real_y * t2.m) / (t1.m + t2.m),
                           (t1.real_r ** 3 + t2.real_r ** 3) ** (1 / 3),
                           t1.m + t2.m,
                           c)
                t.speed[0] = (t1.m * t1.speed[0] + t2.m * t2.speed[0]) / (t1.m + t2.m)
                t.speed[1] = (t1.m * t1.speed[1] + t2.m * t2.speed[1]) / (t1.m + t2.m)
                self.objects.append(t)

        self.objects = list(filter(lambda p: p.status, self.objects))

    def render(self):
        self.screen.fill(BACKGROUND_COLOR)

        for o in self.objects:
            o.render(self.screen, self.zoom, (self.area_x, self.area_y))

        pg.display.flip()

    def exit(self):
        self.running = False
        pg.quit()
        sys.exit()

    def start(self):
        self.main_loop()

    def main_loop(self):
        while self.running:
            for event in pg.event.get():
                self.event_handler(event)

            self.update(self.clock.tick(self.fps))

            self.render()


if __name__ == "__main__":
    w = Main(800, 600)
    w.start()
