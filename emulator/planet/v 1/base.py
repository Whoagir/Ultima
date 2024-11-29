import pygame as pg


class Base(object):
    def __int__(self):
        pass

    def update(self, dt: float, simulate_speed: int):
        pass

    def render(self, surface: pg.Surface, zoom: int, offset: tuple[int, int]):
        pass

    def event_handler(self, e: pg.event.Event):
        pass
