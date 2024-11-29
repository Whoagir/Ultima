from numba import jit
from typing import Tuple
import math


@jit(nopython=True)
def transform_visual(cord: Tuple[float, float], alfa: float) -> Tuple[float, float]:
    center = (15, 15, 15)
    c = math.sqrt((cord[0] - center[0]) ** 2 + (cord[1] - center[1]) ** 2)

    if cord[1] == center[1] or cord[0] == center[0]:
        if cord[1] == center[1] and cord[0] < center[0]:
            cord_new = (center[0] + math.sin(alfa) * c, cord[1])

        if cord[1] == center[1] and cord[0] > center[0]:
            cord_new = (center[0] - math.sin(alfa) * c, cord[1])

        if cord[1] < center[1] and cord[0] == center[0]:
            cord_new = (center[0] - math.sin(alfa) * c, cord[1])

        if cord[1] > center[1] and cord[0] == center[0]:
            cord_new = (center[0] + math.sin(alfa) * c, cord[1])

        if cord[1] == center[1] and cord[0] == center[0]:
            cord_new = cord

    else:
        fi = math.atan(abs(cord[0] - center[0]) / abs(cord[1] - center[1]))

        if cord[0] < center[0] and cord[1] < center[0]:  # 1
            cord_new = (center[0] - math.sin(fi + alfa) * c, cord[1])

        if cord[0] > center[0] and cord[1] < center[0]:  # 2
            cord_new = (center[0] + math.sin(fi - alfa) * c, cord[1])

        if cord[0] > center[0] and cord[1] > center[0]:  # 3
            cord_new = (center[0] + math.sin(fi + alfa) * c, cord[1])

        if cord[0] < center[0] and cord[1] > center[0]:  # 4
            cord_new = (center[0] - math.sin(fi - alfa) * c, cord[1])

    return cord_new
