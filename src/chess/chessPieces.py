import os
import pygame.image
from pygame.sprite import Group

from src.chess.chessPiece import ChessPiece
from src.chess.chessBoard import ChessBoard, ChessTile
from src.chess.pieceType import PieceType


def is_white_piece(piecetype: PieceType):
    if piecetype is None:
        return False
    elif piecetype.value < 6:
        return True
    else:
        return False


def is_pos_possible(possiblemoves, nextpos: ChessTile, whitepiece: bool):
    """
    checks if next position is a possible move
    :param whitepiece: is piece white or black
    :param possiblemoves: list with possible moves
    :param nextpos: the ChessTile to check
    :return: returns False or True according to more possible move possibilities
    """
    if nextpos.occupied is None and nextpos.get_pos() != (-1, -1):
        possiblemoves.append(nextpos)
        return True
    elif nextpos.occupied is not None and whitepiece is not is_white_piece(nextpos.occupied):
        possiblemoves.append(nextpos)
        return False
    elif nextpos.occupied is not None and whitepiece is is_white_piece(nextpos.occupied):
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

    def get_black_pieces_types(self):
        black_pieces = list()
        for i in range(6, 12):
            black_pieces.append(PieceType(i))
        return black_pieces

    def get_white_pieces_types(self):
        white_pieces = list()
        for i in range(0, 6):
            white_pieces.append(PieceType(i))
        return white_pieces

    def get_pieces(self) -> dict:
        pass

    def is_king_checked(self, chesspiece: ChessPiece, chessboard: ChessBoard):
        kingsInPossibleMoves = [s for s in self.get_possible_moves(chesspiece, chessboard) if
                                s.occupied == PieceType.BlackKing or s.occupied == PieceType.WhiteKing]
        if len(kingsInPossibleMoves) > 0:
            return True

    def get_possible_moves(self, chesspiece: ChessPiece, chessboard: ChessBoard) -> list[ChessTile]:
        possibleMoves: list[ChessTile] = list()
        x = chesspiece.posX
        y = chesspiece.posY
        if chesspiece.pieceType == PieceType.WhitePawn:
            if chessboard.get_tile_at((x, y + 1)).occupied is None:
                possibleMoves.append(chessboard.get_tile_at((x, y + 1)))
                if y == 1 and chessboard.get_tile_at((x, y + 2)).occupied is None:
                    possibleMoves.append(chessboard.get_tile_at((x, y + 2)))
            if chessboard.get_tile_at((x - 1, y + 1)).occupied in self.get_black_pieces_types():
                possibleMoves.append(chessboard.get_tile_at((x - 1, y + 1)))
            if chessboard.get_tile_at((x + 1, y + 1)).occupied in self.get_black_pieces_types():
                possibleMoves.append(chessboard.get_tile_at((x + 1, y + 1)))
        if chesspiece.pieceType == PieceType.BlackPawn:
            if chessboard.get_tile_at((x, y - 1)).occupied is None:
                possibleMoves.append(chessboard.get_tile_at((x, y - 1)))
                if y == 6 and chessboard.get_tile_at((x, y - 2)).occupied is None:
                    possibleMoves.append(chessboard.get_tile_at((x, y - 2)))
            if chessboard.get_tile_at((x - 1, y - 1)).occupied in self.get_white_pieces_types():
                possibleMoves.append(chessboard.get_tile_at((x - 1, y - 1)))
            if chessboard.get_tile_at((x + 1, y - 1)).occupied in self.get_white_pieces_types():
                possibleMoves.append(chessboard.get_tile_at((x + 1, y - 1)))
        if chesspiece.pieceType == PieceType.WhiteRook or chesspiece.pieceType == PieceType.BlackRook:
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                for i in range(1, 8):
                    nextPos = chessboard.get_tile_at((x + i * dx, y + i * dy))
                    if not is_pos_possible(possibleMoves, nextPos, is_white_piece(chesspiece.pieceType)):
                        break
        if chesspiece.pieceType == PieceType.WhiteKnight or chesspiece.pieceType == PieceType.BlackKnight:
            directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
            for dx, dy in directions:
                nextPos = chessboard.get_tile_at((x + dx, y + dy))
                is_pos_possible(possibleMoves, nextPos, is_white_piece(chesspiece.pieceType))
        if chesspiece.pieceType == PieceType.WhiteBishop or chesspiece.pieceType == PieceType.BlackBishop:
            directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dx, dy in directions:
                for i in range(1, 8):
                    nextPos = chessboard.get_tile_at((x + i * dx, y + i * dy))
                    if not is_pos_possible(possibleMoves, nextPos, is_white_piece(chesspiece.pieceType)):
                        break
        if chesspiece.pieceType == PieceType.WhiteQueen or chesspiece.pieceType == PieceType.BlackQueen:
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dx, dy in directions:
                for i in range(1, 8):
                    nextPos = chessboard.get_tile_at((x + i * dx, y + i * dy))
                    if not is_pos_possible(possibleMoves, nextPos, is_white_piece(chesspiece.pieceType)):
                        break
        if chesspiece.pieceType == PieceType.WhiteKing or chesspiece.pieceType == PieceType.BlackKing:
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dx, dy in directions:
                nextPos = chessboard.get_tile_at((x + dx, y + dy))
                is_pos_possible(possibleMoves, nextPos, is_white_piece(chesspiece.pieceType))
        return possibleMoves

    def filter_possible_moves_on_check(self, blackchesspieces, whitechesspieces, chessboard: ChessBoard,
                                       possiblemoves: list[ChessTile], chesspiece : ChessPiece, whitesturn: bool):
        print("king is checked")
        illegal_moves = list()
        for move in possiblemoves:
            dummyTile = chessboard.get_tile_at((move.get_pos()[0], move.get_pos()[1]))
            tmpDummyTileType = dummyTile.occupied
            dummyTile.occupied = chesspiece.pieceType
            previousTile = chessboard.get_tile_at((chesspiece.posX, chesspiece.posY))
            previousTile.occupied = None
            for piece in blackchesspieces:
                if (piece.posX, piece.posY) == dummyTile.get_pos():
                    continue
                if self.is_king_checked(piece, chessboard):
                    illegal_moves.append(move)
                    break
            for piece in whitechesspieces:
                if (piece.posX, piece.posY) == dummyTile.get_pos():
                    continue
                if self.is_king_checked(piece, chessboard):
                    illegal_moves.append(move)
                    break
            dummyTile.occupied = tmpDummyTileType
            previousTile.occupied = chesspiece.pieceType
        for move in illegal_moves:
            possiblemoves.remove(move)





