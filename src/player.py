class HumanPlayer:
    def __init__(self):
        pass

    def __str__(self) -> str:
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def make_move(self):
        return int(input("make a move: "))
