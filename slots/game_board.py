from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QPushButton


class BoardUi(QObject):
    button_clicked = Signal(QPushButton)

    def __init__(self, window) -> None:
        super().__init__()
        self.window = window
        self.setup_board_connections()

    def setup_board_connections(self):
        for button in self.window.board_tiles:
            button.clicked.connect(lambda _=False, b=button: self.click_button(b))

    def finish_current_game(self):
        self.window.tab_menu.setCurrentIndex(0)
        for button in self.window.board_tiles:
            button.setEnabled(True)
            button.setText('')

    def disable_all_tiles(self):
        for button in self.window.board_tiles:
            button.setEnabled(False)

    def click_button(self, button):
        button.setEnabled(False)
        self.button_clicked.emit(button)

    def update_score(label, score):
        pass

    def delay_action(self, delay, function):
        QTimer.singleShot(delay, function)
