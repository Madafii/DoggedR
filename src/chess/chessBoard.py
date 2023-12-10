import os.path

import pygame.image
from pygame.surface import Surface
from pygame.sprite import Sprite, Group
from src.chess.pieceType import PieceType


class ChessTile(Sprite):
    def __init__(self, image: Surface, rect: pygame.rect.Rect, pos: tuple[int, int]):
        """
        :param image:
        :param rect: the actual pixel props
        :param pos: the position in form (0, 0), (1, 0)...
        """
        super().__init__()
        self.image = image
        self.rect = rect
        self._pos = pos
        self.occupied = None

    def set_piece(self, piecetype: PieceType = None):
        self.occupied = piecetype

    def get_pos(self) -> tuple[int, int]:
        return self._pos


class ChessBoard:
    def __init__(self, filename, x, y):
        super().__init__()
        self.tileImage = self.load_board_tiles(filename)
        self.tileRect = self.tileImage.get_rect()
        self.tileSize = self.tileRect.height
        self.boardNumTiles = 8
        self.boardSize = self.tileSize * self.boardNumTiles
        self.boardRect = pygame.Rect(x - self.boardSize / 2, y - self.boardSize / 2, self.boardSize, self.boardSize)
        self.boardTiles = Group()
        self.setup_board()

    def load_board_tiles(self, filename) -> Surface:
        image = pygame.image.load(os.path.join('Utils\\Images\\chess', filename)).convert()
        return image

    def setup_board(self):
        tileSize = self.tileRect.height
        for i in range(0, self.boardNumTiles):
            for j in range(0, self.boardNumTiles):
                self.boardTiles.add(ChessTile(self.tileImage.subsurface(  # type: ignore
                    pygame.rect.Rect(0 + (i + j) % 2 * tileSize, 0, tileSize, tileSize)),
                    pygame.rect.Rect(self.convert_coordinates_to_board(i, j).topleft, (tileSize, tileSize)),
                    (i, j)))

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

    def get_tile_at(self, index: tuple[int, int]) -> ChessTile:
        return list(self.boardTiles)[index[0] + index[1] * self.boardNumTiles]

    def update(self, surface: Surface):
        pass

    # no idea why need **kwargs
    def draw(self, surface: Surface, **kwargs):
        for tile in self.boardTiles:
            surface.blit(tile.image, tile.rect)
