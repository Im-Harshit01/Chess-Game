#This handels the main window of the application 
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QFrame


class Square(QFrame):
    clicked = pyqtSignal(int, int)

    def __init__(self, row, col):     # This represents a square on the chessboard, with its row and column indices.
        super().__init__()
        self.row = row
        self.col = col

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

        for row in range(8):
            row_list = []

            for col in range(8):
                square = Square(row, col)

                if (row + col) % 2 == 0:
                    square.setStyleSheet("background-color: white;")
                else:
                    square.setStyleSheet("background-color: black;")

                square.clicked.connect(self.on_square_clicked)

                self.grid.addWidget(square, row, col)
                row_list.append(square)

            self.squares.append(row_list)

    def on_square_clicked(self, row, col):
        print(f"Clicked: {row}, {col}")
