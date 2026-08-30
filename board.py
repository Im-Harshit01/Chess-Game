from piece import Pawn, Rook, Knight, Bishop, Queen, King
import piece


class Board:
    def __init__(self):
        self.squares = []
        self.selected_square = None
        self.turn = "white"
        self.game_over = False
        self.winner = None
        
    def setup_pieces(self):
        # Place all pieces in their starting positions.
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for col in range(8):
            self.get_square(1, col).piece = Pawn("black")
            self.get_square(6, col).piece = Pawn("white")

        for col in range(8):
            self.get_square(0, col).piece = pieces[col]("black")
            self.get_square(7, col).piece = pieces[col]("white")

    def get_square(self, row, col):
        # Return the square at the given position.
        return self.squares[row][col]

    def move_piece(self, start_row, start_col, end_row, end_col):
        # Stops the game if checkmate is detected after a move.
        if self.game_over:
            return False
        
        # Move a piece if the move is legal.
        start_square = self.get_square(start_row, start_col)
        end_square = self.get_square(end_row, end_col)
        piece = start_square.piece

        if piece is None:
            return False
        
        if piece.color != self.turn:
            return False
        
        destination_piece = end_square.piece
        if (
            destination_piece is not None and
            destination_piece.color == piece.color
        ):
            return False
        
        if not piece.is_valid_move(
            self,
            start_row,
            start_col,
            end_row,
            end_col
        ):
            return False
        
        captured_piece = end_square.piece

        # Move temporarily
        start_square.piece = None
        end_square.piece = piece

        # Look for check after the move
        if self.is_in_check(piece.color):
            start_square.piece = piece          #Undo the move
            end_square.piece = captured_piece
            return False

        # Move is valid, finalize it
        piece.has_moved = True
        self.switch_turn()

        if self.is_checkmate(self.turn):
            self.game_over = True
            self.winner = piece.color

        return True


    def select_square(self, row, col):
        # Handle selecting a square.
        self.selected_square = self.get_square(row, col)

    def deselect_square(self):
        # Clear the current selection.
        self.selected_square = None

    def switch_turn(self):
        # Switch the current player's turn.
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def is_in_check(self, color):
        # Return True if the given color is in check.
        king_square = None

        for row in self.squares:
            for square in row:
                piece = square.piece
                if piece is not None and isinstance(piece, King) and piece.color == color:
                    king_square = square
                    break

            if king_square is not None:
                    break

        for row in range(8):
            for col in range(8):
                square = self.get_square(row, col)
                piece = square.piece
                if piece is not None and piece.color != color:
                    if piece.is_valid_move(self, row, col, king_square.row, king_square.col):
                        return True        
        return False


    def is_checkmate(self, color):
        # Return True if the given color is checkmated.

        if not self.is_in_check(color):
            return False

        for row in range(8):
            for col in range(8):
                piece = self.get_square(row, col).piece

                if piece is None or piece.color != color:
                    continue

                for end_row in range(8):
                    for end_col in range(8):

                        if not piece.is_valid_move(
                            self, row, col, end_row, end_col
                        ):
                            continue

                        destination = self.get_square(end_row, end_col)

                        if destination.piece is not None and destination.piece.color == color:
                            continue

                        captured = destination.piece

                        self.get_square(row, col).piece = None
                        destination.piece = piece

                        safe = not self.is_in_check(color)

                        self.get_square(row, col).piece = piece
                        destination.piece = captured

                        if safe:
                            return False

        return True