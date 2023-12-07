import os
import pygame.image
from src.chess.chessPiece import ChessPiece
from enum import Enum


class ChessPieces:
    def __init__(self, filename):
        self.pieceHeight = 50
        self.pieceWidth = 50
        self.colorkeyDefault = (255, 174, 201)  # colorkey is pink
        self.chessPiecesImage = self.load_pieces_image(os.path.join('Utils\\Images\\chess', filename))
        self.chessPieces = self.load_pieces()

    def load_pieces_image(self, filename):
        image = pygame.image.load(filename).convert_alpha()
        image.set_colorkey(self.colorkeyDefault)
        return image

    def load_pieces(self):
        pieces = dict()
        counter = 0
        for i in range(0, 1):
            for j in range(0, 5):
                pieces[counter] = ChessPiece(self.chessPiecesImage.subsurface(pygame.Rect(j * 50, i * 50, 50, 50)))
                counter += 1
        return pieces

    def get_black_pieces(self):
        pass

    def get_white_pieces(self):
        pass

    def get_pieces(self) -> dict:
        pass


class Piece(Enum):
    WhitePawn = 0
    WhiteKnight = 1
    WhiteBishop = 2
    WhiteRook = 3
    WhiteKing = 4
    WhiteQueen = 5
    BlackPawn = 6
    BlackKnight = 7
    BlackBishop = 8
    BlackRook = 9
    BlackKing = 10
    BlackQueen = 11
