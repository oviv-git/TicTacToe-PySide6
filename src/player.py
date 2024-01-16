import random

class HumanPlayer:
    def __init__(self):
        self.symbol = ""

    def __str__(self):
        return f'Human Player: {self.symbol}'

    def set_symbol(self, symbol):
        self.symbol = symbol

    def make_move(self, button, available_moves):
        return str(button.objectName()).split("_")[1]

    def get_symbol(self):
        return self.symbol


class ComputerPlayer(HumanPlayer):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'CPU: {self.symbol}'

    def make_move(self, button, available_moves):
        return random.choice(available_moves)
