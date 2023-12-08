import pygame
from pygame.sprite import Sprite, Group

from src.chess.chessPieces import ChessPieces, PieceType
from src.chess.chessPiece import ChessPiece
from src.chess.chessBoard import ChessBoard


class Chess(Sprite):
    def __init__(self, surface: pygame.Surface):
        super().__init__()
        self.board = ChessBoard('ChessBoard400x400.png', surface.get_width() / 2, surface.get_height() / 2)
        # the used pieces set
        self.pieces = ChessPieces('chessPieces.png')
        self.surface = surface
        self.running = False
        # all the pieces for one game
        self.white_pieces = Group()
        self.black_pieces = Group()
        self.setup_default_chess_game(self.pieces)

    def setup_default_chess_game(self, pieces: ChessPieces):
        # set coordinates (0, 0) = bottom, left (7, 7) = top, right
        self.white_pieces.add(ChessPiece(pieces.chessPieces[PieceType.WhiteRook].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(0, 0)),
                              ChessPiece(pieces.chessPieces[PieceType.WhiteKnight].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(1, 0)),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteBishop].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(2, 0)),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteQueen].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(3, 0)),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteKing].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(4, 0)),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteBishop].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(5, 0)),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteKnight].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(6, 0)),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteRook].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(7, 0)),
                              )

        self.black_pieces.add(ChessPiece(pieces.chessPieces[PieceType.BlackRook].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(0, 7)),
                              ChessPiece(pieces.chessPieces[PieceType.BlackKnight].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(1, 7)),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackBishop].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(2, 7)),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackQueen].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(3, 7)),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackKing].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(4, 7)),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackBishop].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(5, 7)),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackKnight].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(6, 7)),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackRook].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(7, 7)),
                              )

        for i in range(0, 8):
            self.white_pieces.add(ChessPiece(self.pieces.chessPieces[PieceType.WhitePawn].image,  # type: ignore
                                             self.board.convert_coordinates_to_board(i, 1)))
            self.black_pieces.add(ChessPiece(self.pieces.chessPieces[PieceType.BlackPawn].image,  # type: ignore
                                             self.board.convert_coordinates_to_board(i, 6)))

    def update(self):
        self.surface.blit(self.board.boardImage, self.board.boardRect)
        self.white_pieces.update()
        self.white_pieces.draw(self.surface)
        self.black_pieces.update()
        self.black_pieces.draw(self.surface)

    def run(self):
        pass

    def stop(self):
        pass
