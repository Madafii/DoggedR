from pygame.sprite import Sprite
from pygame import Surface
from pygame.rect import Rect
from src.chess.pieceType import PieceType


class ChessPiece(Sprite):
    def __init__(self, image: Surface, rect: Rect, pos: tuple[int, int], piecetype: PieceType):
        """
        :param rect: the actual pixel props
        :param pos: pos in form of (0, 0), (0, 1)...
        """
        super().__init__()
        self.image = image
        self.rect = rect
        self.pos = pos
        self.posX = pos[0]
        self.posY = pos[1]
        self.pieceType = piecetype

    def draw(self, surface: Surface):
        surface.blit(self.image, self.rect.topleft)
