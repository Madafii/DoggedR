import os
import pygame.image
from pygame.sprite import Group

from src.chess.chessPiece import ChessPiece
from src.chess.chessBoard import ChessBoard, ChessTile
from src.chess.pieceType import PieceType


def is_white_piece(piecetype: PieceType):
    if piecetype.value < 6:
        return True
    else:
        return False


class ChessPieces(Group):
    colorkeyDefault = (255, 174, 201)  # colorkey is pink

    def __init__(self, filename):
        super().__init__()
        self.pieceSize = 50
        self.chessPiecesImage = self.load_pieces_image(os.path.join('Utils\\Images\\chess', filename))
        self.chessPieces = self.load_pieces()

    def load_pieces_image(self, filename, colorkey=colorkeyDefault):
        image = pygame.image.load(filename).convert_alpha()
        image.set_colorkey(colorkey)
        return image

    def load_pieces(self):
        pieces = dict()
        counter = 0
        for i in range(0, 2):
            for j in range(0, 6):
                pieces[PieceType(counter)] = ChessPiece(
                    self.chessPiecesImage.subsurface(pygame.rect.Rect(j * 50, i * 50, 50, 50)),
                    pygame.rect.Rect(0, 0, 50, 50),
                    (0, 0),
                    PieceType(counter)
                )
                counter += 1
        return pieces

    def get_black_pieces(self):
        black_pieces = list()
        for i in range(6, 12):
            black_pieces.append(self.chessPieces[(PieceType(i))])
        return black_pieces

    def get_white_pieces(self):
        white_pieces = list()
        for i in range(0, 6):
            white_pieces.append(self.chessPieces[(PieceType(i))])
        return white_pieces

    def get_pieces(self) -> dict:
        pass

    @staticmethod
    def get_possible_moves(chesspiece: ChessPiece, chessboard: ChessBoard) -> list[ChessTile]:
        possibleMoves: list[ChessTile] = list()
        x = chesspiece.posX
        y = chesspiece.posY
        if chesspiece.pieceType == PieceType.WhitePawn:
            if chessboard.get_tile_at((x, y + 1)).occupied is None:
                possibleMoves.append(chessboard.get_tile_at((x, y + 1)))
            if y == 1:
                if chessboard.get_tile_at((x, y + 2)).occupied is None:
                    possibleMoves.append(chessboard.get_tile_at((x, y + 2)))
        if chesspiece.pieceType == PieceType.BlackPawn:
            if chessboard.get_tile_at((x, y - 1)).occupied is None:
                possibleMoves.append(chessboard.get_tile_at((x, y - 1)))
            if y == 6:
                if chessboard.get_tile_at((x, y - 2)).occupied is None:
                    possibleMoves.append(chessboard.get_tile_at((x, y - 2)))
        return possibleMoves
