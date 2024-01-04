import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = QFile('ui/Widget.ui')
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file, self)
        self.window.setWindowTitle('TicTacToe')


def init_app():
    app = QApplication(sys.argv)
#     ui_file = QFile("ui/Widget.ui")
#     ui_file.open(QFile.ReadOnly)
    main_window = MainWindow()
    main_window.resize(900, 900)
    # main_window.window.show()
    return app, main_window

#     loader = QUiLoader()
#     window = loader.load(ui_file)
#     window.setWindowTitle("TicTacToe")
#     return app, window