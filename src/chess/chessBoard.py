import os.path

import pygame.image
from pygame.surface import Surface
from pygame.sprite import Sprite


class ChessBoard(Sprite):
    def __init__(self, filename, x, y):
        super().__init__()
        self.width = 400
        self.height = 400
        self.boardImage = self.load_board_image(filename)
        # rect(top, left, width, height)
        self.boardRect = pygame.Rect(x - self.width / 2, y - self.height / 2, self.width, self.height)

    def load_board_image(self, filename) -> Surface:
        image = pygame.image.load(os.path.join('Utils\\Images\\chess', filename)).convert()
        return image

    def convert_coordinates_to_board(self, x, y):
        bottomleft = self.boardRect.bottomleft
        x = bottomleft[0] + x * self.width / 8
        y = bottomleft[1] - (y + 1) * self.height / 8
        return x, y
