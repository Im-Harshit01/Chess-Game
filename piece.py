from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        pass


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        pass


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        pass


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        pass


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        pass


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        pass


class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        pass