from piece import Pawn, Rook, Knight, Bishop, Queen, King


class Board:
    def __init__(self):
        self.squares = []
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self.turn = "white"

    def setup_pieces(self):
        # Place all pieces in their starting positions.
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for col in range(8):
            self.get_square(1, col).piece = pawn("black")
            self.get_square(6, col).piece = pawn("white")

    def get_square(self, row, col):
        # Return the square at the given position.
        return self.squares[row][col]

    def move_piece(self, start_row, start_col, end_row, end_col):
        # Move a piece if the move is legal.
        pass

    def select_square(self, row, col):
        # Handle selecting a square.
        pass

    def deselect_square(self):
        # Clear the current selection.
        pass

    def switch_turn(self):
        # Switch the current player's turn.
        pass

    def is_in_check(self, color):
        # Return True if the given color is in check.
        pass

    def is_checkmate(self, color):
        # Return True if the given color is checkmated.
        pass