import os.path

import pygame.image


class ChessBoard:
    def __init__(self, filename, x, y):
        self.width = 400
        self.height = 400
        self.boardImage = self.load_board_image(filename)
        # rect(top, left, width, height)
        self.boardRect = pygame.Rect(x - self.width/2, y - self.height/2, self.width, self.height)

    def load_board_image(self, filename):
        image = pygame.image.load(os.path.join('Utils\\Images\\chess', filename)).convert()
        return image

