from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QPushButton


class BoardUi(QObject):
    """
    Responsible for managing the Ui elements of the game. Connects the slots of the
    board tiles, all the labels that display information about the current players
    and the results of the games.

    :ivar button_clicked: button_clicked (Signal): Signal emitted when a signal (QPushButton)
    is clicked so it can be utilized in the Play class in src.game.py
    """

    button_clicked = Signal(QPushButton)

    def __init__(self, window) -> None:
        """Initializies the BoardUi object

        Keyword arguments:

        Initializes the window, sets up all the board connections and sets up the label fonts
        argument -- description
        Return: return_description
        """

        super().__init__()
        self.window = window
        self.setup_board_connections()
        self.label_font = self.window.game_labels[0].font()

    def setup_board_connections(self):
        for button in self.window.board_tiles:
            button.clicked.connect(lambda _=False, b=button: self.click_button(b))

    def finish_current_game(self):
        for button in self.window.board_tiles:
            button.setEnabled(True)
            button.setText("")
        self.window.tab_menu.setCurrentIndex(0)

    def disable_all_tiles(self):
        for button in self.window.board_tiles:
            button.setEnabled(False)

    def click_button(self, button):
        button.setEnabled(False)
        self.button_clicked.emit(button)

    def make_move(self, button, symbol):
        button.setEnabled(False)
        button.setText(symbol)

    def set_game_labels(self, players):
        for i in range(len(players)):
            self.window.game_labels[i].setText(f"{str(players[i])}")

    def reset_game_label(self):
        font = self.label_font
        font.setUnderline(False)

        for label in self.window.game_labels:
            label.setFont(font)

    def display_current_player_game_label(self, current_player):
        font = self.label_font
        font.setUnderline(True)

        current_label = self.window.game_labels[current_player]
        current_label.setFont(font)

    def update_score(self, winning_player):
        new_score = 1 + int(self.window.player_score_labels[winning_player].text())
        self.window.player_score_labels[winning_player].setText(str(new_score))

    def update_results_label(self, game_results):
        self.window.game_results_label.setText(game_results)

    def display_winning_tiles(self, winning_tiles):
        for tile in winning_tiles:
            # print(self.window.board_tiles[tile - 1].objectName())
            self.window.board_tiles[tile - 1].setProperty("class", "winningTile")
        


    def delay_action(self, delay, function, *args, **kwargs):
        QTimer.singleShot(delay, lambda: function(*args, **kwargs))
