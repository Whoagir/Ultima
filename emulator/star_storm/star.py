from config import *
import math
from random import random


def generate():
    x = random() * WIDTH
    y = random() * HEIGHT
    center = WIDTH / 2, HEIGHT / 2
    if x != center[0]:
        k = (y - center[1]) / (x - center[0])
        c = center[1] - k * center[0]
        l = ((y - center[1]) ** 2 + (x - center[0]) ** 2) ** (1 / 2)
        a = math.atan(k)
        vector = (V_N * math.cos(a), V_N * math.sin(a), 0.02) if x >= WIDTH / 2 else (
            -V_N * math.cos(a), -V_N * math.sin(a), 0.015)
        return Star(x, y, random() * DEPTH, vector)
    else:
        return None


class Star(object):
    def __init__(self, x: float, y: float, z: float, speed_vector: tuple):
        self.position = (x, y, z)  # z - size
        self.speed_vector = speed_vector

    def update_position(self, speed):
        self.position = self.position[0] + self.speed_vector[0] * speed, \
                        self.position[1] + self.speed_vector[1] * speed, \
                        self.position[2] + self.speed_vector[2] * speed

    def track_calculate(self):
        pass
