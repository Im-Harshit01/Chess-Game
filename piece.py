from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color):
        self._color = color
        self.has_moved = False

    @property
    def color(self):
        return self._color
    
    @property
    @abstractmethod
    def symbol(self):
        pass

    @abstractmethod
    def is_valid_move(self, board, start_row, start_col, end_row, end_col):
        pass


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    @property
    def symbol(self):
        return "♙" if self.color == "white" else "♟"


    def is_valid_move(self, board, start_row, start_col, end_row, end_col):
        pass


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    @property
    def symbol(self):
        return "♖" if self.color == "white" else "♜"  
     
    def is_valid_move(self, board, start_row, start_col, end_row, end_col):
        if start_row == end_row and start_col == end_col:
           return False
         
        if start_row != end_row and start_col != end_col:
            return False
        
        row_step = 0
        col_step = 0
        
        if end_row > start_row:
            row_step = 1
        elif end_row < start_row:
            row_step = -1

        if end_col > start_col:
            col_step = 1
        elif end_col < start_col:
            col_step = -1

        current_row = start_row + row_step
        current_col = start_col + col_step

        while (current_row, current_col) != (end_row, end_col):
            square = board.get_square(current_row, current_col)
        
            if square.piece:
                return False
        
            current_row += row_step
            current_col += col_step

        return True


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    @property
    def symbol(self):
        return "♘" if self.color == "white" else "♞"

    def is_valid_move(self, board, start_row, start_col, end_row, end_col):
        if start_row == end_row and start_col == end_col:
            return False
        
        row_difference = abs(end_row - start_row)
        col_difference = abs(end_col - start_col)

        if (row_difference == 2 and col_difference == 1) or \
            (row_difference == 1 and col_difference == 2):
            return True
        return False


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    @property
    def symbol(self):
        return "♗" if self.color == "white" else "♝"

    def is_valid_move(self, board, start_row, start_col, end_row, end_col):
        row_difference = abs(end_row - start_row)
        col_difference = abs(end_col - start_col)

        if row_difference != col_difference:
            return False
        row_step = 0
        col_step = 0

        if end_row > start_row:
            row_step = 1
        elif end_row < start_row:
            row_step = -1

        if end_col > start_col:
            col_step = 1
        elif end_col < start_col:
            col_step = -1

        current_row = start_row + row_step
        current_col = start_col + col_step

        while (current_row, current_col) != (end_row, end_col):
            square = board.get_square(current_row, current_col)

            if square.piece:
                return False

            current_row += row_step
            current_col += col_step

        return True
        

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    @property
    def symbol(self):
        return "♕" if self.color == "white" else "♛"

    def is_valid_move(self, board, start_row, start_col, end_row, end_col):
        rook = Rook(self.color)
        bishop = Bishop(self.color)

        if rook.is_valid_move:
            return True
        
        if bishop.is_valid_move:
            return True


class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    @property
    def symbol(self):
        return "♔" if self.color == "white" else "♚"

    def is_valid_move(self, board, start_row, start_col, end_row, end_col):
        pass