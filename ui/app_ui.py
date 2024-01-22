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
# from PySide6.QtUiTools import QUiLoader
from ui.Widget import Ui_Widget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.ui = Ui_Widget()
        self.ui.setupUi(central_widget)
        
        # Initializing the selection of the player types from the QComboBoxes
        self.playerSelections = [self.ui.player_1Selection, self.ui.player_2Selection]
        
        # Initializing the game results label
        self.game_results_label = self.ui.gameResultsLabel
        
        # Initializing each players score next to their selection
        self.player_score_labels = [self.ui.player_1Score, self.ui.player_2Score]
        
        # Initializing the tab and then hiding the tab bar
        self.tab_menu = self.ui.tabWidget
        self.tab_menu.tabBar().hide()

        # Initializing the start game button
        self.start_game_button = self.ui.startGameButton
        
        # Initializing a list of the labels inside of the game tab
        self.game_labels = [self.ui.gameLabel_1, self.ui.gameLabel_2]
        
        # Initializing a list of the board tiles
        self.board_tiles = []
        for i in range(1, 10):
            tile_name = f"tile_{i}"
            self.board_tiles.append(getattr(self.ui, tile_name))


def init_app():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.resize(600, 600)
    return app, main_window
