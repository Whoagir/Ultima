import pygame as pg

from base import Base
from constants import G


class Planet(Base):
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

    def update(self, dt, simulate_speed):
        self.a[0] = (self.f[0] / self.m) * (simulate_speed ** 2) * dt ** 2
        self.a[1] = (self.f[1] / self.m) * (simulate_speed ** 2) * dt ** 2

        self.speed[0] += self.a[0]
        self.speed[1] += self.a[1]

        self.real_x += self.speed[0]
        self.real_y += self.speed[1]

        # траектория:
        self.trace_count += (self.speed[0] ** 2 + self.speed[1] ** 2) ** 0.5
        if self.trace_count / 1_000_000 >= 5:
            self.trace_count = 0
            self.trace.append((self.real_x,
                               self.real_y))
        if len(self.trace) > 1000:
            self.trace.pop(0)

        self.f = [0, 0]

    def render(self, surface, zoom, offset):
        pg.draw.circle(surface,
                           self.colour,
                           ((self.real_x - offset[0]) / zoom,
                            (self.real_y - offset[1]) / zoom),
                           self.real_r / zoom
                           )
        for i in self.trace:
            pg.draw.circle(surface,
                               self.colour,
                               ((i[0] - offset[0]) / zoom,
                                (i[1] - offset[1]) / zoom),
                               1)
