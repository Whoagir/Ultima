from pygame import draw
class Polygon(object):
    def __init__(self, screen, position, color, index=0):
        self.index = index
        self.position = position
        self.screen = screen
        self.color = color

    def draw(self, alfa_chanel=256):  # alfa 0..256
        draw.polygon(self.screen, self.color, self.position)
