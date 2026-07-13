#This handels the main window of the application 

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QFrame, QLabel, QVBoxLayout, QGraphicsDropShadowEffect
from numpy import square

from piece import Piece


class Square(QFrame):
    clicked = pyqtSignal(int, int)

    def __init__(self, row, col, color):     # This represents a square on the chessboard, with its row and column indices.
        super().__init__()
        self.row = row
        self.col = col
        self.color = color
        self.piece = None
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.label = QLabel()
        self.layout.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            font-size: 40px;
            font-family: "DejaVu Sans";
        """)        
        self.setFixedSize(62, 62)


    def update_display(self):   #This updates the display of the square based on the piece it contains.

        if self.piece is not None:
            if self.piece.color == "white":
                # Show ♙
                self.label.setText("♙")
            else:
                # Show ♟
                self.label.setText("♟")
        else:
            self.label.setText("")


    def mousePressEvent(self, event):   #If the square is clicked, it emits a signal with its row and column indices.
        self.clicked.emit(self.row, self.col)


# The MainWindow class represents the main window of the chess game application.
#  It creates an 8x8 grid of Square widgets to represent the chessboard.
#  Each square is styled with alternating colors (white and grey) to create the appearance of a chessboard.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chess Game")
        self.setFixedSize(500, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.central_widget.setLayout(self.grid)

        self.squares = []
        self.selected_square = None


        for row in range(8):
            row_list = []

            for col in range(8):

                if (row + col) % 2 == 0:
                    color = "white"                
                else:
                    color = "grey"

                square = Square(row, col, color)

                if row == 1:
                    pawn = Piece("black")
                    square.piece = pawn
                elif row == 6:
                    pawn = Piece("white")
                    square.piece = pawn

                square.update_display()

                square.setStyleSheet(f"background-color: {square.color};")

                square.clicked.connect(self.on_square_clicked)

                self.grid.addWidget(square, row, col)
                row_list.append(square)

            self.squares.append(row_list)

    def on_square_clicked(self, row, col):
        square = self.squares[row][col]

        #First Click

        if self.selected_square is None:
            if square.piece is not None:
                self.selected_square = square
                self.selected_square.setStyleSheet("background-color: #b8b6b6;")
            return

        #Second Click

        if square.piece is not None:
            if square.piece.color == self.selected_square.piece.color:
                self.selected_square.setStyleSheet(
                    f"background-color: {self.selected_square.color};"
                )

                self.selected_square = square
                self.selected_square.setStyleSheet("background-color: #b8b6b6;")

                return

        square.piece = self.selected_square.piece
        self.selected_square.piece = None

        square.update_display()
        self.selected_square.update_display()

        self.selected_square.setStyleSheet(
            f"background-color: {self.selected_square.color};"
        )
        self.selected_square = None
