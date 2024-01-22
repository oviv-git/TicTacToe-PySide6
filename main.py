import sys

from src.game import TicTacToe, Play
from src.player import HumanPlayer, ComputerPlayer
from PySide6 import QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtUiTools import QUiLoader
from ui.ui_widget import Ui_Form
from ui.app_ui import init_app


# class Widget(QWidget, Ui_Form):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.setWindowTitle("TicTacToe")


def main():
    from slots.game_board import BoardUi

    # Map to safely select the type of player class with the comboBoxes

    app, window = init_app()
    window.setWindowTitle("TicTacToe")
    board_ui = BoardUi(window)
    game = TicTacToe(board_ui)
    # print(window.playerSelections[0].currentText())
    # player_1 = playerMap[window.playerSelections[0].currentText()]()
    # player_2 = playerMap[window.playerSelections[1].currentText()]()
    # player_1 = HumanPlayer()
    # player_2 = HumanPlayer()
    player_1 = ComputerPlayer()
    player_2 = ComputerPlayer()
    # player_2 = ComputerPlayer()
    play = Play(game)

    window.show()

    app.exec()


if __name__ == "__main__":
    main()

    # app = QApplication(sys.argv)
    # ui_file = QFile("ui/Widget.ui")
    # ui_file.open(QFile.ReadOnly)

    # loader = QUiLoader()
    # window = loader.load(ui_file)
    # window.setWindowTitle("TicTacToe")

    # app = MainApplicationWindow(sys.argv)

    # window = Widget()

    # app = QtWidgets.QApplication(sys.argv)
