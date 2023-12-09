import pygame
from pygame.sprite import Sprite, Group

from src.chess.chessPieces import ChessPieces, PieceType
from src.chess.chessPiece import ChessPiece
from src.chess.chessBoard import ChessBoard


class Chess(Sprite):
    def __init__(self, surface: pygame.Surface):
        super().__init__()
        self.board = ChessBoard('ChessBoardTiles.png', surface.get_width() / 2, surface.get_height() / 2)
        # the pieces set
        self.pieces = ChessPieces('chessPieces.png')

        self.surface = surface
        self.running = False
        # all the pieces for one game
        self.white_pieces = Group()
        self.black_pieces = Group()
        # place pieces to starting position
        self.setup_default_chess_game(self.pieces)

    def setup_default_chess_game(self, pieces: ChessPieces):
        # set coordinates (0, 0) = bottom, left (7, 7) = top, right
        self.white_pieces.add(ChessPiece(pieces.chessPieces[PieceType.WhiteRook].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(0, 0).center),
                              ChessPiece(pieces.chessPieces[PieceType.WhiteKnight].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(1, 0).center),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteBishop].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(2, 0).center),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteQueen].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(3, 0).center),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteKing].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(4, 0).center),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteBishop].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(5, 0).center),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteKnight].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(6, 0).center),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteRook].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(7, 0).center),
                              )

        self.black_pieces.add(ChessPiece(pieces.chessPieces[PieceType.BlackRook].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(0, 7).center),
                              ChessPiece(pieces.chessPieces[PieceType.BlackKnight].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(1, 7).center),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackBishop].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(2, 7).center),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackQueen].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(3, 7).center),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackKing].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(4, 7).center),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackBishop].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(5, 7).center),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackKnight].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(6, 7).center),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackRook].image,  # type: ignore
                                         self.board.convert_coordinates_to_board(7, 7).center),
                              )

        for i in range(0, 8):
            self.white_pieces.add(ChessPiece(self.pieces.chessPieces[PieceType.WhitePawn].image,  # type: ignore
                                             self.board.convert_coordinates_to_board(i, 1).center))
            self.black_pieces.add(ChessPiece(self.pieces.chessPieces[PieceType.BlackPawn].image,  # type: ignore
                                             self.board.convert_coordinates_to_board(i, 6).center))

    def update(self):
        self.white_pieces.update()
        self.black_pieces.update()

    def draw(self):
        self.board.draw(self.surface)
        for piece in self.white_pieces:
            piece.draw(self.surface)
        for piece in self.black_pieces:
            piece.draw(self.surface)

    def run(self):
        self.running = True
        pieceSelected = False
        while self.running:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if not pieceSelected:
                        clicked_sprites = [s for s in self.white_pieces if s.rect.collidepoint(mouse_pos)]
                        if len(clicked_sprites) > 0:
                            pieceSelected = True
                        for sprite in clicked_sprites:
                            print("Sprite clicked: ", sprite)
                    if pieceSelected:
                        pass

            # update
            self.update()

            # draw
            self.draw()

            pygame.display.flip()
        print("stoped chess game")

    def stop(self):
        self.running = False
