#The making of GUI of the application is done in this file. The main window of the application is created here.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from window import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()