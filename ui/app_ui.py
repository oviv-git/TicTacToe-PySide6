import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = QFile('ui/Widget.ui')
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file, self)
        self.window.setWindowTitle('TicTacToe')

        self.board_tiles = []
        for i in range(1, 10):
            tile_name = f'tile_{i}'
            self.board_tiles.append(self.window.findChild(QtWidgets.QPushButton, tile_name))
        

def init_app():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.resize(600, 600)
    return app, main_window
