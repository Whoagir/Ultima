from Planet import Planet
from math import pi

WIDTH = 700
HEIGHT = 500
FPS = 60

G = 3  # gravity const

COLOR = [(255, 165, 0), (128, 128, 0),
         (255, 218, 185), (127, 255, 212),
         (139, 0, 0), (255, 127, 80), (240, 230, 140),
         (65, 105, 225), (47, 79, 79), (119, 136, 153)]
solar_center_x, solar_center_y = 350, 200
solar = Planet((solar_center_x, solar_center_y), (0, 0), 81, 12, COLOR[0])

mercury = Planet((solar_center_x, solar_center_y - 50), (1.9, 0), 1, 4, COLOR[1], 46)
venus = Planet((solar_center_x, solar_center_y - 70), (-1.45, 0), 0.8, 5, COLOR[2], 80)
earth = Planet((solar_center_x, solar_center_y - 90), (1.5, 0), 1, 5, COLOR[3], 110)
mars = Planet((solar_center_x, solar_center_y - 110), (1.74, 0), 1.5, 5, COLOR[4], 140)
jupiter = Planet((solar_center_x, solar_center_y - 130), (2.6, 0), 4, 7, COLOR[5], 110)
saturn = Planet((solar_center_x, solar_center_y - 150), (3, 0), 6, 7, COLOR[6], 120)
uranus = Planet((solar_center_x, solar_center_y - 180), (-2.2, 0), 4, 6, COLOR[7], 190)
neptune = Planet((solar_center_x, solar_center_y - 200), (1.3, 0), 1.5, 5, COLOR[8], 340)
pluto = Planet((solar_center_x, solar_center_y - 260), (2, 0), 4, 4, COLOR[9], 400)

planets = mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto

center = (solar_center_x, solar_center_y)
alfa = pi/2.5
