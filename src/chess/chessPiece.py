from pygame.sprite import Sprite
from pygame import Surface
from pygame.rect import Rect
from src.chess.pieceType import PieceType
from src.chess.chessBoard import ChessBoard


class ChessPiece(Sprite):
    def __init__(self, image: Surface, rect: Rect, pos: tuple[int, int], piecetype: PieceType):
        """
        :param rect: the ChessTile_rect in which ChessPiece is placed
        :param pos: pos in form of (0, 0), (0, 1)...
        """
        super().__init__()
        self.image = image
        self.imageSize = image.get_rect().width
        self.boardRect = rect
        self.rect = Rect((self.boardRect.centerx - self.imageSize / 2, self.boardRect.centery - self.imageSize / 2),
                         (self.imageSize, self.imageSize))
        self.pos = pos
        self.posX = pos[0]
        self.posY = pos[1]
        self.pieceType = piecetype

    def move(self, posx, posy, chessboard: ChessBoard):
        self.posX = posx
        self.posY = posy
        self.rect.center = chessboard.convert_coordinates_to_board(posx, posy).center

    def draw(self, surface: Surface):
        surface.blit(self.image, (self.rect.centerx - self.rect.height / 2, self.rect.centery - self.rect.width / 2))
