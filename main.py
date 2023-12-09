import os.path

import pygame
from sys import exit

from src.chess.chess import Chess

pygame.init()
size = width, height = 1080, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

# Colors
black = pygame.Color(0, 0, 0)
grey = pygame.Color(125, 125, 125)
white = pygame.Color(255, 255, 255)

gameRunning = True

# setup chess game
chess = Chess(screen)

while gameRunning:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                print('starting a chess game...')
                chess.run()

    # fill screen so nothing left from the last frame
    screen.fill(grey)

    # render Game


    # update screen
    pygame.display.flip()

    # limit frames
    clock.tick(60)

pygame.quit()
