import pygame
from pygame.sprite import Sprite, Group

from src.chess.chessPieces import ChessPieces, is_white_piece
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

        # states/rules of the game
        self.surface = surface
        self.running = False
        self.pieceSelected = False
        self.whitesTurn = True
        self.castlingWhitePossible = [True, True]    # if either left or right rook or the king was moved         
        self.castlingBlackPossible = [True, True]    # if either left or right rook or the king was moved      
        self.clickedPieceSprite = None
        self.clickedTileSprite = None
        # all the pieces for one game
        self.white_pieces: Group[ChessPiece] = Group()
        self.black_pieces: Group[ChessPiece] = Group()
        # place pieces to starting position
        self.setup_default_chess_game(self.pieces)
        # self.all_pieces = self.white_pieces.add(self.black_pieces)  # type: ignore

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

    def select_piece(self, pos):
        if self.whitesTurn:
            self.clickedPieceSprite = [s for s in self.white_pieces if s.rect.collidepoint(pos)]
        elif not self.whitesTurn:
            self.clickedPieceSprite = [s for s in self.black_pieces if s.rect.collidepoint(pos)]
        self.clickedPieceSprite = self.clickedPieceSprite[0] if self.clickedPieceSprite else None
        if self.clickedPieceSprite is not None:
            print("clicked piece is of type: " + str(self.clickedPieceSprite.pieceType))
    
    def clicked_on_tile(self, pos, possible_moves):
        # if own color selects a new piece switch to that piece
        if self.clickedTileSprite.occupied is not None and \
                self.whitesTurn is is_white_piece(self.clickedTileSprite.occupied):
            if self.whitesTurn and is_white_piece(self.clickedTileSprite.occupied):
                self.clickedPieceSprite = [s for s in self.white_pieces if
                                        s.rect.collidepoint(pos)]
            if not self.whitesTurn and not is_white_piece(self.clickedTileSprite.occupied):
                self.clickedPieceSprite = [s for s in self.black_pieces if
                                        s.rect.collidepoint(pos)]
            self.clickedPieceSprite = self.clickedPieceSprite[0] if self.clickedPieceSprite else None
            # reset possible moves
            for posMoves in possible_moves:
                posMoves.selected = False
            # dont know why but sometimes no sprite is selected (should not happen) so just skip and
            # unselect currently selected piece
            if self.clickedPieceSprite is None:
                self.pieceSelected = False
                return
            possible_moves = self.pieces.get_possible_moves(self.clickedPieceSprite, self.board, self.castlingWhitePossible, self.castlingBlackPossible)
            self.pieces.filter_possible_moves_on_check(self.black_pieces, self.white_pieces, self.board,
                                                        possible_moves, self.clickedPieceSprite)
            for posMoves in possible_moves:
                posMoves.selected = True
            print('switched selected piece to: ' + str(self.clickedPieceSprite.pieceType))
        # a possible move got selected
        if possible_moves.count(self.clickedTileSprite) > 0:
            # a piece got captured
            if self.clickedTileSprite.occupied is not None:
                # remove piece that got captured
                if self.whitesTurn:
                    captured_piece_sprite = [s for s in self.black_pieces if
                                                s.rect.collidepoint(pos)]
                    captured_piece_sprite = captured_piece_sprite[0] if \
                        captured_piece_sprite else None
                    self.black_pieces.remove(captured_piece_sprite)
                if not self.whitesTurn:
                    captured_piece_sprite = [s for s in self.white_pieces if
                                                s.rect.collidepoint(pos)]
                    captured_piece_sprite = captured_piece_sprite[0] if \
                        captured_piece_sprite else None
                    self.white_pieces.remove(captured_piece_sprite)
            # reset turn for other player and change tile and piece properties
            self.check_change_piece_pos()
            checked = self.pieces.is_king_checked(self.clickedPieceSprite, self.board)
            self.pieceSelected = False
            self.whitesTurn = not self.whitesTurn
            self.clickedPieceSprite = None
            for posMoves in possible_moves:
                posMoves.selected = False

    def check_change_piece_pos(self):
        from_tile = self.board.get_tile_at((self.clickedPieceSprite.posX, self.clickedPieceSprite.posY))
        to_tile = self.clickedTileSprite
        chess_piece = self.clickedPieceSprite
        if (chess_piece.pieceType == PieceType.WhiteKing):
            # king moved so no castling possible anymore
            self.castlingWhitePossible[0] = False
            self.castlingWhitePossible[1] = False
            self.do_castling()
        elif (chess_piece.pieceType == PieceType.BlackKing):
            # king moved so no castling possible anymore
            self.castlingBlackPossible[0] = False
            self.castlingBlackPossible[1] = False
            self.do_castling()
        if (chess_piece.pieceType == PieceType.WhiteRook or chess_piece.pieceType == PieceType.BlackRook):
            if (from_tile.get_pos()[0] == 0):
                self.castlingWhitePossible[0] = False
                self.castlingBlackPossible[0] = False
            if (from_tile.get_pos()[1] == 7):
                self.castlingWhitePossible[1] = False
                self.castlingBlackPossible[1] = False
        self.board.change_piece_pos(from_tile, to_tile, chess_piece)

    def do_castling(self):
        from_tile = self.board.get_tile_at((self.clickedPieceSprite.posX, self.clickedPieceSprite.posY))
        to_tile = self.clickedTileSprite
        dist = from_tile.get_pos()[0] - to_tile.get_pos()[0]
        if self.whitesTurn:
            y = 0
        else:
            y = 7
        if dist > 1:
            from_tile_knight = self.board.get_tile_at((to_tile.get_pos()[0] - 2, to_tile.get_pos()[1]))
            to_tile_knight   = self.board.get_tile_at((to_tile.get_pos()[0] + 1, to_tile.get_pos()[1]))
            chess_piece_knight = self.get_piece_at(0, y)
        elif dist < -1:
            from_tile_knight = self.board.get_tile_at((to_tile.get_pos()[0] + 1, to_tile.get_pos()[1]))
            to_tile_knight   = self.board.get_tile_at((to_tile.get_pos()[0] - 1, to_tile.get_pos()[1]))
            chess_piece_knight = self.get_piece_at(7, y)
        self.board.change_piece_pos(from_tile_knight, to_tile_knight, chess_piece_knight)

    def get_piece_at(self, x, y):
        print ("get chess piece at" + str(x) + " : " + str(y))
        if (self.whitesTurn):
            pieceAt = [piece for piece in self.white_pieces if piece.posX == x and piece.posY == y]
        else:
            pieceAt = [piece for piece in self.black_pieces if piece.posX == x and piece.posY == y]
        return pieceAt[0]

    def clicked_left_mouse_button(self):
        # check winning condition
        mouse_pos = pygame.mouse.get_pos()
        # if no ChessPiece is selected
        if not self.pieceSelected:
            self.select_piece(mouse_pos)
            if (self.clickedPieceSprite is not None):
                self.pieceSelected = True
        if self.pieceSelected:
            # mark possible moves on ChessBoard
            possible_moves = self.pieces.get_possible_moves(self.clickedPieceSprite, self.board, self.castlingWhitePossible, self.castlingBlackPossible)
            self.pieces.filter_possible_moves_on_check(self.black_pieces, self.white_pieces, self.board,
                                                        possible_moves, self.clickedPieceSprite)
            # print(str(self.clickedPieceSprite.pieceType) + " still has possible moves")
            # print(possible_moves)
            for posMoves in possible_moves:
                posMoves.selected = True
            self.clickedTileSprite = [s for s in self.board.boardTiles if s.rect.collidepoint(mouse_pos)]
            self.clickedTileSprite = self.clickedTileSprite[0] if self.clickedTileSprite else None
            # clicked on a tile
            if self.clickedTileSprite is not None:
                self.clicked_on_tile(mouse_pos, possible_moves)
        if (self.whitesTurn and self.pieces.checkmate(self.white_pieces, self.black_pieces, self.board, self.whitesTurn)):
            print("black won")
        elif (not self.whitesTurn and self.pieces.checkmate(self.white_pieces, self.black_pieces, self.board, self.whitesTurn)):
            print("white won")

    def reset_game_state(self):
        # setup states of the game
        self.running = True
        self.pieceSelected = False
        self.whitesTurn = True
        self.castlingWhitePossible = [True, True]    # if either left or right rook or the king was moved         
        self.castlingBlackPossible = [True, True]    # if either left or right rook or the king was moved      
        self.clickedPieceSprite = None

    def update(self):
        self.white_pieces.update()
        self.black_pieces.update()

    def draw(self):
        self.board.draw(self.surface)
        for piece in self.white_pieces:
            piece.draw(self.surface)
        for piece in self.black_pieces:
            piece.draw(self.surface)
        self.board.draw_selected(self.surface)

    def stop(self):
        self.running = False

    def run(self):
        self.reset_game_state()
        while self.running:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left mouse button
                    print("left mouse click")
                    self.clicked_left_mouse_button()

            # update
            self.update()

            # draw
            self.draw()

            pygame.display.flip()
        print("stoped chess game")


