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
white = pygame.Color(255, 255, 255)

gameRunning = True

# poly = pygame.draw.polygon(screen, white, [(50, 50), (100, 100), (40, 40)])

chessPieces = pygame.image.load(os.path.join('Utils\\Images\\chess', 'chessPieces.png'))
chessPiecesC = chessPieces.convert_alpha()
chessPiecesC.set_colorkey([255, 174, 201])
chess = Chess(screen)

while gameRunning:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # fill screen so nothing left from the last frame
    screen.fill(black)

    # render Game
    chess.update()
    # screen.blit(chessPiecesC, [0, 0], [(0, 0), (50, 50)])
    # update screen
    pygame.display.flip()

    # limit frames
    clock.tick(60)

pygame.quit()
