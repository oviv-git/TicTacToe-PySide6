import sys

from src.game import TicTacToe, Play
from src.player import HumanPlayer
from PySide6 import QtWidgets
# from PySide6.QtCore import QtWidget
from PySide6.QtWidgets import QWidget
from ui.ui_widget import Ui_Form


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TicTacToe")

def main():
    # game = TicTacToe()
    # player_1 = HumanPlayer()
    # player_2 = HumanPlayer()
    # play = Play(game, player_1, player_2)
    
    app = QtWidgets.QApplication(sys.argv)

    window = Widget()
    window.show()

    app.exec()
    # t = TicTacToe() 
    # print(t)

if __name__ == "__main__":
    main()
