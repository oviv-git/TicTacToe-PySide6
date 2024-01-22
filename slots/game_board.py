from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QPushButton


class BoardUi(QObject):
    button_clicked = Signal(QPushButton)

    def __init__(self, window) -> None:
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

    def remove_game_label_underline(self):
        font = self.label_font
        font.setUnderline(False)

        for label in self.window.game_labels:
            label.setFont(font)

    def underline_current_player_game_label(self, current_player):
        font = self.label_font
        font.setUnderline(True)

        current_label = self.window.game_labels[current_player]
        current_label.setFont(font)

    def update_score(self, label):
        print(self.window.game_labels)

    def delay_action(self, delay, function, *args, **kwargs):
        QTimer.singleShot(delay, lambda: function(*args, **kwargs))
