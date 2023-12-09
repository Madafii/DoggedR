import os.path

import pygame.image
from pygame.surface import Surface
from pygame.sprite import Sprite, Group


class ChessBoard(Sprite):
    def __init__(self, filename, x, y):
        super().__init__()
        self.tileImage = self.load_board_tiles(filename)
        self.tileRect = self.tileImage.get_rect()
        self.tileSize = self.tileRect.height
        self.boardSize = self.tileSize * 8
        self.boardRect = pygame.Rect(x - self.boardSize / 2, y - self.boardSize / 2, self.boardSize, self.boardSize)
        self.board = Group()
        self.setup_board()

    def load_board_tiles(self, filename) -> Surface:
        image = pygame.image.load(os.path.join('Utils\\Images\\chess', filename)).convert()
        return image

    def setup_board(self):
        tileSize = self.tileRect.height
        for i in range(0, 8):
            for j in range(0, 8):
                self.board.add(ChessTile(self.tileImage.subsurface(  # type: ignore
                    pygame.rect.Rect(0 + (i + j) % 2 * tileSize, 0, tileSize, tileSize)),
                    pygame.rect.Rect(i, j, tileSize, tileSize)))

    def convert_coordinates_to_board(self, x, y) -> pygame.rect.Rect:
        """
        convert coordinates in the form of (0, 0), (1, 0) on a chessboard to the real coordinates to the top left of
        the corresponding tile. :param x: :param y: :return:
        """
        bottomleft = self.boardRect.bottomleft
        x = bottomleft[0] + x * self.tileSize
        y = bottomleft[1] - (y + 1) * self.tileSize
        rect = pygame.rect.Rect(x, y, self.tileSize, self.tileSize)
        return rect

    def update(self, surface: Surface):
        pass

    def draw(self, surface: Surface):
        for tile in self.board:
            surface.blit(tile.image, self.convert_coordinates_to_board(tile.rect.x, tile.rect.y))


class ChessTile(Sprite):
    def __init__(self, image: Surface, rect):
        super().__init__()
        self.image = image
        self.rect = rect
