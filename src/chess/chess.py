import pygame
from pygame.sprite import Sprite

from src.chess.chessPieces import ChessPieces
from src.chess.chessBoard import ChessBoard


class Chess(Sprite):
    def __init__(self, surface: pygame.Surface):
        super().__init__()
        self.board = ChessBoard('ChessBoard400x400.png', surface.get_width() / 2, surface.get_height() / 2)
        self.pieces = ChessPieces('chessPieces.png')
        self.surface = surface

    def setup_pieces(self, pieces):
        pass

    def update(self):
        self.surface.blit(self.board.boardImage, self.board.boardRect)

    def run(self):
        pass
