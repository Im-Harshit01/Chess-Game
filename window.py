#This handels the main window of the application 

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QFrame


class piece:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Square(QFrame):
    clicked = pyqtSignal(int, int)

    def __init__(self, row, col, color):     # This represents a square on the chessboard, with its row and column indices.
        super().__init__()
        self.row = row
        self.col = col
        self.color = color
        self.piece = None

    def mousePressEvent(self, event):   #If the square is clicked, it emits a signal with its row and column indices.
        self.clicked.emit(self.row, self.col)


# The MainWindow class represents the main window of the chess game application.
#  It creates an 8x8 grid of Square widgets to represent the chessboard.
#  Each square is styled with alternating colors (white and black) to create the appearance of a chessboard.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chess Game")
        self.setFixedSize(500, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid = QGridLayout()
        self.central_widget.setLayout(self.grid)

        self.squares = []
        self.selected_square = None
        self.selected_piece = None


        for row in range(8):
            row_list = []

            for col in range(8):

                if (row + col) % 2 == 0:
                    color = "white"
                    if row == 1:
                        square.piece = piece("pawn", "black")
                    elif row == 6:
                        square.piece = piece("pawn", "white")
                else:
                    color = "black"


                square = Square(row, col, color)
                square.setStyleSheet(f"background-color: {square.color};")

                square.clicked.connect(self.on_square_clicked)

                self.grid.addWidget(square, row, col)
                row_list.append(square)

            self.squares.append(row_list)

    def on_square_clicked(self, row, col):
        square = self.squares[row][col]

        if self.selected_square is not None:
            self.selected_square.setStyleSheet(
                f"background-color: {self.selected_square.color};"
            )

        self.selected_square = square
        self.selected_square.setStyleSheet("background-color: #b8b6b6;")