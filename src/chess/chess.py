import pygame
from pygame.sprite import Sprite, Group

from src.chess.chessPieces import ChessPieces
from src.chess.chessPiece import ChessPiece
from src.chess.chessBoard import ChessBoard, ChessTile
from src.chess.pieceType import PieceType


class Chess(Sprite):
    def __init__(self, surface: pygame.Surface):
        super().__init__()
        # the board tiles
        self.board = ChessBoard('ChessBoardTiles.png', surface.get_width() / 2, surface.get_height() / 2)
        # the pieces set
        self.pieces = ChessPieces('chessPieces.png')

        self.surface = surface
        self.running = False
        # all the pieces for one game
        self.white_pieces: Group[ChessPiece] = Group()
        self.black_pieces: Group[ChessPiece] = Group()
        # place pieces to starting position
        self.setup_default_chess_game(self.pieces)
        self.all_pieces = self.white_pieces.add(self.black_pieces)  # type: ignore

    def setup_default_chess_game(self, pieces: ChessPieces):
        # set coordinates (0, 0) = bottom, left (7, 7) = top, right
        # pieces all with same height and width for calculation of tope left position in a tile
        pieceSize = self.board.tileSize
        self.white_pieces.add(ChessPiece(pieces.chessPieces[PieceType.WhiteRook].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(0, 0).topleft,
                                                          (pieceSize, pieceSize)),
                                         (0, 0),
                                         PieceType.WhiteRook),
                              ChessPiece(pieces.chessPieces[PieceType.WhiteKnight].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(1, 0).topleft,
                                                          (pieceSize, pieceSize)),
                                         (1, 0),
                                         PieceType.WhiteKnight),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteBishop].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(2, 0).topleft,
                                                          (pieceSize, pieceSize)),
                                         (2, 0),
                                         PieceType.WhiteBishop),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteQueen].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(3, 0).topleft,
                                                          (pieceSize, pieceSize)),
                                         (3, 0),
                                         PieceType.WhiteQueen),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteKing].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(4, 0).topleft,
                                                          (pieceSize, pieceSize)),
                                         (4, 0),
                                         PieceType.WhiteKing),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteBishop].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(5, 0).topleft,
                                                          (pieceSize, pieceSize)),
                                         (5, 0),
                                         PieceType.WhiteBishop),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteKnight].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(6, 0).topleft,
                                                          (pieceSize, pieceSize)),
                                         (6, 0),
                                         PieceType.WhiteKnight),
                              ChessPiece(self.pieces.chessPieces[PieceType.WhiteRook].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(7, 0).topleft,
                                                          (pieceSize, pieceSize)),
                                         (7, 0),
                                         PieceType.WhiteRook),
                              )
        self.board.get_tile_at((0, 0)).set_piece(PieceType.WhiteRook)
        self.board.get_tile_at((1, 0)).set_piece(PieceType.WhiteKnight)
        self.board.get_tile_at((2, 0)).set_piece(PieceType.WhiteBishop)
        self.board.get_tile_at((3, 0)).set_piece(PieceType.WhiteQueen)
        self.board.get_tile_at((4, 0)).set_piece(PieceType.WhiteKing)
        self.board.get_tile_at((5, 0)).set_piece(PieceType.WhiteBishop)
        self.board.get_tile_at((6, 0)).set_piece(PieceType.WhiteKnight)
        self.board.get_tile_at((7, 0)).set_piece(PieceType.WhiteRook)

        self.black_pieces.add(ChessPiece(pieces.chessPieces[PieceType.BlackRook].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(0, 7).topleft,
                                                          (pieceSize, pieceSize)),
                                         (0, 7),
                                         PieceType.BlackRook),
                              ChessPiece(pieces.chessPieces[PieceType.BlackKnight].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(1, 7).topleft,
                                                          (pieceSize, pieceSize)),
                                         (1, 7),
                                         PieceType.BlackKnight),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackBishop].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(2, 7).topleft,
                                                          (pieceSize, pieceSize)),
                                         (2, 7),
                                         PieceType.BlackBishop),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackQueen].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(3, 7).topleft,
                                                          (pieceSize, pieceSize)),
                                         (3, 7),
                                         PieceType.BlackQueen),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackKing].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(4, 7).topleft,
                                                          (pieceSize, pieceSize)),
                                         (4, 7),
                                         PieceType.BlackKing),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackBishop].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(5, 7).topleft,
                                                          (pieceSize, pieceSize)),
                                         (5, 7),
                                         PieceType.BlackBishop),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackKnight].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(6, 7).topleft,
                                                          (pieceSize, pieceSize)),
                                         (6, 7),
                                         PieceType.BlackKnight),
                              ChessPiece(self.pieces.chessPieces[PieceType.BlackRook].image,  # type: ignore
                                         pygame.rect.Rect(self.board.convert_coordinates_to_board(7, 7).topleft,
                                                          (pieceSize, pieceSize)),
                                         (7, 7),
                                         PieceType.BlackRook),
                              )
        self.board.get_tile_at((0, 7)).set_piece(PieceType.BlackRook)
        self.board.get_tile_at((1, 7)).set_piece(PieceType.BlackKnight)
        self.board.get_tile_at((2, 7)).set_piece(PieceType.BlackBishop)
        self.board.get_tile_at((3, 7)).set_piece(PieceType.BlackQueen)
        self.board.get_tile_at((4, 7)).set_piece(PieceType.BlackKing)
        self.board.get_tile_at((5, 7)).set_piece(PieceType.BlackBishop)
        self.board.get_tile_at((6, 7)).set_piece(PieceType.BlackKnight)
        self.board.get_tile_at((7, 7)).set_piece(PieceType.BlackRook)

        for i in range(0, 8):
            self.white_pieces.add(ChessPiece(self.pieces.chessPieces[PieceType.WhitePawn].image,  # type: ignore
                                             pygame.rect.Rect(self.board.convert_coordinates_to_board(i, 1).topleft,
                                                              (pieceSize, pieceSize)),
                                             (i, 1),
                                             PieceType.WhitePawn))
            self.board.get_tile_at((i, 1)).set_piece(PieceType.WhitePawn)
            self.black_pieces.add(ChessPiece(self.pieces.chessPieces[PieceType.BlackPawn].image,  # type: ignore
                                             pygame.rect.Rect(self.board.convert_coordinates_to_board(i, 6).topleft,
                                                              (pieceSize, pieceSize)),
                                             (i, 6),
                                             PieceType.BlackPawn))
            self.board.get_tile_at((i, 6)).set_piece(PieceType.BlackPawn)

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
        clicked_sprite: ChessPiece = None
        while self.running:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if not pieceSelected:
                        clicked_sprite = [s for s in self.white_pieces if s.rect.collidepoint(mouse_pos)][0]
                        if clicked_sprite is not None:
                            pieceSelected = True
                            print("clicke piece is of type: " + str(clicked_sprite.pieceType))
                    if pieceSelected:
                        possible_moves = ChessPieces.get_possible_moves(clicked_sprite, self.board)
                        clicked_tile_sprite = [s for s in self.board.boardTiles if s.rect.collidepoint(mouse_pos)][0]
                        if clicked_tile_sprite is not None:
                            if possible_moves.count(clicked_tile_sprite) > 0:
                                clicked_sprite.move(clicked_tile_sprite.get_pos()[0], clicked_tile_sprite.get_pos()[1], self.board)

            # update
            self.update()

            # draw
            self.draw()

            pygame.display.flip()
        print("stoped chess game")

    def stop(self):
        self.running = False
