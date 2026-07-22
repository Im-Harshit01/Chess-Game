from piece import Pawn, Rook, Knight, Bishop, Queen, King


class Board:
    def __init__(self):
        self.squares = []
        self.selected_square = None
        self.turn = "white"
        
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
        
        end_square.piece = piece
        start_square.piece = None
        piece.has_moved = True

        self.switch_turn()

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
        pass

    def is_checkmate(self, color):
        # Return True if the given color is checkmated.
        pass