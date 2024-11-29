from math import *
from config import *
from Planet import Planet


def gravity(object_1: Planet, object_2: Planet) -> tuple:
    x1 = object_1.position[0]
    y1 = object_1.position[1]
    m1 = object_1.mass
    x2 = object_2.position[0]
    y2 = object_2.position[1]
    m2 = object_2.mass
    # print(x1, x2, y1, y2, m1, m2)
    if x1 == x2:
        return (0, 0), (0, 0)
    else:
        l = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
        fm = G * (m1 * m2) / (l ** 2)
        k = (y1 - y2) / (x1 - x2)
        c = y1 - k * x1
        a = atan(k)
        vector_1 = -cos(a) * fm, -sin(a) * fm
        vector_2 = cos(a) * fm, sin(a) * fm
        if x1 > x2:
            return vector_1, vector_2
        else:
            return vector_2, vector_1


def transform_visual(cord: tuple, radius: int) -> tuple:
    l = cord[1] - center[1]
    cord_new = (cord[0], cord[1] * cos(alfa) + center[1])
    radius_new = 1 if radius == 1 else int(((l + center[1])/ center[1]) * radius * 0.8)
    return cord_new, radius_new
