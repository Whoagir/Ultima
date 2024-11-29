import pygame
from constant import *


class Game(object):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.FPS = 60

    def setup(self):
        pass

    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                self.event_handler(event)
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption(str(self.clock.get_fps()))

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            self.stop()

    def stop(self):
        self.running = False


if __name__ == '__main__':
    game = Game()
    game.run()
