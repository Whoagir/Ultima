import pygame
import math

from random import random
from config import *
from star import Star, generate

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
star_l = list()

for i in range(MAX_STAR):
    star_l.append(generate())

stop = False
running = True
DS = 0
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                stop = 1 - stop
            if event.button == 2:
                DS += 0.5
            if event.button == 3:
                DS -= 0.5

    if not stop:
        screen.fill(BLACK)
        for star in star_l:
            pygame.draw.circle(screen, WHITE, star.position[:2], star.position[2])
            star.update_position(SPEED + DS)
            if star.position[0] < 0 or star.position[0] > WIDTH \
                    or star.position[1] < 0 or star.position[1] > HEIGHT:
                star_l.pop(star_l.index(star))
                star_l.append(generate())

        pygame.display.update()

pygame.quit()
