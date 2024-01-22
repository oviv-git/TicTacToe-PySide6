import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QMainWindow,
    QComboBox,
    QPushButton,
    QLabel,
)
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = QFile("ui/Widget.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file, self)

        # Initializing the selection of the player types from the QComboBoxes
        self.playerSelections = []
        for i in range(1, 3):
            comboBox = f"player_{i}Selection"
            self.playerSelections.append(
                self.window.findChild(QtWidgets.QComboBox, comboBox)
            )

        # Initializing the game results label
        self.game_results_label = self.window.findChild(
            QtWidgets.QLabel, "gameResultsLabel"
        )

        # Initialzing each players score next to their selection
        self.player_score_labels = []
        for i in range(1, 3):
            label = f"player_{i}Score"
            self.player_score_labels.append(
                self.window.findChild(QtWidgets.QLabel, label)
            )

        # Initializing the tab and then hiding the tab bar
        self.tab_menu = self.window.findChild(QtWidgets.QTabWidget, "tabWidget")
        self.tab_menu.tabBar().hide()

        # Initializing the start game button
        self.start_game_button = self.window.findChild(
            QtWidgets.QPushButton, "startGameButton"
        )

        # Initializing a list of the labels inside of the game tab
        self.game_labels = []
        for i in range(1, 3):
            label_name = f"gameLabel_{i}"
            self.game_labels.append(self.window.findChild(QtWidgets.QLabel, label_name))

        # Initializing a list of the board tiles
        self.board_tiles = []
        for i in range(1, 10):
            tile_name = f"tile_{i}"
            self.board_tiles.append(
                self.window.findChild(QtWidgets.QPushButton, tile_name)
            )


def init_app():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.resize(600, 600)
    return app, main_window
