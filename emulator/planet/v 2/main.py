import pygame

from Logic import gravity, transform_visual
from config import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

stop = False
running = True
while running:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                stop = 1 - stop
    if stop:
        screen.fill((0, 0, 0))
        for planet in planets:
            vector_gravity_planet, v = gravity(planet, solar)
            planet.update(vector_gravity_planet)
            visual_position, visual_radius = transform_visual(planet.position, planet.radius)
            pygame.draw.circle(screen, planet.color, visual_position, visual_radius)
            planet.trace()
            for trace in planet.traces:
                visual_position, visual_radius = transform_visual(trace, 1)
                pygame.draw.circle(screen, planet.color, visual_position, visual_radius)

    visual_position, visual_radius = transform_visual(solar.position, 1)
    pygame.draw.circle(screen, solar.color, visual_position, solar.radius)
    pygame.display.update()

pygame.quit()
