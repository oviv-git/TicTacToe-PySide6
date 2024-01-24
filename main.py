import sys
from src.game import TicTacToe, Play
from src.player import HumanPlayer, ComputerPlayer
from PySide6 import QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtUiTools import QUiLoader
from ui.ui_widget import Ui_Form
from ui.app_ui import init_app


def main():
    """
    TODO
    """

    from slots.game_board import BoardUi

    app, window = init_app()
    try:
        with open("ui/style.qss", "r") as file:
            stylesheet = file.read()
            app.setStyleSheet(stylesheet)
    except Exception as e:
        print(f"Stylesheet error: {e}")

    window.setWindowTitle("TicTacToe")
    board_ui = BoardUi(window)
    game = TicTacToe(board_ui)
    play = Play(game)

    window.show()

    app.exec()


if __name__ == "__main__":
    main()
